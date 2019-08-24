# Rajini++

Rajini++ (rajiniPP) is a programming language based on the iconic dialogues by Rajinikanth. 

The project is an interpteter(rather translator?) to execute the Rajini++ code by converting it to python code. 

The inspiration for this project is drawn from the amazing [ArnoldC](https://github.com/lhartikk/ArnoldC) project.

## Language Description
---

Rajini++ is not a super feature rich language. To start with, it is designed to support the basic programming constructs like:

* __Math Ops:__  addition, subtraction, multiplication, division, modulo.
* __Logical Ops:__ gt, gte, lt, lte, eq, and, or, not
* __Programming Constructs__: if block, if-else block, for/while loop

The language is also designed to be easily modifiable; one can change the commands to whatever (s)he wants by modifying the `placeholder.json` file.

Rajini++ has a syntax similar to ArnoldC but is simplified for ease of use.

Rajini++ codes can be embedded within python scripts.

Rajini++ scripts have the extension __`.baasha`__.

### Main Method
All Rajini++ codes exist within the main method. The form is:
```
LAKSHMI START
[code statements]
KATHAM KATHAM 
```
Because Rajini++ doesn't yet support functions, this all the code goes into the main block.

### Printing
The Print function is summoned by using the `UNMAI ELLAM SOLLA THONUDHE` command.

e.g.,
```
LAKSHMI START
# x = 10
NAA SOLRADHAYUM SEIVEN x SOLLADHADHAYUM SEIVEN 10
#print(x)
UNMAI ELLAM SOLLA THONUDHE x
KATHAM KATHAM 
```

### Declaring a Variable

All variables should be declared with an initial value. Declaration can be done using the `NAA SOLRADHAYUM SEIVEN` command.  Assignment is done using the `SOLLADHADHAYUM SEIVEN` command.

e.g.,
```
LAKSHMI START
# x = 10
NAA SOLRADHAYUM SEIVEN x SOLLADHADHAYUM SEIVEN 10
KATHAM KATHAM 
```
### Assigning Variable

TODO

### Math Operations

#### 1. Addition
TODO
#### 2. Subtraction
TODO
#### 3. Multiplication
TODO
#### 4. Division
_command_: `SEEVIDUVEN` 
e.g. `z = x seeviduven y #z=x/y`
 
## `helloworld.baasha`
---
```
LAKSHMI START
UNMAI ELLAM SOLLA THONUDHE 'Hello, World!'
KATHAM KATHAM
```
