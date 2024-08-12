__all__ = ['sort_files']

from pathlib import Path
import os


def sort_files(path: str | Path, groups: dict[str: list[str]] = None) -> None:
    os.chdir(path)
    if groups is None:
        groups = {
            Path('video'): ['avi', 'mkv', 'mk4', 'mov'],
            Path('images'): ['bmp', 'jpeg', 'jpg', 'png']
        }
    reversed_groups = {}
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for ext in ext_list:
            reversed_groups[f'.{ext}'] = target_dir
    for file in path.iterdir():
        if file.is_file() and file.suffix in reversed_groups:
            file.replace(reversed_groups[file.suffix] / file.name)


if __name__ == '__main__':
    sort_files(Path('tests'))
