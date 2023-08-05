from abc import ABC
import glob
from .data import Symbol, get_alphabet
from .split import NativeSplitter
import cv2 as cv
import matplotlib.pyplot as plt


class Alphabet(ABC):
    symbols: list[Symbol]


class DefaultAlphabet(Alphabet):
    symbols = get_alphabet()


class CustomAlphabet(Alphabet):
    symbols = None

    @classmethod
    def from_repository(cls, path):
        for img_name in glob.glob(f"{path}/*.png"):
            s = Symbol()
            s.vector = NativeSplitter.split_into_symbols(
                cv.imread(img_name, cv.IMREAD_GRAYSCALE)
            )[0].vector
            s.sym_mapper = img_name.split("/")[-1].replace(".png", "").replace("_", "")
            cls.symbols.append(s)
        return cls
