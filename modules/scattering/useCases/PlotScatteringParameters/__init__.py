from typing import Literal
from matplotlib import pyplot as plt
from modules.scattering.entities.ScatteringParameters import ScatteringParameters
from modules.scattering.useCases.ConvertScatteringParametersToDB import (
    ConvertScatteringParametersToDBUseCase,
)


class PlotScatteringParametersUseCase:
    @staticmethod
    def execute(
        scattering_parameters: ScatteringParameters,
        legend_location: Literal[
            "best",
            "upper right",
            "upper left",
            "lower left",
            "lower right",
            "right",
            "center left",
            "center right",
            "lower center",
            "upper center",
            "center",
        ] = "best",
    ) -> None:

        convert_scattering_parameters_to_db_usecase = (
            ConvertScatteringParametersToDBUseCase()
        )

        scattering_parameters_in_db = (
            convert_scattering_parameters_to_db_usecase.execute(
                scattering_parameters=scattering_parameters,
            )
        )

        plt.subplot(2, 2, 1)
        plt.plot(
            scattering_parameters_in_db.frequency,
            scattering_parameters_in_db.S11,
            label="S11 Parameter",
        )
        plt.xscale("log")
        plt.legend(loc=legend_location)
        plt.grid(True, which="both", ls="-")

        plt.subplot(2, 2, 2)
        plt.plot(
            scattering_parameters_in_db.frequency,
            scattering_parameters_in_db.S12,
            label="S12 Parameter",
        )
        plt.xscale("log")
        plt.legend(loc=legend_location)
        plt.grid(True, which="both", ls="-")

        plt.subplot(2, 2, 3)
        plt.plot(
            scattering_parameters_in_db.frequency,
            scattering_parameters_in_db.S21,
            label="S21 Parameter",
        )
        plt.xscale("log")
        plt.legend(loc=legend_location)
        plt.grid(True, which="both", ls="-")

        plt.subplot(2, 2, 4)
        plt.plot(
            scattering_parameters_in_db.frequency,
            scattering_parameters_in_db.S22,
            label="S22 Parameter",
        )
        plt.xscale("log")
        plt.legend(loc=legend_location)
        plt.grid(True, which="both", ls="-")

        plt.show()
