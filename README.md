# GRASS GIS Interpolation Script

This repository contains a Python script that performs spatial interpolation using GRASS GIS's `r.series.lwr` module. The script is compatible with both Ubuntu and Windows Subsystem for Linux (WSL).

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

The provide input output parameters in the main.py script
