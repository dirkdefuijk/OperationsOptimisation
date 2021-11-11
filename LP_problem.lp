\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x00 + 2 x01 + 3 x02 + 2 x03 + 4 x04 + 5 x05 + 2 x10 + 4 x11 + 6 x12
   + 4 x13 + 8 x14 + 10 x15 + x20 + 2 x21 + 3 x22 + 2 x23 + 4 x24 + 5 x25
   + 2 x30 + 4 x31 + 6 x32 + 4 x33 + 8 x34 + 10 x35 + 3 x40 + 6 x41 + 9 x42
   + 6 x43 + 12 x44 + 15 x45
Subject To
 R0: x00 + x01 + x02 + x03 + x04 + x05 = 1
 R1: x10 + x11 + x12 + x13 + x14 + x15 = 1
 R2: x20 + x21 + x22 + x23 + x24 + x25 = 1
 R3: x30 + x31 + x32 + x33 + x34 + x35 = 1
 R4: x40 + x41 + x42 + x43 + x44 + x45 = 1
 R5: x00 + x10 + x20 + x30 + x40 <= 1
 R6: x01 + x11 + x21 + x31 + x41 <= 1
 R7: x02 + x12 + x22 + x32 + x42 <= 1
 R8: x03 + x13 + x23 + x33 + x43 <= 1
 R9: x04 + x14 + x24 + x34 + x44 <= 1
 R10: x05 + x15 + x25 + x35 + x45 <= 1
Bounds
Binaries
 x00 x01 x02 x03 x04 x05 x10 x11 x12 x13 x14 x15 x20 x21 x22 x23 x24 x25
 x30 x31 x32 x33 x34 x35 x40 x41 x42 x43 x44 x45
End
