import numpy as np
import cv2 as cv
from .base import RecognitionMethod
from recognizer.alphabet import Alphabet
from recognizer.split import Splitter


class Correlation(RecognitionMethod):
    @staticmethod
    def recognize(img: np.ndarray, alphabet: Alphabet, splitter: Splitter) -> str:
        splitted = splitter.split_into_symbols(img)
        for sym in splitted:
            max_val = 0
            for et in alphabet.symbols:
                cur_val = np.linalg.norm(
                    Correlation.check_correlation(sym.vector, et.vector)
                )
                if cur_val > max_val:
                    max_val = cur_val
                    sym.sym_mapper = et.sym_mapper
        return "".join(sym.sym_mapper for sym in splitted)

    @staticmethod
    def check_correlation(img: np.ndarray, eth: np.ndarray) -> float:
        if img.shape != eth.shape:
            img = cv.resize(img, (eth.shape[1], eth.shape[0]))
        img = img / np.linalg.norm(img)
        eth = eth / np.linalg.norm(eth)
        if np.linalg.norm(img) * np.linalg.norm(eth) != 0:
            return (
                np.dot(img.flatten(), eth.flatten())
                / np.linalg.norm(img)
                * np.linalg.norm(eth)
            )
        return 0
