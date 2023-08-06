from multiprocessing import Process, Queue
import importlib


def load_config_module(import_path):
    try:
        result = importlib.import_module(import_path)
    except Exception:  # noqa
        return None

    return result


def determine_django_app_labels(q):
    while True:
        import_path = q.get()

        module = load_config_module(import_path)

        if not module:
            q.put(None)
            continue

        configs = [getattr(module, entry) for entry in dir(module) if entry.endswith('Config') and entry != 'AppConfig']
        configs = [entry for entry in configs if isinstance(entry, type) and entry.__module__ == import_path]

        if not configs:
            q.put(None)
            continue

        config = configs[0]

        if hasattr(config, 'label'):
            label = config.label
        else:

            if not hasattr(config, 'name'):
                q.put(None)
                continue

            label = config.name.rpartition(".")[2]

        print("Sandbox putting label: " + label + "\n")

        q.put(label)


__queue = None
__process = None


def initialise_support():
    global __queue
    global __process

    __queue = Queue()
    __process = Process(target=determine_django_app_labels, args=(__queue,))
    __process.start()


def determine_django_app_label(import_path):
    if __process is None:
        initialise_support()

    __queue.put(import_path) # noqa
    django_app_label = __queue.get() # noqa
    return django_app_label

