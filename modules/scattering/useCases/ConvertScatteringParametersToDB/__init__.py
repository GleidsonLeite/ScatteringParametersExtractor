from modules.scattering.entities.ScatteringParameters import ScatteringParameters
from utils.ConvertToDB import convert_signal_to_db


class ConvertScatteringParametersToDBUseCase:
    def execute(
        self,
        scattering_parameters: ScatteringParameters,
    ) -> ScatteringParameters:
        S11_in_db = convert_signal_to_db(signal=scattering_parameters.S11)
        S12_in_db = convert_signal_to_db(signal=scattering_parameters.S12)
        S21_in_db = convert_signal_to_db(signal=scattering_parameters.S21)
        S22_in_db = convert_signal_to_db(signal=scattering_parameters.S22)

        scattering_parameters_in_db = ScatteringParameters(
            frequency=scattering_parameters.frequency,
            S11=S11_in_db,
            S12=S12_in_db,
            S21=S21_in_db,
            S22=S22_in_db,
        )

        return scattering_parameters_in_db
