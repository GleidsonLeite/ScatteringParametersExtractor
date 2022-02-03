from PySpice.Spice.Netlist import SubCircuit, Circuit


class DriveCircuitPortsUseCase:
    def __init__(self, sub_circuit: SubCircuit) -> None:
        self.__sub_circuit = sub_circuit

    def execute(
        self,
        input_sub_circuit: SubCircuit,
        output_sub_circuit: SubCircuit,
        input_point_name: str = "P1",
        output_point_name: str = "P2",
        circuit_title: str = "ScatteringWithInputDrived",
    ) -> Circuit:
        circuit = Circuit(title=circuit_title)

        circuit.subcircuit(self.__sub_circuit)
        circuit.subcircuit(input_sub_circuit)
        circuit.subcircuit(output_sub_circuit)

        circuit.X(
            "inputCircuit",
            input_sub_circuit.name,
            input_point_name,
            circuit.gnd,
        )
        circuit.X(
            "analysisCircuit",
            self.__sub_circuit.name,
            input_point_name,
            output_point_name,
            circuit.gnd,
        )
        circuit.X(
            "outputCircuit",
            output_sub_circuit.name,
            output_point_name,
            circuit.gnd,
        )

        return circuit
