from enum import Enum
from typing import Union

class Pitch(Enum):
    A = 1
    Ab = 2
    As = 3
    B = 4
    Bb = 5
    C = 6
    Cs = 7
    D = 8
    Db = 9
    Ds = 10
    E = 11
    Eb = 12
    F = 13
    Fs = 14
    G = 15
    Gb = 16
    Gs = 17

class Note:
    def __init__(self, pitch: Pitch, length: NoteLength):
        self.pitch = pitch
        self.length = length

    def relative_sharp(self) -> Union[Pitch, None]:
        """Returns the relative sharp of a pitch, provided that the note is flatted.

        Returns:
            Union[Pitch, None]: pitch value corresponding to the flat pitch, or none if the note is sharp or natural.
        """
        match self.pitch:
            case Pitch.Ab:
                return Pitch.Gs
            case Pitch.Bb:
                return Pitch.As
            case Pitch.Db:
                return Pitch.Cs
            case Pitch.Eb:
                return Pitch.Ds
            case Pitch.Gb:
                return Pitch.Fs
            case _:
                return None
                
    def relative_flat(self) -> Union[Pitch, None]:
        """Return the relative flat of a pitch, provided that the note is sharpened.
        
        Returns:
            Union[Pitch, None]: pitch value corresponding to the sharp pitch, or none if the note is flat or natural.
        """
        match self.pitch:
            case Pitch.As:
                return Pitch.Bb
            case Pitch.Cs:
                return Pitch.Cb
            case 