# Shello-world: run shell commands from your Python code via simple functions
A few simple Python functions allow you to run shell commands from your Python code

## Why shello-world?
It isn't a big library or framework. If you want a quick solution, you could prefer shello-world.

## Usage
Let's take a look at a simple example below
```python
from shello_world import shell_execute, shell_run

# Both functions work similarly

# shell_run runs a command directly in your shell
# Change color to green
shell_run("color a")
# You will see executing ipconfig in your shell just like you'd enter it
ipconfig = shell_run("ipconfig")
# But the function doesn't return anything
print(ipconfig is None) # True

# shell_execute doesn't print executing in your shell by default
systeminfo = shell_execute("systeminfo") # This line doesn't print anything
# But it always returns result as a string
print(systeminfo.upper())
print(systeminfo.split())
```

## Installation
You can install this library with ```pip install shello-world``` command.