import json
import os
import tempfile
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / 'data' / 'enrollments.json'


def _identifier(value):

    if value is None or isinstance(value, bool) or not isinstance(value, (str, int)):
        raise ValueError('A valid class ID and member ID are required.')
    result = str(value).strip()
    if not result:
        raise ValueError('IDs cannot be blank.')
    return result


def _read(path):
    if not path.exists():
        return []
    with path.open('r', encoding='utf-8') as file:
        records = json.load(file)
    if not isinstance(records, list):
        raise ValueError('Enrollment data must be a list.')
    for record in records:
        if (not isinstance(record, dict)
                or not isinstance(record.get('class_id'), str)
                or not isinstance(record.get('member_id'), str)
                or type(record.get('active')) is not bool):
            raise ValueError('An enrollment record is invalid.')
    return records


def _write(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)

    temporary = None
    try:
        with tempfile.NamedTemporaryFile('w', encoding='utf-8',
                                         dir=path.parent, delete=False) as file:
            temporary = Path(file.name)
            json.dump(records, file, ensure_ascii=False, indent=2)
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def set_enrollment(member_id, class_id, active=True, *, path=DATA_FILE):

    if type(active) is not bool:
        raise ValueError('Active must be True or False.')
    member_id, class_id = _identifier(member_id), _identifier(class_id)
    path = Path(path)
    records = _read(path)
    for record in records:
        if record['member_id'] == member_id and record['class_id'] == class_id:
            record['active'] = active
            break
    else:
        records.append({'member_id': member_id, 'class_id': class_id, 'active': active})
    _write(path, records)


def is_enrolled(member_id, class_id, *, path=DATA_FILE):

    member_id, class_id = _identifier(member_id), _identifier(class_id)
    return any(
        item['member_id'] == member_id and item['class_id'] == class_id and item['active']
        for item in _read(Path(path))
    )


def active_member_ids(class_id, *, path=DATA_FILE):

    class_id = _identifier(class_id)
    return [item['member_id'] for item in _read(Path(path))
            if item['class_id'] == class_id and item['active']]


def active_class_ids(member_id, *, path=DATA_FILE):

    member_id = _identifier(member_id)
    return [item['class_id'] for item in _read(Path(path))
            if item['member_id'] == member_id and item['active']]
