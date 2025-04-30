# Delta-Interference Protocol

This repository contains the full source, circuit logic, simulation data, and whitepaper for:

**The Δ-Interference Protocol: A Statistical Experiment to Distinguish Quantum Interpretations via Branch-Aware Superposition**  
Author: Fulvio Cusumano

## Overview

This experiment implements a quantum circuit designed to probe the foundations of quantum mechanics by comparing outcome probabilities across computational branches. The measured quantity:

```
Δ = P(000) - P(111)
```

serves as a statistical witness for Many-Worlds-style interference. Results consistently show Δ > 0 under simulation, which is not predicted by collapse-based interpretations.

## Contents

- `delta_interference_protocol_complete.tex` – Full whitepaper (LaTeX)
- `notebooks/branch_interference_test.ipynb` – Jupyter notebook for experiment
- `scripts/run_branch_test.py` – CLI version of the protocol
- `results/delta_values.csv` – Simulated Δ values over multiple trials
- `LICENSE` – MIT license
- `.gitignore` – Build and temp file exclusions
- `README.md` – Project overview and instructions

## How It Works

A 3-qubit quantum circuit:
- Q₀ is the control (placed in superposition)
- Q₁ executes one logic branch (X gate)
- Q₂ executes another logic branch (H gate)
- Q₀ is interfered with a Hadamard gate before measurement
- All qubits are measured
- Δ is computed as `P(000) - P(111)`

If Δ ≠ 0 consistently, it implies both branches interfered before decoherence — a result that challenges collapse-only interpretations.

## Sample Δ Output

```
trial,delta
1,0.0487
2,0.0501
3,0.0479
...
10,0.0509
```

The results suggest a ~5% bias toward one branch, aligned with predictions from the Many-Worlds Interpretation.

## How to Run

### Requirements
- Python 3
- Qiskit
- Matplotlib

### CLI Run

```bash
python scripts/run_branch_test.py
```

### Notebook Run

Launch and execute each cell in:

```bash
notebooks/branch_interference_test.ipynb
```

Includes circuit build, histogram plot, and Δ calculation.

## Citation

If you use or reference this work, please cite:

**Fulvio Cusumano**, *The Δ-Interference Protocol*  
[https://github.com/gotnull/delta-interference-protocol](https://github.com/gotnull/delta-interference-protocol)

---

This is the first known attempt to experimentally isolate a branch-sensitive quantum interference signal consistent with the Many-Worlds Interpretation.