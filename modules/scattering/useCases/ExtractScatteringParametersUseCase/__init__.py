from typing import Literal
from PySpice.Spice.Netlist import SubCircuit

from modules.scattering.useCases.DriveCircuitToGetSParametersUseCase import (
    DriveCircuitToGetSParametersUseCase,
)
from modules.scattering.useCases.ExtractScatteringParametersUseCase.ScatteringParameters import (
    ScatteringParamers,
)
from modules.simulator.UseCases.DestroyNGSharedInstanceUseCase import (
    DestroyNGSharedInstanceUseCase,
)
from modules.simulator.UseCases.SimulateACUseCase import SimulateACUseCase


class ExtractScatteringParametersUseCase:
    def __init__(self, sub_circuit: SubCircuit) -> None:
        self.__sub_circuit = sub_circuit

    def execute(
        self,
        input_point_name: str = "P1",
        output_point_name: str = "P2",
        circuit_title: str = "ScatteringWithInputDrived",
        input_drived_sub_circuit_name: str = "InputDrivedSubCircuit",
        output_sub_circuit_name: str = "OutputDrivedCircuit",
        simulation_start_frequency: float = 1,
        simulation_stop_frequency: float = 2.45e9,
        simulation_variation: Literal["dec", "oct", "lin"] = "dec",
        number_of_points_of_simulation: int = 1000,
    ) -> ScatteringParamers:
        scattering_parameters = ScatteringParamers()

        drive_circuit_to_get_s_parameters_use_case = (
            DriveCircuitToGetSParametersUseCase(sub_circuit=self.__sub_circuit)
        )

        for counter in range(2):

            is_in_first_loop = counter == 1

            circuit_test = drive_circuit_to_get_s_parameters_use_case.execute(
                should_drive_input_port=is_in_first_loop,
                output_point_name=output_point_name,
                input_point_name=input_point_name,
                circuit_title=circuit_title,
                output_sub_circuit_name=output_sub_circuit_name,
                input_drived_sub_circuit_name=input_drived_sub_circuit_name,
            )

            circuit_simulator = circuit_test.simulator(
                temperature=25,
                nominal_temperature=25,
            )

            simulate_ac_usecase = SimulateACUseCase(simulator=circuit_simulator)

            analysis = simulate_ac_usecase.execute(
                start_frequency=simulation_start_frequency,
                stop_frequency=simulation_stop_frequency,
                number_of_points=number_of_points_of_simulation,
                variation=simulation_variation,
            )

            input_response = analysis[input_point_name].as_ndarray()
            output_response = analysis[input_point_name].as_ndarray()

            if is_in_first_loop:
                scattering_parameters.S11 = 2 * input_response - 1
                scattering_parameters.S21 = 2 * output_response
                scattering_parameters.frequency = analysis.frequency.as_ndarray()
            else:
                scattering_parameters.S12 = 2 * input_response
                scattering_parameters.S22 = 2 * output_response - 1

            destroy_ngshared_instance_use_case = DestroyNGSharedInstanceUseCase(
                simulator=circuit_simulator
            )

            destroy_ngshared_instance_use_case.execute()

        return scattering_parameters
