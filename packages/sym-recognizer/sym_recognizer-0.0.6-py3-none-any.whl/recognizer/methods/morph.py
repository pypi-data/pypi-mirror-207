import numpy as np
from .base import RecognitionMethod
from recognizer.alphabet import Alphabet
from recognizer.split import Splitter
from recognizer.data import Symbol
import cv2 as cv


class Morphology(RecognitionMethod):
    @staticmethod
    def recognize(img: np.ndarray, alphabet: Alphabet, splitter: Splitter) -> str:
        splitted: list[Symbol] = splitter.split_into_symbols(img)
        for sym in splitted:
            min_dist = np.inf
            for eth in alphabet.symbols:
                cur_dist = Morphology.dist(sym.vector, eth.vector)
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    sym.sym_mapper = eth.sym_mapper
        return "".join(sym.sym_mapper for sym in splitted)

    @staticmethod
    def project(img: np.ndarray, eth: np.ndarray) -> np.ndarray:
        tb = eth.copy()
        for field in set(img.flatten()):
            tmp_mb = np.ma.masked_where(img == field, tb)
            tb[~tmp_mb.mask] = tmp_mb.mean()
        return tb

    @staticmethod
    def dist(img: np.ndarray, eth: np.ndarray):
        if img.shape != eth.shape:
            img = cv.resize(img, (eth.shape[1], eth.shape[0]))
        img = img / np.linalg.norm(img)
        eth = eth / np.linalg.norm(eth)
        c = np.ones_like(img)
        if np.linalg.norm(img - c) != 0:
            return np.linalg.norm(img - Morphology.project(eth, img)) / np.linalg.norm(
                img - c
            )
        return 1
