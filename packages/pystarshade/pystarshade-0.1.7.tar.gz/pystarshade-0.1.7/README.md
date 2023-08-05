# PyStarshade

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Overview

Developed by Jamila Taaki (UIUC).

PyStarshade is a Python library for Starshade simulations from star-planet system to CCD with Fresnel diffraction methods. This library efficiently calculates output fields using Bluestein FFTs.

What is a Bluestein FFT? The Bluestein Fast Fourier Transform (1968) is an algorithm that computes M equispaced samples of the Discrete-Time Fourier Transform (DTFT) over an arbitrary frequency region between [0, 1/dx] for a compact input signal containing N non-zero samples, each with a size of dx. The computational complexity of this method in one dimension is O((N+M)log(N+M)). The Bluestein FFT is particularly advantageous when large zero-padding factors would be needed for performing optical propagation using FFT's.

This means that end-to-end simulation can be performed with arbitrary high-resolution sampling in each plane of propagation. 

This library is compatible with Python 3.6 and later versions. 


## Example
Log starlight supression with a truncated Hypergaussian apodization, sweeping star planet brightness ratios between (10e-8, 10e-3). Planet at a 2 AU separation and 10 pc distance from Earth. 
<p align="center">
  <img src="images/contrast_.gif" alt="Star planet brightness ratio range (10e-8, 10e-3)">
</p>

## Installation

You can install PyStarshade using pip:

```bash
pip install pystarshade
```

## Dependencies

Scipy, Numpy

## Quickstart
import pystarshade

Nominal parameters: 

## Organization

<pre>
Pystarshade
├── examples
│   ├── haystacks_model.py
│   └── star_exo.py
├── images
│   └── contrast_.gif
├── __init__.py
├── pystarshade
│   ├── apodization
│   │   ├── apodization.py
│   │   ├── __init__.py
│   │   └── sample.py
│   ├── diffraction
│   │   ├── bluestein_fft.py
│   │   ├── diffract.py
│   │   ├── field.py
│   │   ├── __init__.py
│   │   └── util.py
│   ├── __init__.py
│   ├── simulate_field.py
│   └── version.py
├── README.md
└── setup.py

</pre>

## License

[PyStarshade] is released under the [GNU General Public License v3.0](LICENSE).
