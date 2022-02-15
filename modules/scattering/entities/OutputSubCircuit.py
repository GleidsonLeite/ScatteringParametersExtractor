from typing import List
from PySpice.Spice.Netlist import SubCircuit


class OutputCircuit(SubCircuit):
    def __init__(
        self,
        name: str,
        resistance: float = 50,
        nodes: List[str] = ["OUT", "GND"],
    ) -> None:
        super().__init__(name, *nodes)

        output_port, gnd = nodes

        self.R("R0", output_port, gnd, resistance)
