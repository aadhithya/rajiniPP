# rajini++

rajini++ (rajinipp, rajiniPP) is a hobby programming language based on the iconic dialogues of Rajinikanth.

This project is inspired by the [ArnoldC](https://github.com/lhartikk/ArnoldC) project.

## Installation
right now, the only way to get rajini++ is to clone the repository and build your own wheel. You need to have at least python 3.8 installed.
- clone project: `git clone https://github.com/aadhithya/rajiniPP.git`
- change directory to rajiniPP: `cd rajiniPP`
- install poetry: `pip install poetry`
- generate wheel: `poetry build`
- install rajini++: `pip install dist/rajinipp-0.0.1-py3-none-any.whl`
- test installation: `rajinipp version`

## The rajini++ language

rajini++ is not a feature rich language and is not intended for serious use. It is rather a hobby project and a tribute to the one and only superstar.

### The `hello_world.rpp` program
The Print function is summoned by using the `DOT` command.
```
LAKSHMI START
DOT "Hello, world!";
KATHAM KATHAM
```
will result in the following output:

![hello world output](./imgs/hello-out.png)

## Learn more about rajini++
- To learn about all the features supported by rajini++ and the rajinipp interpreter, head to the [rajiniPP Wiki](https://github.com/aadhithya/rajiniPP/wiki/rajiniPP)!


## Roadmap
- [x] Math Ops
  - [x] MUL
  - [x] DIV
  - [x] MOD
- [x] Unary Ops
- [x] print multiple objects with the same statement.
- [x] variable declaration
- [x] variable access
- [ ] variable manipulation
- [ ] conditional expressions
- [ ] if statement
- [ ] if-else statement
- [ ] for loop
- [ ] while loop
- [ ] rpp in python integration
- [ ] void functions
