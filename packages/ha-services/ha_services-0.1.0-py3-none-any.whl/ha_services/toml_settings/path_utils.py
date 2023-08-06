import logging
import shutil
from pathlib import Path

from bx_py_utils.path import assert_is_file


logger = logging.getLogger(__name__)


def backup(file_path: Path):
    assert_is_file(file_path)
    for number in range(1, 100):
        bak_file_candiate = file_path.with_suffix(f'.bak{number if number>1 else ""}')
        if not bak_file_candiate.is_file():
            logger.info('Backup %s to %s', file_path, bak_file_candiate)
            shutil.copyfile(file_path, bak_file_candiate)
            return
    raise RuntimeError('No backup made: Maximum attempts to find a file name failed.')


def clean_settings_path(settings_path: str) -> Path:
    settings_path = Path(settings_path).expanduser()
    assert settings_path.suffix == '.toml', f'File extension must be ".toml": {settings_path=}'
    return settings_path
