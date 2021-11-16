\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.87 X0|0 + 0.7 X0|1 + 0.12 X0|2 + 0.87 X1|0 + 0.7 X1|1 + 0.12 X1|2
   + 0.87 X2|0 + 0.7 X2|1 + 0.12 X2|2 + 0.87 X3|0 + 0.7 X3|1 + 0.12 X3|2
Subject To
 R0: <= -1
 flight_1: X1|1 = 1
 flight_2: X2|0 = 1
 flight_3: X3|2 = 1
Bounds
Binaries
 X0|0 X0|1 X0|2 X1|0 X1|1 X1|2 X2|0 X2|1 X2|2 X3|0 X3|1 X3|2
End
