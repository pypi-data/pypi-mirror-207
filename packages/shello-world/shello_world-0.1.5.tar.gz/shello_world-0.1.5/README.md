
# Shello-world: simple Python functions to run shell commands
A few simple Python functions allow you to run shell commands from your Python code.

## Why shello-world?
It is a simple and quick solution if you don't want to use a big library or framework.

## Usage
Let's take a look at a simple example below:
```python
from shello_world import shell_execute, shell_run

# Both functions work similarly

# Use shell_run if you want to run a command
# directly in your shell, like you'd enter it
shell_run("color a") # Change font color to green
# But shell_run doesn't return anything
output = shell_run("echo 'This text is printed in the shell'")
print(output is None) # True

# Use shell_execute to get output to use it in your code
# shell_execute doesn't print anything
systeminfo = shell_execute("systeminfo")
# But it always returns result as a string
print(systeminfo.upper())
#
# HOST NAME:
# OS NAME:
# OS VERSION:
# ...
#
```

## Installation
### pip
```
pip install shello-world
```
### poetry
```
poetry add shello-world
```

## Links
[PyPI](https://pypi.org/project/shello-world/)  
[GitHub](https://github.com/numericmaestro/shello-world)