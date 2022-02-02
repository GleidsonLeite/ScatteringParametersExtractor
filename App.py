from circuit import circuit
from modules.simulator.UseCases.DestroyNGSharedInstanceUseCase import (
    DestroyNGSharedInstanceUseCase,
)
from modules.simulator.UseCases.SimulateACUseCase import SimulateACUseCase


circuit_simulator = circuit.simulator(temperature=25, nominal_temperature=25)


simulate_ac_usecase = SimulateACUseCase(simulator=circuit_simulator)

analysis = simulate_ac_usecase.execute(
    start_frequency=100,
    stop_frequency=10e3,
    number_of_points=100,
    variation="dec",
)

for out in ("out5", "out1", "out2", "out4"):
    print(analysis[out].as_ndarray())

destroy_ngspice_shared_instance_use_case = DestroyNGSharedInstanceUseCase(
    simulator=circuit_simulator,
)

destroy_ngspice_shared_instance_use_case.execute()
