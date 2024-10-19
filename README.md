# GRASS GIS Local Weighted Regression (LWR) Interpolation Python Script

This repository contains a Python script that performs spatial interpolation using GRASS GIS's `r.series.lwr` module. The script is compatible with both Ubuntu and Windows Subsystem for Linux (WSL).
Cleveland and Devlin 1988
Read More Here: https://grass.osgeo.org/grass84/manuals/addons/r.series.lwr.html
## Requirements

- **OS**: Ubuntu or WSL
- **Memory**: Minimum 16 GB RAM @ 3200 MHz
- **CPU**: Minimum 6 processor cores @ 1.98 GHz

This script is computationally intensive, so it's recommended to run it on a machine that meets or exceeds these requirements for smooth execution.

## Installation

### 1. Install GRASS GIS

Before running the script, ensure that GRASS GIS and its development tools are installed on your system:

```bash
sudo apt-get install grass grass-dev
export GRASSBIN=/usr/bin/grass
grass --version
```
### 2. Run the script
The provide input output parameters in the main.py script
