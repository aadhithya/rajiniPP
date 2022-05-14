# rajini++

![banner_thin](https://user-images.githubusercontent.com/6749212/168450764-5ae486d8-8299-4425-b51d-cf3b9538efb2.png)



![GitHub Workflow Status](https://img.shields.io/github/workflow/status/aadhithya/rajiniPP/Test%20and%20Release?logo=Github%20Actions&logoColor=%23fff&style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/aadhithya/rajiniPP?style=flat-square)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/aadhithya/rajiniPP?logo=semantic%20release&style=flat-square)
![GitHub Release Date](https://img.shields.io/github/release-date/aadhithya/rajiniPP?logo=semantic%20release&style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rajinipp?logo=PyPI&logoColor=%23eaeaea&style=flat-square)
![PyPI - License](https://img.shields.io/pypi/l/rajinipp?style=flat-square)
![GitHub commits since latest release (by SemVer)](https://img.shields.io/github/commits-since/aadhithya/rajiniPP/latest/master?style=flat-square)


![Twitter Follow](https://img.shields.io/twitter/follow/asankar96?style=social)
![GitHub followers](https://img.shields.io/github/followers/aadhithya?style=social)


rajini++ (rajiniPP) is a programming language is a tribute to the one and only superstar and based on the iconic dialogues of Rajinikanth. This is a hobby project ans is not meant to be used for serious software development.



## Installation
- rajinipp requires **python >= 3.8**. Install python from [here](https://www.python.org/downloads/).
- Install the rajini++ interpreter using the following command:
  `pip install rajinipp`

- test installation: `rajinipp version`

## Getting started

rajini++ is not a feature rich language and is not intended for serious use. It is rather a hobby project and a tribute to the one and only superstar.

### Run programs
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
- Workflows setup based on [poetry_project_template](https://github.com/a-parida12/poetry_pypi_template).
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
- [ ] if-else statement
- [ ] for loop
- [ ] while loop
- [ ] void functions
- [ ] number functions
- [ ] string functions

### rajinipp package
- [ ] expose rajinipp python apis:
  - [ ] `rajinipp.api.require`: load rajini++ code into python program.
  - [ ] `rajinipp.api.eval`:
    - [ ] eval rajini++ statement in python scripts.
    - [ ] eval function calls from loaded rajini++ code and return output.

### General
- [x] Add tests.
