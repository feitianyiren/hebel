# Copyright (C) 2013  Hannes Bretschneider

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os as _os

sequence_conv_root = _os.path.split(
    _os.path.abspath(_os.path.dirname(__file__)))[0]

from scikits.cuda import linalg
linalg.init()

DNA_A = 0b1000
DNA_C = 0b0100
DNA_G = 0b0010
DNA_T = 0b0001
DNA_R = 0b1010
DNA_Y = 0b0101
DNA_N = 0b0000

def enum(*sequential, **named):
    # Implementation of enums in Python 2
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)
