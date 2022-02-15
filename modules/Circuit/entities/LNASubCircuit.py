from typing import List
from PySpice.Spice.Netlist import SubCircuit


class LNASubCircuit(SubCircuit):
    def __init__(
        self,
        name: str,
        nfet_type: str = "sky130_fd_pr__nfet_01v8",
        pfet_type: str = "sky130_fd_pr__pfet_01v8",
        nodes: List[str] = ["INP", "OUT", "GND"],
    ) -> None:
        super().__init__(name, *nodes)

        self.L("LG", "INP", "PLG", 5.8e-9)
        self.R("RPOL1", "PLG", "VPOL1", 19939)
        self.V("VPOL1", "VPOL1", "GND", 0.9)

        self.X(
            "M1",
            nfet_type,
            "PRF",
            "PLG",
            "GND",
            "GND",
            L=2.2,
            W=68.3,
            ad="'W*0.29'",
            pd="'2*(W+0.29)'",
            as_="'W*0.29'",
            ps="'2*(W+0.29)'",
            nrd="'0.29/W'",
            nrs="'0.29/W'",
            sa=0,
            sb=0,
            sd=0,
            nf=1,
            mult=1,
        )

        self.C("C1", "PC1", "PLG", 19.7e-12)
        self.R("RF", "PC1", "PRF", 19540)

        self.X(
            "M2",
            pfet_type,
            "VCC",
            "PC1",
            "PRF",
            "GND",
            L=39.9,
            W=1.1,
            ad="'W*0.29'",
            pd="'2*(W+0.29)'",
            as_="'W*0.29'",
            ps="'2*(W+0.29)'",
            nrd="'0.29/W'",
            nrs="'0.29/W'",
            sa=0,
            sb=0,
            sd=0,
            nf=1,
            mult=1,
        )
        self.C("CDEC", "VCC", "GND", 1e-6)
        self.C("CM1", "PRF", "PCM1", 4.7e-12)
        self.R("RPOL2", "PCM1", "VPOL2", 13548)

        self.X(
            "M3",
            nfet_type,
            "PM3",
            "PCM1",
            "GND",
            "GND",
            L=48,
            W=6.5,
            ad="'W*0.29'",
            pd="'2*(W+0.29)'",
            as_="'W*0.29'",
            ps="'2*(W+0.29)'",
            nrd="'0.29/W'",
            nrs="'0.29/W'",
            sa=0,
            sb=0,
            sd=0,
            nf=1,
            mult=1,
        )
        self.L("LPK", "VDD", "PM3", 7.6e-9)
        self.C("CM2", "PM3", "OUT", 0.65e-12)
        self.C("CM3", "OUT", "GND", 4.7e-12)

        self.V("VCC", "VCC", "GND", 1.8)
        self.V("VDD", "VDD", "GND", 1.8)
        self.V("VPOL2", "VPOL2", "GND", 0.53)

    @property
    def w1(self) -> float:
        return self.XM1.parameters["W"]

    @w1.setter
    def w1(self, width: float) -> None:
        self.XM1.parameters["W"] = width if 0.15 <= width < 100 else self.w1

    @property
    def l1(self) -> float:
        return self.XM1.parameters["L"]

    @l1.setter
    def l1(self, length: float) -> None:
        self.XM1.parameters["L"] = length if 0.15 <= length < 100 else self.l1

    @property
    def w2(self) -> float:
        return self.XM2.parameters["W"]

    @w2.setter
    def w2(self, width: float) -> None:
        self.XM2.parameters["W"] = width if 0.15 <= width < 100 else self.w2

    @property
    def l2(self) -> float:
        return self.XM2.parameters["L"]

    @l2.setter
    def l2(self, length: float) -> None:
        self.XM2.parameters["L"] = length if 0.15 <= length < 100 else self.l2

    @property
    def w3(self) -> float:
        return self.XM3.parameters["W"]

    @w3.setter
    def w3(self, width: float) -> None:
        self.XM3.parameters["W"] = width if 0.15 <= width < 100 else self.w3

    @property
    def l3(self) -> float:
        return self.XM3.parameters["L"]

    @l3.setter
    def l3(self, length: float) -> None:
        self.XM3.parameters["L"] = length if 0.15 <= length < 100 else self.l3

    @property
    def Rf(self) -> float:
        return self.RRF.resistance

    @Rf.setter
    def Rf(self, resistance: float) -> None:
        self.RRF.resistance = max(1, resistance)

    @property
    def Rpol1(self) -> float:
        return self.RRPOL1.resistance

    @Rpol1.setter
    def Rpol1(self, resistance: float) -> None:
        self.RRPOL1.resistance = max(1, resistance)

    @property
    def Rpol2(self) -> float:
        return self.RRPOL2.resistance

    @Rpol2.setter
    def Rpol2(self, resistance: float) -> None:
        self.RRPOL2.resistance = max(1, resistance)

    @property
    def Lg(self) -> float:
        return self.LLG.inductance

    @Lg.setter
    def Lg(self, inductance: float) -> None:
        self.LLG.inductance = max(1e-12, inductance)

    @property
    def Lpk(self) -> float:
        return self.LLPK.inductance

    @Lpk.setter
    def Lpk(self, inductance: float) -> None:
        self.LLPK.inductance = max(1e-12, inductance)

    @property
    def C1(self) -> float:
        return self.CC1.capacitance

    @C1.setter
    def C1(self, capacitance: float) -> None:
        self.CC1.capacitance = max(0.1e-12, capacitance)

    @property
    def Cm1(self) -> float:
        return self.CCM1.capacitance

    @Cm1.setter
    def Cm1(self, capacitance: float) -> None:
        self.CCM1.capacitance = max(0.1e-12, capacitance)

    @property
    def Cm2(self) -> float:
        return self.CCM2.capacitance

    @Cm2.setter
    def Cm2(self, capacitance: float) -> None:
        self.CCM2.capacitance = max(0.1e-12, capacitance)

    @property
    def Cm3(self) -> float:
        return self.CCM3.capacitance

    @Cm3.setter
    def Cm3(self, capacitance: float) -> None:
        self.CCM3.capacitance = max(0.1e-12, capacitance)
