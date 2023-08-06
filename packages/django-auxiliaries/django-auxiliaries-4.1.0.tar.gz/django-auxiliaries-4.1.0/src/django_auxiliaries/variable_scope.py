import threading
import copy

from types import SimpleNamespace

__all__ = ['register_variable_scope', 'reset_variable_scopes', 'initialise_variable_scope', 'load_variable_scope',
           'ArgumentInitialiser', 'Copy', 'EnvironmentVariable', 'WagtailPageMixin']


local = threading.local()


class ArgumentInitialiser:

    def __call__(self, env):
        return None


class Copy(ArgumentInitialiser):

    def __init__(self, value):
        self.value = value

    def __call__(self, env):
        return copy.copy(self.value)


class EnvironmentVariable(ArgumentInitialiser):

    class Missing:
        pass

    def __init__(self, identifier, default_value, copy_default=True, modifier=None):
        self.identifier = identifier
        self.default_value = default_value
        self.copy_default = copy_default
        self.modifier = modifier

    def __call__(self, env):

        value = env.get(self.identifier, self.Missing)

        if value is self.Missing:
            value = self.default_value

            if self.copy_default:
                value = copy.copy(value)
        elif callable(self.modifier):
            value = self.modifier(value)

        return value


def initialise_variable_scope(app_label, **kwargs):

    defaults = REGISTRY.get(app_label, None)

    if defaults:
        arguments = initialise_arguments(defaults)
        arguments.update(kwargs)
    else:
        arguments = kwargs

    scope = SimpleNamespace(**arguments)
    setattr(local, app_label, scope)
    return scope


def load_variable_scope(app_label, **kwargs):

    if not hasattr(local, app_label):
        scope = initialise_variable_scope(app_label, **kwargs)
    else:
        scope = getattr(local, app_label)

        if kwargs:
            scope.__dict__.update(kwargs)

    return scope


def initialise_arguments(defaults, env=None):

    env = env if env is not None else {}
    arguments = {}

    for key, value in defaults.items():

        if isinstance(value, ArgumentInitialiser):
            value = value(env) # noqa

        arguments[key] = value

    return arguments


REGISTRY = {}


def register_variable_scope(app_label, **defaults):
    REGISTRY[app_label] = defaults


def reset_variable_scopes(env):
    for app_label, defaults in REGISTRY.items():
        arguments = initialise_arguments(defaults, env)
        initialise_variable_scope(app_label, **arguments)


class WagtailPageMixin:

    def reset_variable_scopes(self, request):

        env = {
            'request': request,
            'page': self
        }

        reset_variable_scopes(env)

    def serve(self, request):
        self.reset_variable_scopes(request)
        return super().serve(request)  # noqa

    def serve_preview(self, request, preview_mode):
        self.reset_variable_scopes(request)
        return super().serve_preview(request, preview_mode)  # noqa
