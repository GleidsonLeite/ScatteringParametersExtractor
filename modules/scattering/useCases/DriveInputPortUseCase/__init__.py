from PySpice.Spice.Netlist import SubCircuitFactory


class DriveInputPortUseCase:
    def __init__(self, sub_circuit: SubCircuitFactory) -> None:
        self.__sub_circuit = sub_circuit

    def execute(self) -> None:
        pass
