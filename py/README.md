# Python challenge solution version

This is not within the time limit of the challenge and is only to proof I can actually write Python

## I've added configs in YAML for both collector.py and analyser.py


## How to run it
1. Open first terminal and execute below.
```
cd py
pip3 install -r requirements.txt

python3 collector
```
This will run check with the interval set in the collector_cfg.yaml file.

2. In second terminal run below for stats.
```
python3 analyse ./analyse_cfg.yaml
```
Configuration file has only two variables:
- logfile
- time window
