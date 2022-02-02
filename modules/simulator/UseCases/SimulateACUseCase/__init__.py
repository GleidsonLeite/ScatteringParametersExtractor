from typing import Literal
from PySpice.Spice.NgSpice.Simulation import NgSpiceSharedCircuitSimulator

from PySpice.Probe.WaveForm import AcAnalysis


class SimulateACUseCase:
    def __init__(self, simulator: NgSpiceSharedCircuitSimulator) -> None:
        self.__simulator = simulator

    def execute(
        self,
        start_frequency: float,
        stop_frequency: float,
        number_of_points: int,
        variation: Literal["dec", "oct", "lin"],
    ) -> AcAnalysis:
        analysis: AcAnalysis = self.__simulator.ac(
            start_frequency=start_frequency,
            stop_frequency=stop_frequency,
            number_of_points=number_of_points,
            variation=variation,
        )

        return analysis
