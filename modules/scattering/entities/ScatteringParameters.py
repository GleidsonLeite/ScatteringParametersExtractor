from dataclasses import dataclass
import numpy as np


@dataclass
class ScatteringParameters:
    frequency: np.ndarray = None
    S11: np.ndarray = None
    S12: np.ndarray = None
    S21: np.ndarray = None
    S22: np.ndarray = None
