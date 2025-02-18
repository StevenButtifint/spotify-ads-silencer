from enum import Enum


class ProcessState(Enum):
    CLOSED = 1
    PLAYING_MUSIC = 2
    PLAYING_AD = 3