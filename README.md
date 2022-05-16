# rajini++

![banner_thin](https://user-images.githubusercontent.com/6749212/168450764-5ae486d8-8299-4425-b51d-cf3b9538efb2.png)



[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/aadhithya/rajiniPP/Test%20and%20Release?logo=Github%20Actions&logoColor=%23fff&style=flat-square)](https://github.com/aadhithya/rajiniPP/actions/workflows/release.yml)
[![GitHub issues](https://img.shields.io/github/issues/aadhithya/rajiniPP?style=flat-square)](https://github.com/aadhithya/rajiniPP/issues)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/aadhithya/rajiniPP?logo=semantic%20release&style=flat-square)](https://pypi.org/project/rajinipp/)
![GitHub Release Date](https://img.shields.io/github/release-date/aadhithya/rajiniPP?logo=semantic%20release&style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rajinipp?logo=PyPI&logoColor=%23eaeaea&style=flat-square)
![PyPI - License](https://img.shields.io/pypi/l/rajinipp?style=flat-square)
![GitHub commits since latest release (by SemVer)](https://img.shields.io/github/commits-since/aadhithya/rajiniPP/latest/master?style=flat-square)


[![Twitter Follow](https://img.shields.io/twitter/follow/asankar96?style=social)](https://twitter.com/asankar96)
[![GitHub followers](https://img.shields.io/github/followers/aadhithya?style=social)](https://github.com/aadhithya)


rajini++ (rajiniPP) is a programming language is a tribute to the one and only superstar and based on the iconic dialogues of Rajinikanth. This is a hobby project ans is not meant to be used for serious software development.

## Superstar Rajinikanth
- [Who is Rajinikanth](https://www.youtube.com/watch?v=YDUQZwMHMoo)?
- [Rajinikanth on Wikipedia](https://en.wikipedia.org/wiki/Rajinikanth).

## Installation
- rajinipp requires **python >= 3.8**. Install python from [here](https://www.python.org/downloads/).
- Install the rajini++ interpreter using the following command:
  `pip install rajinipp`

- test installation: `rajinipp version`

## Getting started

rajini++ is not a feature rich language and is not intended for serious use. It is rather a hobby project and a tribute to the one and only superstar.

### Run programs
`hello_world.rpp`:
```
LAKSHMI START
DOT "Hello, World!";
MAGIZHCHI
```
- Run the `hello_world.rpp` program:

  `rajinipp run examples/hello_world.rpp`

will result in the following output:

![hello world output](./imgs/hello-out.png)



## Resources
- **Learn the rajini++ language**:
  -  **The rajini++ language documentation** can be found at the [rajiniPP Wiki](https://github.com/aadhithya/rajiniPP/wiki/).
  -  Example programs can be found here: [Example Programs](https://github.com/aadhithya/rajiniPP/tree/master/examples).
- **The rajini++ Language Spec**: The rajini++ commands and its equivalent in python3 can be found at the [rajiniPP Language Spec](https://github.com/aadhithya/rajiniPP/wiki/rajiniPP:-Language-Specification) wiki.
- **The rajinipp Interpreter Documentation**: The documentation for the rajinipp interpreter can be found [here](https://github.com/aadhithya/rajiniPP/wiki/rajinipp:-The-interpreter).


## Acknowledgements
- A lot of learnings from [DIVSPL](https://github.com/di/divspl) and its accompanying [pycon talk](https://www.youtube.com/watch?v=ApgUrtCrmV8).
- A lot of learnings from [this pycon talk](https://www.youtube.com/watch?v=LCslqgM48D4&t=1388s) by [Alex Gaynor](alex).
- Workflows setup based on [poetry_pypi_template](https://github.com/a-parida12/poetry_pypi_template).
- This project is inspired by the [ArnoldC](https://github.com/lhartikk/ArnoldC) project.



## Roadmap
### rajini++ Features
- [x] Math Ops
  - [x] SUM
  - [x] SUB
  - [x] MUL
  - [x] DIV
  - [x] MOD
- [x] Unary Ops
- [x] print multiple objects with the same statement.
- [x] variable declaration
- [x] variable access
- [x] variable manipulation
- [x] bool data type
- [x] float datatype
- [x] logical ops
- [x] if statement
- [x] if-else statement
- [x] for loop
- [x] while loop
- [x] functions
- [x] functions with return
- [ ] fuinctions with arguments
- [ ] Execute python code in rajini++ scripts
### rajinipp package
- [ ] rajinipp python runner:
  - [ ] `rajinipp.api.require`: load rajini++ code into python program.
  - [x] `rajinipp.runner.RppRunner.exec`: execute rajini++ programs in python loaded as string.
  - [ ] `rajinipp.runner.RppRunner.eval`:
    - [x] eval rajini++ statement in python scripts [limited support].
    - [ ] support flow control statements.
    - [ ] eval function calls from loaded rajini++ code and return output.
- [ ] rajinipp shell to run rajini++ commands from the terminal.
  - [x] limited support using `rajinipp.runner.RppRunner.eval`.
  - [ ] complete support to all rajini++ features.

### General
- [x] Add tests.
- [x] semantic releases.
