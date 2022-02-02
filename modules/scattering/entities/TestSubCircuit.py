from pickle import NONE
from typing import List
from PySpice.Spice.Netlist import SubCircuit


class TestSubCircuit(SubCircuit):
    def __init__(
        self,
        name: str,
        nodes: List[str] = ["PORT1", "PORT2", "GND"],
    ) -> None:
        super().__init__(name, *nodes)

        self.R("R0", nodes[0], "P1", 15)
        self.R("R1", "P1", nodes[2], 500)
        self.R("R2", "P1", nodes[1], 36)
        self.C("C0", nodes[1], nodes[2], 50e-15)
        self.R("R3", nodes[1], nodes[2], 200)
        self.L("L0", nodes[1], nodes[2], 645e-12)


# Reference: https://electronics.stackexchange.com/questions/528557/deriving-the-s-parameters-different-matched-loads-possible
