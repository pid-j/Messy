"""
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
"""
# FUNCTIONS
def makeErrorMessage(col: int, string: str, file: str, error) -> str:
	buffer = f"...{string[col]}..."
	buffer += "\n   "
	buffer += "^\n\n"
	buffer += f"File {file}, column {col}\n"
	buffer += error.name + (f": {error.message}" if error.message else "")
	return buffer

# CLASSES
class Error:
	def __init__(self, col: int, message: str, name: str = "Error") -> None:
		self.col = col
		self.message = message
		self.name = name

	def __str__(self) -> str:
		return self.name + (f": {self.message}" if self.message else "")

class IllegalCharError(Error):
	def __init__(self, col: int, message: str) -> None:
		super().__init__(col, message, "IllegalCharError")

class IllegalJumpError(Error):
	def __init__(self, col: int, message: str) -> None:
		super().__init__(col, message, "IllegalJumpError")

class Process:
	"A process of Messy."
	def __init__(self) -> None:
		self.ptable = [0 for idx in range(1000)]
		self.cidx = 0
		self.chidx = 0

	def goRight(self) -> None:
		self.cidx += 1
		self.cidx %= len(self.ptable)

	def goLeft(self) -> None:
		self.cidx -= 1
		self.cidx += len(self.ptable) * int(self.cidx < 0)

	def execute(self, string: str) -> None:
		self.chidx = 0
		while self.chidx < len(string):
			JUMP_ERROR_MSG = makeErrorMessage(
				self.chidx, string, "<stdin>",
				IllegalJumpError(
					self.chidx,
					"Attempted to perform jump by 10 instructions backward"
				)
			)
			char = string[self.chidx]
			if char == "+":
				self.ptable[self.cidx] += 1
				self.chidx += 1
				continue
			if char == "-":
				self.ptable[self.cidx] -= 1
				self.chidx += 1
				continue
			if char == "=":
				self.ptable[self.cidx] += 64
				self.chidx += 1
				continue
			if char == "_":
				self.ptable[self.cidx] -= 64
				self.chidx += 1
				continue
			if char == "^":
				self.ptable[self.cidx] = 0
				self.chidx += 1
				continue
			if char == " ":
				self.chidx += 1
				continue
			if char == "<":
				self.goLeft()
				self.chidx += 1
				continue
			if char == ">":
				self.goRight()
				self.chidx += 1
				continue
			if char == ";":
				if self.ptable[self.cidx] != 0:
					self.chidx = 0
					continue
				self.chidx += 1
				continue
			if char == "{":
				pidx = (self.cidx + 1) % len(self.ptable)
				if self.ptable[self.cidx] > self.ptable[pidx]:
					self.chidx = 0
					continue
				self.chidx += 1
				continue
			if char == "}":
				pidx = (self.cidx + 1) % len(self.ptable)
				if self.ptable[self.cidx] < self.ptable[pidx]:
					self.chidx = 0
					continue
				self.chidx += 1
				continue
			if char == ":":
				pidx = (self.cidx + 1) % len(self.ptable)
				if self.ptable[self.cidx] > self.ptable[pidx]:
					self.chidx -= 10
					if self.chidx > 0:
						print(JUMP_ERROR_MSG)
						break
					continue
				self.chidx += 1
				continue
			if char == "'":
				pidx = (self.cidx + 1) % len(self.ptable)
				if self.ptable[self.cidx] < self.ptable[pidx]:
					self.chidx -= 10
					if self.chidx < 0:
						print(JUMP_ERROR_MSG)
						break
					continue
				self.chidx += 1
				continue
			if char == ".":
				print("", end=str(self.ptable[self.cidx]))
				self.chidx += 1
				continue
			if char == ",":
				print("", end=chr(self.ptable[self.cidx]))
				self.chidx += 1
				continue
			CHAR_ERROR_MSG = makeErrorMessage(
				self.chidx, string, "<stdin>",
				IllegalCharError(
					self.chidx,
					f"Illegal character \"{char}\"")
			)
			print(CHAR_ERROR_MSG)
			break

# TEST
if __name__ == "__main__":
	print("Messy - Python Shell")
	process = Process()
	while True:
		process.execute(input(">>> "))
