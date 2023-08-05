import dataclasses
import logging
from collections.abc import Iterable

import tomlkit
from rich import print  # noqa
from rich.console import Console
from tomlkit import TOMLDocument

from ha_services.toml_settings.debug import print_dataclasses
from ha_services.toml_settings.deserialize import toml2dataclass
from ha_services.toml_settings.exceptions import UserSettingsNotFound
from ha_services.toml_settings.path_utils import backup, clean_settings_path
from ha_services.toml_settings.sensible_editor import open_editor_for
from ha_services.toml_settings.serialize import dataclass2toml


logger = logging.getLogger(__name__)


def edit_user_settings(*, user_settings: dataclasses, settings_path: str) -> None:
    settings_path = clean_settings_path(settings_path)
    if not settings_path.is_file():
        logger.info('Settings file "%s" not exist -> create default', settings_path)
        document: TOMLDocument = dataclass2toml(instance=user_settings)
        doc_str = tomlkit.dumps(document, sort_keys=False)
        settings_path.write_text(doc_str, encoding='UTF-8')

    open_editor_for(settings_path)


def get_user_settings(*, user_settings: dataclasses, settings_path: str, debug: bool = False) -> dataclasses:
    settings_path = clean_settings_path(settings_path)
    if debug:
        print(f'Use user settings file: {settings_path}')
    if not settings_path.is_file():
        raise UserSettingsNotFound(settings_path)

    doc_str = settings_path.read_text(encoding='UTF-8')
    user_settings_doc: TOMLDocument = tomlkit.loads(doc_str)

    document_changed = toml2dataclass(document=user_settings_doc, instance=user_settings)
    logger.debug(f'{document_changed=}')
    if document_changed:
        logger.info('User toml file needs update!')
        doc_str = tomlkit.dumps(user_settings_doc, sort_keys=False)
        backup(settings_path)
        settings_path.write_text(doc_str, encoding='UTF-8')

    return user_settings


def debug_print_user_settings(
    *, user_settings: dataclasses, settings_path: str, anonymize_keys: Iterable = ('password', 'email')
) -> None:
    user_settings = get_user_settings(user_settings=user_settings, settings_path=settings_path, debug=True)

    print()
    console = Console()
    console.rule('user settings')
    print_dataclasses(instance=user_settings, anonymize_keys=anonymize_keys)
    console.rule()
