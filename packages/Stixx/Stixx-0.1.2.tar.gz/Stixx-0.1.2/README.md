# Stixx

Stixx is an up and coming two-player game where the objective of the game is
to deplete your opponent of their sticks. Players start with a stick in each of
their hands and add sticks to the opponent based on how many sticks they
currently have. If either player gets exactly five sticks, they lose said hand.

<!-- ![GitHub](https://img.shields.io/github/license/mg4145/stixx)-->
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Issues](https://img.shields.io/github/issues/mg4145/stixx)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]
[![Build Status](https://github.com/mg4145/stixx/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/mg4145/stixx/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/mg4145/stixx/branch/main/graph/badge.svg)](https://codecov.io/gh/mg4145/stixx)
[![PyPI](https://img.shields.io/pypi/v/stixx)](https://pypi.org/project/stixx/)
[![Docs](https://img.shields.io/readthedocs/stixx)](https://stixx.readthedocs.io/)

# Overview
Stixx is childhood game that many of us have played under different names or
rules. The purpose of this project is to give back the nostalgia that this
childhood game gave us. The current plan is to have a bare-bones UI of the game
that works. There are also exciting plans in for future of this game.

[black]: https://github.com/psf/black

<!--
## Features

- TODO

## Requirements

- TODO
-->

## Installation

You can install _stixx_ via [pip] from [PyPI]:

```console
$ pip install stixx
```

# Running
  - Locate the directory
```bash
$ pip show stixx | grep "Location"
```
  - Once the location has been found change directories to said location
  ```bash
  $ cd <location>
  ```
  -  Run the game
```bash
$ python game.py
```

## Demo
![](demo.gif)

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [Apache 2.0 license][license],
_stixx_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/mg4145/stixx/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/mg4145/stixx/blob/main/LICENSE
[contributor guide]: https://github.com/mg4145/stixx/blob/main/CONTRIBUTING.md
[command-line reference]: https://stixx.readthedocs.io/en/latest/usage.html
