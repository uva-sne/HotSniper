#!/usr/bin/env python3 

# Line Format: <unit-name>\t<width>\t<height>\t<left-x>\t<bottom-y>
Core63 = (0.000887, 0.000887, 0.006209, 0.000000)
ncores = 64

chip_size = (8 * Core63[0]) * (8 * Core63[0])
print("chip {:e}".format(chip_size))
print("core size {:e}".format(chip_size / ncores))


