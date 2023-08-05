from typing import Dict, List, Union

from ._core import mongodb

assisdb = mongodb.start


async def get_start_names(chat_id: int) -> List[str]:
    _notes = []
    for note in await _get_start(chat_id):
        _notes.append(note)
    return _notes


async def _get_start(chat_id: int) -> Dict[str, int]:
    _notes = await assisdb.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_start(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _notes = await _get_start(chat_id)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_start(chat_id: int, name: str, note: dict):
    name = name.lower().strip()
    _notes = await _get_start(chat_id)
    _notes[name] = note
    await assisdb.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )
