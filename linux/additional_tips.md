# Some more additional useful tips for linux terminal:

- The PATH and PYTHONPATH env variables store the all the directories to which any program need be executed will look at to find the executable file to run:
  - in order for all the programs to be run on your machine, their program directory needs to be in the $PATH variable.
  - in order for any python modular programs to run, their root directory need to be added to the $PYTHONPATH variable.
- How to modify these files:
  - you will need to add this line to your .bashrc or .zshrc in your home directory to permanently add a directory to your PATH or PYTHONPATH env:
  - ```export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"```
  - ```export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"```
  - to temporarily add any dir to any of these variables, just run the command directly in the terminal. it will not save it next time you log in to terminal.