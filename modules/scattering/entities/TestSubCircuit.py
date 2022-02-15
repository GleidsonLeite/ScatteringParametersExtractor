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

        input_port, output_port, gnd = nodes

        self.C("C0", input_port, gnd, 318.3e-9)
        self.L("L0", input_port, output_port, 1.592e-3)
        self.C("C1", output_port, gnd, 318.3e-9)


# Reference: https://electronics.stackexchange.com/questions/528557/deriving-the-s-parameters-different-matched-loads-possible
