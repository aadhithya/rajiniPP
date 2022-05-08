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

rajini++ is not a feature rich language, it is rather a hobby language and a tribute to the one and only super star.

### Main Method
All rajini++ codes exist within the main method. The form is:
```
LAKSHMI START
[code statements]
KATHAM KATHAM
```

### The `hello_world.rpp` program
The Print function is summoned by using the `DOT` command.
```
LAKSHMI START
DOT("Hello, world!");
KATHAM KATHAM
```
will result in the following output:

![hello world output](./imgs/hello-out.png)


- **Note**: All raniji++ statements terminate with a semicolon!

### Running a rajini++ script
- the rajini++ scripts(`.rpp`) can be run using the following command: `rajinipp run path/to/file./rpp`
