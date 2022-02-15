import numpy as np


def convert_signal_to_db(signal: np.ndarray, is_power: bool = False) -> np.ndarray:
    signal_module = np.sqrt(np.power(np.real(signal), 2) + np.power(np.imag(signal), 2))
    signal_in_db = (10 if is_power else 20) * np.log10(signal_module)
    return signal_in_db
