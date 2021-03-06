from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Configuration:
    libraries_to_include: List[str]
    nfet_type: str = "sky130_fd_pr__nfet_01v8"
    pfet_type: str = "sky130_fd_pr__pfet_01v8"


configuration = Configuration(
    libraries_to_include=[
        "/skywater-pdk/libraries/sky130_fd_pr/latest/models/corners/tt.spice"
    ]
)
