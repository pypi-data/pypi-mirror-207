from abc import ABC, abstractmethod
import numpy as np
from recognizer.alphabet import Alphabet
from recognizer.split import Splitter


class RecognitionMethod(ABC):
    @staticmethod
    @abstractmethod
    def recognize(img: np.ndarray, alphabet: Alphabet, splitter: Splitter) -> str:
        raise NotImplementedError
