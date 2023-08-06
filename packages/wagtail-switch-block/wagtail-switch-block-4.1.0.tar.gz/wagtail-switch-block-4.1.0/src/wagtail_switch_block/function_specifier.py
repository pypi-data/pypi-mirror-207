import importlib
import builtins

__all__ = ['FunctionSpecifier']


class FunctionSpecifier(object):

    @property
    def function(self):

        if self._function is None:
            if self._function_module:
                module = importlib.import_module(self._function_module)
            else:
                module = builtins

            self._function = getattr(module, self._function_name, lambda: list())

        return self._function

    @property
    def function_path(self):
        return self._function_path

    def __init__(self, *, function_path):
        super().__init__()
        self._function_path = function_path

        parts = self._function_path.rsplit('.', maxsplit=1)

        if len(parts) == 2:
            self._function_module = parts[0]
            self._function_name = parts[1]
        else:
            self._function_module = None
            self._function_name = parts[0]

        self._function = None

    def save_init_arguments(self, arguments):
        arguments.function_path = self._function_path

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs) # noqa
