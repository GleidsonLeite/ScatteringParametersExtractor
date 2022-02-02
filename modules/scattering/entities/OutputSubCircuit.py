from typing import List
from PySpice.Spice.Netlist import SubCircuit


class OutputCircuit(SubCircuit):
    def __init__(
        self,
        name: str,
        resistance: float = 50,
        capacitance: float = 100,
        nodes: List[str] = ["OUT", "GND"],
    ) -> None:
        super().__init__(name, *nodes)

        self.C("C0", nodes[0], "P0", capacitance)
        self.R("R0", "P0", nodes[1], resistance)
