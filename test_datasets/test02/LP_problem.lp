\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  X0|0 + 2 X0|1 + 3 X0|2 + 2 X1|0 + 4 X1|1 + 6 X1|2 + 3 X2|0 + 6 X2|1
   + 9 X2|2 + 4 X3|0 + 8 X3|1 + 12 X3|2
Subject To
 flight_0: X0|0 + X0|1 + X0|2 = 1
 flight_1: X1|0 + X1|1 + X1|2 = 1
 flight_2: X2|0 + X2|1 + X2|2 = 1
 flight_3: X3|0 + X3|1 + X3|2 = 1
 gate_0: X0|0 + X1|0 + X2|0 + X3|0 <= 1
 gate_1: X0|1 + X1|1 + X2|1 + X3|1 <= 1
 gate_2: X0|2 + X1|2 + X2|2 + X3|2 <= 1
Bounds
Binaries
 X0|0 X0|1 X0|2 X1|0 X1|1 X1|2 X2|0 X2|1 X2|2 X3|0 X3|1 X3|2
End
