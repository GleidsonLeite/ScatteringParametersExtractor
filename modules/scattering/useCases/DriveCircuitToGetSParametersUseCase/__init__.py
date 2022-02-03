from PySpice.Spice.Netlist import SubCircuit, Circuit
from modules.scattering.entities.InputDrivedSubCircuit import InputDrivedSubCircuit
from modules.scattering.entities.OutputSubCircuit import OutputCircuit
from modules.scattering.useCases.DriveCircuitPortsUseCase import (
    DriveCircuitPortsUseCase,
)


class DriveCircuitToGetSParametersUseCase(DriveCircuitPortsUseCase):
    def __init__(self, sub_circuit: SubCircuit) -> None:
        super().__init__(sub_circuit)

    def execute(
        self,
        should_drive_input_port: bool = True,
        input_point_name: str = "P1",
        output_point_name: str = "P2",
        circuit_title: str = "ScatteringWithInputDrived",
        input_drived_sub_circuit_name: str = "InputDrivedSubCircuit",
        output_sub_circuit_name: str = "OutputDrivedCircuit",
    ) -> Circuit:

        input_drived_sub_circuit = None
        output_sub_circuit = None

        if should_drive_input_port:
            input_drived_sub_circuit = InputDrivedSubCircuit(
                name=input_drived_sub_circuit_name,
                signal_amplitude=2,
            )

            output_sub_circuit = OutputCircuit(
                name=output_sub_circuit_name,
            )
        else:
            input_drived_sub_circuit = OutputCircuit(
                name=output_sub_circuit_name,
            )

            output_sub_circuit = InputDrivedSubCircuit(
                name=input_drived_sub_circuit_name,
                signal_amplitude=2,
            )

        circuit = super().execute(
            input_sub_circuit=input_drived_sub_circuit,
            output_sub_circuit=output_sub_circuit,
            input_point_name=input_point_name,
            output_point_name=output_point_name,
            circuit_title=circuit_title,
        )

        return circuit
