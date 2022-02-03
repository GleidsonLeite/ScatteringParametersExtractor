from matplotlib import pyplot as plt

from modules.scattering.entities.TestSubCircuit import TestSubCircuit
from modules.scattering.useCases.ExtractScatteringParametersUseCase import (
    ExtractScatteringParametersUseCase,
)
from utils.ConvertToDB import convert_signal_to_db


test_sub_circuit = TestSubCircuit(name="TestCircuit")

extract_scattering_parameters_use_case = ExtractScatteringParametersUseCase(
    sub_circuit=test_sub_circuit,
)

scattering_parameters = extract_scattering_parameters_use_case.execute(
    simulation_start_frequency=1,
    simulation_stop_frequency=3e9,
    number_of_points_of_simulation=100,
)

S11_in_db = convert_signal_to_db(signal=scattering_parameters.S11)
plt.plot(scattering_parameters.frequency, S11_in_db)
plt.title("Scalar Logarithmic Gain")
plt.grid()
plt.xlabel("frequency [Hz]")
plt.ylabel("Gain [dB]")
plt.xscale(value="log")
plt.show()
