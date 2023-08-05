import dataclasses
import inspect

import tomlkit
from tomlkit import TOMLDocument

from ha_services.toml_settings.data_class_utils import iter_dataclass


def add_docstring(document: TOMLDocument, instance):
    if doc_string := inspect.getdoc(instance):
        for line in doc_string.strip().splitlines():
            document.add(tomlkit.comment(line))


def add_dataclass(document: TOMLDocument, name, instance: dataclasses):
    assert dataclasses.is_dataclass(instance), f'No dataclass: {instance!r}'

    document.add(tomlkit.nl())  # Add new line

    table = tomlkit.table()
    add_docstring(table, instance)

    for field_name, field_value in iter_dataclass(instance):
        if dataclasses.is_dataclass(field_value):
            raise TypeError(f'Field {field_name} of dataclass {name} is a dataclass! Only two levels are allowed!')
        table.add(field_name, field_value)

    document.add(name, table)


def dataclass2toml(instance: dataclasses) -> TOMLDocument:
    """
    Serialize a dataclass to a tomlkit document.
    """
    assert dataclasses.is_dataclass(instance), f'No dataclass: {instance!r}'

    document = tomlkit.document()
    add_docstring(document, instance)

    for field_name, field_value in iter_dataclass(instance):
        if dataclasses.is_dataclass(field_value):
            add_dataclass(document, field_name, field_value)
        else:
            document.add(field_name, field_value)

    return document
