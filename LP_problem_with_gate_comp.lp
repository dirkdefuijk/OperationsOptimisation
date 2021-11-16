\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x00 + 2 x01 + 3 x02 + 2 x10 + 4 x11 + 6 x12 + 3 x20 + 6 x21 + 9 x22
Subject To
 R0: x00 = 1
 R1: x12 = 1
 R2: x21 = 1
 R3: x00 <= 1
 R4: x21 <= 1
 R5: x12 <= 1
Bounds
Binaries
 x00 x01 x02 x10 x11 x12 x20 x21 x22
End
