from modules.scattering.entities.TestSubCircuit import TestSubCircuit
from modules.scattering.useCases.ExtractScatteringParametersUseCase import (
    ExtractScatteringParametersUseCase,
)


test_sub_circuit = TestSubCircuit(name="TestCircuit")

extract_scattering_parameters_use_case = ExtractScatteringParametersUseCase(
    sub_circuit=test_sub_circuit
)

scattering_parameters = extract_scattering_parameters_use_case.execute()

print(scattering_parameters)
