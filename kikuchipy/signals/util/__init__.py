# -*- coding: utf-8 -*-
# Copyright 2019-2021 The kikuchipy developers
#
# This file is part of kikuchipy.
#
# kikuchipy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kikuchipy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kikuchipy. If not, see <http://www.gnu.org/licenses/>.

"""Signal utilities for handling signal metadata and attributes, output
from signal methods, and for controlling chunking of lazy signal data in
:class:`~dask.array.Array`.
"""

from kikuchipy.signals.util._dask import get_chunking, get_dask_array
from kikuchipy.signals.util._metadata import ebsd_metadata, metadata_nodes

__all__ = [
    "ebsd_metadata",
    "get_chunking",
    "get_dask_array",
    "metadata_nodes",
]
