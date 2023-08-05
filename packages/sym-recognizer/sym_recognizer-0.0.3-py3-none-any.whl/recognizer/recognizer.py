from typing import Type
import numpy as np
from .methods.base import RecognitionMethod
from .alphabet import Alphabet, DefaultAlphabet
from .split import Splitter, NativeSplitter


class Recognizer:
    _alphabet: Alphabet = DefaultAlphabet
    _splitter: Splitter = NativeSplitter

    @classmethod
    def set_alphabet(cls, alphabet: Alphabet) -> None:
        cls.alphabet = alphabet

    @classmethod
    def set_splitter(cls, splitter: Splitter) -> None:
        cls._splitter = splitter

    @classmethod
    def recognize(cls, img: np.ndarray, method: Type[RecognitionMethod]) -> str:
        return method.recognize(img, cls._alphabet, cls._splitter)
