from re import sub
from modules.scattering.entities.TestSubCircuit import TestSubCircuit
from modules.scattering.useCases.DriveCircuitToGetSParametersUseCase import (
    DriveCircuitToGetSParametersUseCase,
)
from modules.simulator.UseCases.SimulateACUseCase import SimulateACUseCase


test_sub_circuit = TestSubCircuit(name="TestCircuit")

drive_circuit_to_get_s_parameters_use_case = DriveCircuitToGetSParametersUseCase(
    sub_circuit=test_sub_circuit,
)


circuit_test = drive_circuit_to_get_s_parameters_use_case.execute(
    should_drive_input_port=True
)


circuit_simulator = circuit_test.simulator(
    temperature=25,
    nominal_temperature=25,
)
simulate_ac_usecase = SimulateACUseCase(simulator=circuit_simulator)

analysis = simulate_ac_usecase.execute(
    start_frequency=20e9,
    stop_frequency=30e9,
    number_of_points=10,
    variation="dec",
)

print(analysis["P2"].as_ndarray())
