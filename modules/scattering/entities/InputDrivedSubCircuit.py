from typing import List
from PySpice.Spice.Netlist import SubCircuit


class InputDrivedSubCircuit(SubCircuit):
    def __init__(
        self,
        name: str,
        signal_amplitude: float,
        dc_offset: float = 0,
        signal_frequency: float = 1e3,
        signal_magnitude: float = 1,
        resistance: float = 50,
        nodes: List[str] = ["INP", "GND"],
    ):
        super().__init__(name, *nodes)

        input_port, gnd = nodes

        self.SinusoidalVoltageSource(
            "signal",
            "SOUT",
            gnd,
            dc_offset,
            signal_magnitude,
            0,
            signal_amplitude,
            signal_frequency,
        )

        self.R("R0", "SOUT", input_port, resistance)
