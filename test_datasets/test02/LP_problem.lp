\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.87 X0|0 + 0.7 X0|1 + 0.88 X0|2 + 0.88 X0|3 + 0.12 X0|4 + 0.87 X1|0
   + 0.7 X1|1 + 0.88 X1|2 + 0.88 X1|3 + 0.12 X1|4 + 0.87 X2|0 + 0.7 X2|1
   + 0.88 X2|2 + 0.88 X2|3 + 0.12 X2|4 + 0.87 X3|0 + 0.7 X3|1 + 0.88 X3|2
   + 0.88 X3|3 + 0.12 X3|4
Subject To
 flight_0: X0|1 = 1
 flight_1: X1|1 = 1
 flight_2: X2|1 = 1
 flight_3: X3|1 = 1
 gate_0: X0|1 <= 1
 gate_1: X1|1 <= 1
 gate_2: X2|1 <= 1
 gate_3: X3|1 <= 1
Bounds
Binaries
 X0|0 X0|1 X0|2 X0|3 X0|4 X1|0 X1|1 X1|2 X1|3 X1|4 X2|0 X2|1 X2|2 X2|3 X2|4
 X3|0 X3|1 X3|2 X3|3 X3|4
End
