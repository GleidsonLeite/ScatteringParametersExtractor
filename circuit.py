from PySpice.Spice.Netlist import Circuit

circuit = Circuit("Four double-pole Low-Pass RLC Filter")

inductance = 10e-3
capacitance = 1e-6

circuit.SinusoidalVoltageSource("input", "inp", circuit.gnd, amplitude=1)
# Q = .5
circuit.R(1, "inp", 1, 200)
circuit.L(1, 1, "out5", inductance)
circuit.C(1, "out5", circuit.gnd, capacitance)
# Q = 1
circuit.R(2, "inp", 2, 100)
circuit.L(2, 2, "out1", inductance)
circuit.C(2, "out1", circuit.gnd, capacitance)
# Q = 2
circuit.R(3, "inp", 3, 50)
circuit.L(3, 3, "out2", inductance)
circuit.C(3, "out2", circuit.gnd, capacitance)
# Q = 4
R4 = circuit.R(4, "inp", 4, 25)
circuit.L(4, 4, "out4", inductance)
circuit.C(4, "out4", circuit.gnd, capacitance)
