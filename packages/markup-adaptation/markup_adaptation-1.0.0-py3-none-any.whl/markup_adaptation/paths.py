from .errors import *


def split_path(path):
    return path.split(".")


def join_path_components(components):
    return ".".join(components)


def last_path_component(path):
    path = split_path(path)

    if not path:
        return ""

    return path[-1]


def get_path_value(path, scope, default_value=None, raise_on_undefined=False):

    parts = split_path(path)

    if not parts:
        raise UndefinedPath()

    for index, part in enumerate(parts[:-1]):

        try:
            scope = scope[part]
        except TypeError:
            undefined_path = join_path_components(parts[:index + 1])
            raise UndefinedVariableScope(undefined_path)
        except KeyError:
            undefined_path = join_path_components(parts[:index + 1])
            raise UndefinedVariable(undefined_path)

    variable_name = parts[-1]

    try:
        return scope[variable_name]

    except TypeError:
        raise UndefinedVariable(path)

    except KeyError:

        if raise_on_undefined:
            raise UndefinedVariable(path)

        return default_value


def set_path_value(path, path_value, scope, do_create_missing_scopes=False, do_create_variable=True):

    parts = split_path(path)

    if not parts:
        raise UndefinedPath()

    for index, part in enumerate(parts[:-1]):

        try:
            scope = scope[part]

        except TypeError:
            undefined_path = join_path_components(parts[:index + 1])
            raise UndefinedVariableScope(undefined_path)

        except KeyError:

            if not do_create_missing_scopes:
                undefined_path = join_path_components(parts[:index + 1])
                raise UndefinedVariable(undefined_path)

            value = {}
            scope[part] = value
            scope = value

    variable_name = parts[-1]

    try:
        _ = scope[variable_name]

    except TypeError:
        raise UndefinedVariable(path)

    except KeyError:

        if not do_create_variable:
            raise UndefinedVariable(path)

    scope[variable_name] = path_value

