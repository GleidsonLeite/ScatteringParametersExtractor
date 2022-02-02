from typing import List
from PySpice.Spice.Netlist import SubCircuit


class InputDrivedSubCircuit(SubCircuit):
    def __init__(
        self,
        name: str,
        signal_amplitude: float,
        resistance: float = 50,
        capacitance: float = 100,
        nodes: List[str] = ["INP", "GND"],
    ):
        super().__init__(name, *nodes)

        self.SinusoidalVoltageSource(
            "signal",
            "SOUT",
            nodes[1],
            signal_amplitude,
        )

        self.R("R0", "SOUT", "ROUT", resistance)
        self.C("C0", "ROUT", nodes[0], capacitance)
