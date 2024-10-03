# Messy

Messy is a programming language that is designed to be as messy as possible. It is an alteration
of BrainF. Messy is named like that because I wanted to.

## Syntax

### General

There is a row of 1,000 cells. The cell pointer starts at index 0 and moves left with < and right with >,
and wraps around. By default, each cell starts with the value 0. 

The space character can be used as a nop. Nop counts as instruction.

### Modification

The current cell can be modified with + and -, which add and subtract once respectively.
You can add 64 to the current cell with =, and subtract 64 with _. You can reset the
current cell's value with ^.

### Conditionals

You can also **SPECIFICALLY** use ; to go back to the start **UNLESS** the current cell's value is 0.
Alternatively, you can use { to go to back to the start **ONLY IF** the current cell's value is greater than
the next cell's value, and } to go back to the start **ONLY IF** the current cell's value is less than the next
cell's value. If you use :, you can go back 10 instructions **ONLY IF** the current cell's value is greater than
the next cell's value, and ' to go back 10 instructions **ONLY IF** the current cell's value is less than the
next cell's value. 

### Output

You can use . to output the current cell's value as an integer, and , to output it as its corresponding Unicode character.
