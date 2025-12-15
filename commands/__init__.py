import importlib
import pkgutil


def register_all(subparsers):
    """
    Automatically discover and register all command modules
    in this package.
    """
    package_name = __name__

    for module_info in pkgutil.iter_modules(__path__):
        module_name = module_info.name

        # Skip private / helper modules
        if module_name.startswith("_"):
            continue

        module = importlib.import_module(
            f"{package_name}.{module_name}"
        )

        if hasattr(module, "register"):
            module.register(subparsers)
