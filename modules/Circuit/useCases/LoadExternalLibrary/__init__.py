from PySpice.Spice.Netlist import Circuit


class LoadExternalLibraryUseCase:
    def __init__(self, circuit: Circuit) -> None:
        self.__circuit = circuit

    def execute(self, path: str) -> None:
        self.__circuit.include(path)
