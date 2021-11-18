\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  X0|0 + 0.29 X0|1 + 0.31 X0|2 + 0.05 X1|0 + 0.0145 X1|1 + 0.0155 X1|2
   + 3 X2|0 + 0.87 X2|1 + 0.93 X2|2
Subject To
 flight_0: X0|0 = 1
 flight_1: X1|1 = 1
 flight_2: X2|1 + X2|2 = 1
 gate_0: X0|0 <= 1
 gate_1: X1|1 + X2|1 <= 1
 gate_2: X2|2 <= 1
Bounds
Binaries
 X0|0 X0|1 X0|2 X1|0 X1|1 X1|2 X2|0 X2|1 X2|2
End
