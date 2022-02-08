from PySpice.Spice.Netlist import Circuit as PySpiceCircuit
from configuration import configuration

from modules.Circuit.useCases.LoadExternalLibrary import LoadExternalLibraryUseCase


class Circuit(PySpiceCircuit):
    def __init__(self, title, ground=0, *args, **kwargs):
        super().__init__(
            title=title,
            ground=ground,
            *args,
            **kwargs,
        )

        load_external_library_use_case = LoadExternalLibraryUseCase(
            circuit=self,
        )
        for library in configuration.libraries_to_include:
            load_external_library_use_case.execute(path=library)
