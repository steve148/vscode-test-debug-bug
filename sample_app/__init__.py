from datetime import datetime

from dateutil import tz


def now_local() -> datetime:
    datetime.now()
    d = datetime.now(tz.tzlocal())
    return d
