from enum import Enum


class RegEx(Enum):
    BRAND = (
        r'^[A-Z][a-zA-Z\d]{1,20}$',
        'First letter uppercase min 2 max 20 ch'
    )

    LABEL = (
        r'^[A-Z][a-zA-Z\D ]{1,20}$',
        'First letter uppercase min 2 max 20 chars, only letters'
    )

    def __init__(self, pattern, msg):
        self.pattern = pattern
        self.msg = msg
