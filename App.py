from matplotlib import pyplot as plt
from modules.Circuit.entities.LNASubCircuit import LNASubCircuit

from modules.scattering.useCases.ExtractScatteringParametersUseCase import (
    ExtractScatteringParametersUseCase,
)


test_sub_circuit = LNASubCircuit(name="TestCircuit")

extract_scattering_parameters_use_case = ExtractScatteringParametersUseCase(
    sub_circuit=test_sub_circuit,
)

scattering_parameters = extract_scattering_parameters_use_case.execute(
    simulation_start_frequency=2e9,
    simulation_stop_frequency=3e9,
    number_of_points_of_simulation=1000,
)

print(scattering_parameters)
