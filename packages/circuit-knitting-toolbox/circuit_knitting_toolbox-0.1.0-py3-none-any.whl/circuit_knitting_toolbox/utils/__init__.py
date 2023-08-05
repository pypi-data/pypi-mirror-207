# This code is a Qiskit project.

# (C) Copyright IBM 2022.

# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Utility functions.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   conversion
   metrics
   orbital_reduction.reduce_bitstrings
"""

from .orbital_reduction import reduce_bitstrings

__all__ = [
    "reduce_bitstrings",
]
