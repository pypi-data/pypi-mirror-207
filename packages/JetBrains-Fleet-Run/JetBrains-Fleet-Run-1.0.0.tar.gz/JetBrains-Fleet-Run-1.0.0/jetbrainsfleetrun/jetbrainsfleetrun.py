import os
import sys

"""This is a package made for running
    Python files in JetBrains Fleet using 
    run.json with command line arguments.
"""

def find_filename():
    """Gets the filename of the file
    that you want to run in JetBrains
    Fleet

    Returns:
        string: filename
    """
    filename = os.path.basename(sys.argv[0])
    return str(filename)

def run(filename=find_filename()):
    """Runs the file specified by the
    import in JetBrains Fleet

    Args:
        filename (string, optional): Filename of the file you want to execute. Defaults to find_filename().
    """
    os.system(f"python {filename}")