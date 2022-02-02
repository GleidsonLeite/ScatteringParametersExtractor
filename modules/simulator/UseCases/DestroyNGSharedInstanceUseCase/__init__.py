from PySpice.Spice.NgSpice.Simulation import NgSpiceSharedCircuitSimulator
from PySpice.Spice.NgSpice.Shared import NgSpiceShared


class DestroyNGSharedInstanceUseCase:
    def __init__(self, simulator: NgSpiceSharedCircuitSimulator) -> None:
        self.__simulator = simulator

    def execute(self) -> None:
        ngspice_instance: NgSpiceShared = self.__simulator.ngspice
        ngspice_instance.remove_circuit()
        ngspice_instance.destroy()
