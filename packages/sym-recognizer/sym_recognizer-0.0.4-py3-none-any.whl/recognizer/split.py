from abc import ABC, abstractmethod
from .symbol import Symbol
import numpy as np
import cv2 as cv


class Splitter(ABC):
    @staticmethod
    @abstractmethod
    def split_into_symbols(img: np.ndarray) -> list[Symbol]:
        raise NotImplementedError


class NativeSplitter(Splitter):
    @staticmethod
    def split_into_symbols(
        img: np.ndarray, kernel_size: tuple[int] = (5, 5)
    ) -> list[Symbol]:
        ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

        kernel = cv.getStructuringElement(cv.MORPH_RECT, kernel_size)
        thresh = cv.morphologyEx(th2, cv.MORPH_CLOSE, kernel)
        contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        symbols = []
        for idx, contour in enumerate(contours):
            x, y, w, h = cv.boundingRect(contour)
            img_c = thresh[y : y + h, x : x + w].copy()
            mn = img_c.mean()
            fmin = img_c < mn
            fmax = img_c >= mn
            img_c[fmin] = 0
            img_c[fmax] = 255
            ic = Symbol()
            ic.vector = img_c
            ic.pos_mapper = x**2 + y**2
            symbols.append(ic)
        symbols.sort(key=lambda x: x.pos_mapper)
        return symbols

    @staticmethod
    def _make_border(img: np.ndarray, chunk_size: int, color: list = [0, 0, 0]):
        b_size = chunk_size // 2 + 1
        constant = cv.copyMakeBorder(
            img, b_size, b_size, b_size, b_size, cv.BORDER_CONSTANT, value=color
        )
        return constant

    @staticmethod
    def normalize(v):
        norm = np.linalg.norm(v)
        if norm == 0:
            return v
        return v / norm
