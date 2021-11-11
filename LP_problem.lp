\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x00 + 2 x01 + 3 x02 + 2 x03 + 2 x10 + 4 x11 + 6 x12 + 4 x13 + 3 x20
   + 6 x21 + 9 x22 + 6 x23 + 5 x30 + 10 x31 + 15 x32 + 10 x33
Subject To
 R0: x00 + x03 = 1
 R1: x12 = 1
 R2: x21 = 1
 R3: x30 + x33 = 1
 R4: x00 + x30 <= 1
 R5: x21 <= 1
 R6: x12 <= 1
 R7: x03 + x33 <= 1
Bounds
Binaries
 x00 x01 x02 x03 x10 x11 x12 x13 x20 x21 x22 x23 x30 x31 x32 x33
End
