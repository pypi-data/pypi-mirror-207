import dataclasses
import inspect
import textwrap
from collections.abc import Iterable

from bx_py_utils.anonymize import anonymize
from rich import console, print  # noqa

from ha_services.toml_settings.data_class_utils import iter_dataclass


def print_dataclasses(*, instance, anonymize_keys: Iterable, indent=0):
    print(f'{" "*indent}[magenta]{instance.__class__.__name__}[/magenta]:')

    indent += 2

    if doc_string := inspect.getdoc(instance):
        print(textwrap.indent(doc_string, prefix=' ' * indent))

    indent += 2

    for field_name, field_value in iter_dataclass(instance):
        if dataclasses.is_dataclass(field_value):
            print()
            print_dataclasses(instance=field_value, anonymize_keys=anonymize_keys, indent=indent + 4)
        else:
            if field_name in anonymize_keys:
                field_value = anonymize(field_value)
            print(f'{" "*indent}* [cyan]{field_name}[/cyan] = {field_value!r}')
