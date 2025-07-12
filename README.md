# 3D Rotation with Quaternions - TIPE 2024

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg)](notebooks/quaternion_analysis.ipynb)

> ⚠️ This project contains documents written in French, as it was part of my academic work during my classes.

## Introduction
This repository presents a comparative study of 3D rotation methods: classical matrix rotations and quaternion-based rotations. The project is part of a TIPE (Travail d'Initiative Personnelle Encadrée) by Zakariae El Bouzidi.

## Mathematical Context
- **Rotation matrices**: 3x3 orthogonal matrices representing 3D rotations
- **Quaternions (ℍ)**: Hypercomplex numbers providing a robust alternative for 3D rotations

![Quaternion Multiplication Graph](Picture/Q8_multiplication_graph.svg)
*Visualization of quaternion multiplication structure*

## Objectives
- Demonstrate the mathematical and computational advantages of quaternions for 3D rotations
- Provide a complete, tested implementation for both methods
- Serve as a reference for academic and engineering studies

## Performance Results
The project benchmarks both methods:
- **Matrix rotations**: 90 multiplications, 60 additions per rotation
- **Quaternions**: 48 multiplications, 24 additions per rotation

Performance graphs and detailed analysis are available in the [notebook](notebooks/quaternion_analysis.ipynb) and the [PDF report](docs/Quaternion_TIPE_2024.pdf).

## Repository Structure
- `src/` : Python modules for matrix and quaternion rotations, and performance comparison
- `notebooks/` : Jupyter notebook for demonstrations and analysis
- `tests/` : Unit tests for all rotation methods
- `docs/` : Project documentation and the full TIPE PDF

## Installation & Usage
```bash
pip install -r requirements.txt
```

Run the notebook:
```bash
jupyter notebook notebooks/quaternion_analysis.ipynb
```

Run tests:
```bash
pytest tests/
```

## Download the full PDF report
[📄 Download the complete PDF (French)](docs/Quaternion_TIPE_2024.pdf)

## License
MIT License © Zakariae El Bouzidi 