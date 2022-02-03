import numpy as np


def convert_signal_to_db(signal: np.ndarray, is_power: bool = False) -> np.ndarray:
    signal_in_db = (10 if is_power else 20) * np.log10(np.absolute(signal))
    return signal_in_db
