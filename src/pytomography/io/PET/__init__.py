"""PyTomography is committed to providing support for the PETSIRD data format, established by the Emission Tomography Standardization Initiative (ETSI). The establishment of this data type is still in early stages; once an official repository is established, PyTomography will include it as a dependency. For now, data types are defined in the /prd directory, which was generated from the ``https://github.com/ETSInitiative/PRDdefinition`` repository using ``yardl``. In addition, the ``read_prd`` function in the ``petsird.py`` file was borrowed from the ``https://github.com/ETSIhackers/LMSimRecon`` library. While it is expected that all this code will be formatted into a single library in the future, PyTomography will currently manage the functionality in its own source code."""

from . import prd