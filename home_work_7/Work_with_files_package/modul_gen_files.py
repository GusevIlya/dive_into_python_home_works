__all__ = ['gen_files', 'gen_files_2']

from random import choices, randint
from string import ascii_lowercase, digits
from pathlib import Path
import os


def gen_files(ext: str, min_name: int = 6, max_name: int = 30, min_size: int = 256,
              max_size: int = 4096, count_files: int = 42) -> None:
    for _ in range(count_files):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            if not Path(f'{name}.{ext}').is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)


def gen_files_2(directory: str | Path, **kwargs) -> None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)
    os.chdir(directory)
    for ext, cnt in kwargs.items():
        gen_files(ext, count_files=cnt)


if __name__ == '__main__':
    gen_files_2(r'F:\Учеба GeekBrains\Погружение в Python\Семинары\seminar_7\tests', avi=3, mov=2, jpeg=3, txt=3)
