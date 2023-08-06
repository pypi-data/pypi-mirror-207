import re

_all__ = ['parse_dotted_path_components', 'value_at_dotted_path']

IDENTIFIER_RE = re.compile(r'^[A-Za-z_][A-Za-z_0-9]*$')


def parse_dotted_path_components(path):

    components = [component.strip() for component in path.split(".")]

    for component in components:
        if IDENTIFIER_RE.match(component) is None:
            return None

    return components


def value_at_dotted_path(scope, path, default=None):

    if isinstance(path, str):
        path = parse_dotted_path_components(path)

    if path is None:
        return default

    try:
        for index, component in enumerate(path):

            try:
                scope = scope[component]
            except TypeError:
                scope = getattr(scope, component)

    except (AttributeError, KeyError):
        return default

    return scope
