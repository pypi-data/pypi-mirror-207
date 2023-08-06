"""Run shell commands from your Python code"""
import subprocess
import os

__attr_type_error_message = "The type of the attribute '{attribute}' must be {type}"

def shell_execute(command: str, encoding: str = 'utf-8') -> str:
    """
    Execute shell command and get output
    """
    # Check attributes' types
    if not isinstance(command, str):
        raise TypeError(__attr_type_error_message.format(attribute="command", type="string"))
    elif not isinstance(encoding, str):
        raise TypeError(__attr_type_error_message.format(attribute="encoding", type="string"))
    
    # Execute the command
    output = subprocess.check_output(command)
    output_string = output.decode(encoding)
    
    # Return the output
    return output_string

def shell_run(command: str) -> None:
    """
    Execute shell command in user's shell
    """
    # Check attribute's type
    if not isinstance(command, str):
        raise TypeError(__attr_type_error_message.format(attribute="command", type="string"))
    # Run the command
    os.system(command)


if __name__ == "__main__":
    systeminfo = shell_execute('systeminfo')
    print(systeminfo.upper())
