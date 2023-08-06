import os
import importlib
import pkgutil
import configparser
import codecs
import graphlib
import weakref
import re

from django.utils.functional import cached_property

from importlib.metadata import distribution, requires, PackageNotFoundError

from .sandbox import determine_django_app_label

__all__ = ['resolve_app_dependencies']


def transitive_closure_of_requirements(package_name, requirements, requirements_by_package_name):
    explored_packages = set()
    requirements_closure = []

    stack = [(package_name, 0, requirements)]

    while stack:
        package_name, index, required_packages = stack[-1]

        r = None

        while index < len(required_packages):
            r = required_packages[index]

            if r not in explored_packages:
                break

            index += 1

        if index >= len(required_packages):
            stack.pop()
            continue

        explored_packages.add(r)
        requirements_closure.append(r)
        stack[-1] = package_name, index + 1, required_packages

        if r in requirements_by_package_name:
            stack.append((r, 0, requirements_by_package_name[r]))

    return requirements_closure


def get_apps_in_package(package_path):
    prefix, package_app = os.path.split(package_path)
    result = []

    for r, d, f in os.walk(package_path):

        if 'apps.py' in f:

            app_name = r

            if app_name.startswith(prefix):
                app_name = app_name[len(prefix) + 1:].replace(os.sep, '.').replace('-', '_')
                result.append(app_name)

    return result


def get_installed_packages_modules():
    result = {module.name: module for module in pkgutil.iter_modules() if module.ispkg}
    return result


class App:

    @cached_property
    def package(self):
        return self._package() if self._package is not None else None

    @cached_property
    def django_app_label(self):
        return self._django_app_label if self._django_app_label else self.name

    def __init__(self, name, import_path, path, config_path, package):
        self.name = name
        self.import_path = import_path
        self.path = path
        self.config_path = config_path

        self._package = weakref.ref(package) if package else None
        self._django_app_label = self.determine_django_app_label()

    def determine_django_app_label(self):

        if not self.config_path:
            return None

        # result = determine_django_app_label(self.import_path + ".apps")
        # return result
        return None

def split_path_components(path):
    result = []

    while path:
        path, component = os.path.split(path)

        if not component:
            break

        result.insert(0, component)

    return result


class Package:

    """
    @property
    def module(self):

        if self._module:
            return self._module

        try:
            self._module = importlib.import_module(self.name)
        except Exception:
            return None

        return self._module
    """

    def __init__(self, name, path, init_path):

        self.name = name
        self.path = path
        self.init_path = init_path
        self.distribution_path, self.distribution_name = self.determine_distribution()
        self._module = None
        self.requirements = self.determine_requirements()
        self.apps = self.load_apps()

    def load_apps(self):

        result = []

        path_components = split_path_components(self.path)

        for r, d, f in os.walk(self.path):

            has_apps = 'apps.py' in f
            has_models = 'models.py' in f
            has_models_module = 'models' in d
            has_views = 'views.py' in f
            has_views_module = 'views' in d

            is_app = has_apps or has_models or has_models_module or has_views or has_views_module

            if is_app:

                app_path_components = split_path_components(r)
                app_path_components = [self.name] + app_path_components[len(path_components):]
                app_path = '.'.join(app_path_components)

                app_name = os.path.basename(r)

                if app_name.startswith(self.name):
                    # app_name = app_name[len(self.name) + 1:].replace(os.sep, '.').replace('-', '_')
                    pass

                app = App(app_name, app_path, r, os.path.join(r, 'apps.py') if has_apps else None, self)
                result.append(app)

        return result

    REQUIREMENT_RE = re.compile(r'^([A-Za-z_][A-Za-z_0-9\-]*)')

    def determine_distribution(self):

        try:
            dist = distribution(self.name)
        except PackageNotFoundError:
            return None, None

        result = [file.parent for file in dist.files if file.name == 'METADATA']

        if not result:
            return None, None

        result = str(dist.locate_file(result[0]))
        name = dist.metadata.get('Name', None)

        return result, name

    def determine_requirements(self):

        try:
            requirements = requires(self.name)
        except PackageNotFoundError:

            p = os.path.join(self.path, 'requirements.txt')

            try:
                with codecs.open(p, encoding="utf-8") as file:
                    requirements = file.read().split(os.linesep)
            except Exception:
                return []

            requirements = [r for r in requirements if r and not r.strip().startswith('#')]

        if not requirements:
            requirements = []

        # requirements = [Package.REQUIREMENT_RE.match(r).group(1).replace('-', '_').lower() for r in requirements]

        requirements = [Package.REQUIREMENT_RE.match(r).group(1) for r in requirements]

        return requirements


def load_installed_packages(include_distributed_packages_only=False):
    installed_packages = {module.name: module for module in pkgutil.iter_modules() if module.ispkg}
    packages_by_name = {}
    packages_by_distribution_name = {}
    package_paths = set()

    for package_name, module_info in installed_packages.items():

        loader = module_info.module_finder.find_module(module_info.name)

        if not hasattr(loader, 'path'):
            continue

        path = os.path.dirname(loader.path)

        if package_name.startswith('_'):
            continue

        package_name = package_name.replace('-', '_')

        if path in package_paths:
            continue

        package_paths.add(path)

        package = Package(package_name, path, loader.path)
        packages_by_name[package.name] = package

        dist_name = package.distribution_name

        if dist_name:
            packages_by_distribution_name[dist_name] = package

    for package in packages_by_name.values():

        for index, r in enumerate(package.requirements):
            if r not in packages_by_distribution_name:
                continue

            package.requirements[index] = packages_by_distribution_name[r].name

    packages_by_name = {package.name: package for package in packages_by_name.values()
                        if "django" in (package.requirements or [] if include_distributed_packages_only else ["django"]) and package.apps}
    return packages_by_name


def build_app_index(packages_by_name):
    result = {}

    for package in packages_by_name.values():
        for app in package.apps:
            result[app.import_path] = app

    return result


def build_dependency_graph(app_list, packages_by_name):
    nodes = {}
    traversal_list = list(app_list)
    app_index = build_app_index(packages_by_name)

    while traversal_list:
        app_name = traversal_list[0]
        traversal_list = traversal_list[1:]

        if app_name in nodes:
            continue

        required_apps = []
        nodes[app_name] = required_apps

        app = app_index.get(app_name, None)

        if app is None:
            continue

        for r in app.package.requirements:

            if r in ['wagtail', 'django']:
                continue

            package = packages_by_name.get(r, None)

            if package is None:
                continue

            for app in package.apps:
                required_apps.append(app.import_path)

                if app.import_path not in nodes:
                    traversal_list.append(app.import_path)

    return nodes


def resolve_app_dependencies(app_list):
    packages_by_name = load_installed_packages()
    nodes = build_dependency_graph(app_list, packages_by_name)

    ts = graphlib.TopologicalSorter(nodes)
    result = tuple(ts.static_order())
    return result

