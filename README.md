# guidata: Automatic GUI generation for easy dataset editing and display with Python

[![license](https://img.shields.io/pypi/l/guidata.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/guidata.svg)](https://pypi.org/project/guidata/)
[![PyPI status](https://img.shields.io/pypi/status/guidata.svg)](https://github.com/CODRA-Ingenierie-Informatique/guidata/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/guidata.svg)](https://pypi.python.org/pypi/guidata/)
[![download count](https://img.shields.io/conda/dn/conda-forge/guidata.svg)](https://www.anaconda.com/download/)

Simple example of ``guidata`` datasets embedded in an application window:

<img src="https://raw.githubusercontent.com/CODRA-Ingenierie-Informatique/guidata/master/doc/images/screenshots/editgroupbox.png">

See [documentation](https://guidata.readthedocs.io/en/latest/) for more details on
the library and [changelog](CHANGELOG.md) for recent history of changes.

Copyrights and licensing:

* Copyright © 2023 [CEA](https://www.cea.fr), [Codra](https://codra.net/), [Pierre Raybaut](https://github.com/PierreRaybaut).
* Licensed under the terms of the BSD 3-Clause (see [LICENSE](LICENSE)).

## Overview

Based on the Qt library, ``guidata`` is a Python library generating graphical user
interfaces for easy dataset editing and display. It also provides helpers and
application development tools for Qt (PyQt5, PySide2, PyQt6, PySide6).

Generate GUIs to edit and display all kind of objects:

* integers, floats, strings ;
* ndarrays (NumPy's n-dimensional arrays) ;
* etc.

Application development tools:

* configuration management
* internationalization (``gettext``)
* deployment tools
* HDF5 I/O helpers
* misc. utils

## Dependencies

### Requirements

* Python 3.7+
* [PyQt5](https://pypi.python.org/pypi/PyQt5) (Python Qt bindings)
* [QtPy](https://pypi.org/project/QtPy/) (abstraction layer for Python-Qt binding libraries)
* [h5py](https://pypi.org/project/h5py/) (interface to the HDF5 data format)
* [NumPy](https://pypi.org/project/numpy/) (operations on multidimensional arrays)

## Installation

### From the source package

```bash
python setup.py install
```
