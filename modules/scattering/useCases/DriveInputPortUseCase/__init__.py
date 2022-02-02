from PySpice.Spice.Netlist import SubCircuit, Circuit

from modules.scattering.entities.InputDrivedSubCircuit import InputDrivedSubCircuit
from modules.scattering.entities.OutputSubCircuit import OutputCircuit


class DriveInputPortUseCase:
    def __init__(self, sub_circuit: SubCircuit) -> None:
        self.__sub_circuit = sub_circuit

    def execute(self) -> Circuit:
        circuit = Circuit(title="ScatteringWithInputDrived")

        circuit.subcircuit(self.__sub_circuit)

        input_drived_subcircuit_name = "InputDrivedSubCircuit"
        input_drived_subcircuit = InputDrivedSubCircuit(
            name=input_drived_subcircuit_name,
            signal_amplitude=2,
        )
        circuit.subcircuit(input_drived_subcircuit)

        output_subcircuit_name = "OutputDrivedCircuit"
        output_subcircuit = OutputCircuit(name=output_subcircuit_name)
        circuit.subcircuit(output_subcircuit)

        circuit.X("inputDrived", input_drived_subcircuit_name, "P1", circuit.gnd)
        circuit.X("C", self.__sub_circuit.name, "P1", "P2", circuit.gnd)
        circuit.X("Output", output_subcircuit_name, "P2", circuit.gnd)

        return circuit
