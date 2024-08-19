__all__ = ['json_to_pickle']

from pathlib import Path
import pickle
import json


def json_to_pickle(path: Path) -> None:
    for obj in path.iterdir():
        if obj.is_file() and obj.suffix == '.json':
            with (
                open(obj, 'r', encoding='utf-8') as f_read,
                open(f'{obj.stem}.pickle', 'wb') as f_write
            ):
                data = json.load(f_read)
                pickle.dump(data, f_write)


if __name__ == '__main__':
    json_to_pickle(Path(r'F:\Учеба GeekBrains\Погружение в Python\Семинары\seminar_8'))
