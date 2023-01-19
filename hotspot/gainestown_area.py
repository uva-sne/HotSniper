#!/usr/bin/env python3 

# Line Format: <unit-name>\t<width>\t<height>\t<left-x>\t<bottom-y>
Core0 =	(0.00496516316, 0.0057122545, 0.00541883244, 0.00000000000)
Core1 =	(0.00496516316, 0.0057122545, 0.00541883244, 0.00571307345)
L3 = (0.00541883244, 0.01142450900, 0.00000000000, 0.00000000000)
ncores = 2

chip_area = (L3[0] + Core0[0]) * L3[1]
print("chip size {:e}".format(chip_area))
print("core size {:e}".format(chip_area / ncores))
