# SPDX-FileCopyrightText: 2022 The Ikarus Developers mueller@ibb.uni-stuttgart.de
# SPDX-License-Identifier: LGPL-3.0-or-later

import setpath
setpath.set_path()
import ikarus as iks
import numpy

import dune.grid


if __name__ == "__main__":
    lowerLeft = []
    upperRight = []
    elements = []
    for i in range(2):
        lowerLeft.append(-1)
        upperRight.append(1)
        elements.append(3)

    grid = dune.grid.structuredGrid(lowerLeft,upperRight,elements)
    nDofs1 = grid.size(2)
    nDofs2 = grid.size(2)
    for i in range(2):
        nDofs2 += grid.size(i)




