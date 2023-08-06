from enum import Enum

import requests

from jupyter_d1.settings import settings


class D1CommandType(str, Enum):
    NOTIFY = "notify"
    HANDLE_IMPORT_ERROR = "handle_import_error"


def execute_d1_notify(title: str, message: str):
    requests.post(
        f"{settings.MOTHERSHIP_URL}/work_nodes/{settings.WORK_NODE_ID}/push",
        json={
            "secret": settings.PUSH_NOTE_SECRET_KEY,
            "title": title,
            "message": message,
        },
        timeout=30,
    )
