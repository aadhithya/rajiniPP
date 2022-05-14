# rajini++
<p align="center">
<img width=256 src="https://user-images.githubusercontent.com/6749212/167663396-3030d334-ebde-4b0e-939b-ff48e146f488.png"/>
</p>

rajini++ (rajiniPP) is a programming language is a tribute to the one and only superstar and based on the iconic dialogues of Rajinikanth. This is a hobby project ans is not meant to be used for serious software development.

This project is inspired by the [ArnoldC](https://github.com/lhartikk/ArnoldC) project.

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
- **Learn the rajini++ language**: The documentation for rajini++, the language can be found at the [rajiniPP Wiki](https://github.com/aadhithya/rajiniPP/wiki/).
- **The rajini++ Language Spec**: The rajini++ commands and its equivalent in python3 can be found at the [rajiniPP Language Spec](https://github.com/aadhithya/rajiniPP/wiki/rajiniPP:-Language-Specification) wiki.
- **The rajinipp Interpreter Documentation**: The documentation for the rajinipp interpreter can be found [here](https://github.com/aadhithya/rajiniPP/wiki/rajinipp:-The-interpreter).


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
