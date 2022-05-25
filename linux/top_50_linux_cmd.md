# Top 50 Linux Commands:


## Why bother learning the command line ie linux terminal?
- You would have more control and greater accesss over you machine that you could not do othewise
- It's faster: you learn the commands and get used to them and be way faster.
- You can automate many tasks and save ourselves a lot of time
- It's available everywhere and can be used any sort of developer and software engineer career. Any coding related career.
- It's basically a requirement.
- Cloud computing program and VMs work only on Linux and Unix operating systems


## Why these commands work only on Mac and Linux:
- Open source vs closed source operating systems. Windows is closed source. Mac and Linux are open source.
- Every single type of operating system is a decendant of UNICS
- Windows is on its own and is not a decendant of the UNICS operating system.
- Early Unix versions are from 1969

## What is GNU and Linux:
- Richard Stallman wanted to make his own OS that is compeletely free.
- Another developer name Linus Torvalds started working on the Linux Kernel at the same time.
- And they both merged their creatures Kernel with GNU and it resulted for the OS Linux.
- True UNIX: in order for your to call your operating system UNIX you have to pay a lot of money.
- Unix-Like: are compatible with unix standards but they are free and not as effective as certified.
- Linux itself is just a kernel. Completely free and open source.
- Ubuntu is a Linux distribution of which there's many. 

## What's Shell?
- A shell is a computer interface to an operating system. Shells exposte the OS's serveices to human users or other programs.
- The shell take our commands and gives them to the operating system to perform.
- It's named a shell because it is the outer layer around the OS, like the shell aroudn an oyster!


## Terminal
- Takes your commands and pass them to the shell so it transfers them to the OS.
- Bash and Zsh and Sh shells.


## Let's get started with the actual commands in Linux:

- ```whoami``` : it returns the current user name that's logged in.
- ```man``` : it can be used before any other commands to get the manual for that command.
- ```open``` : it will open a folder or file outside of the terminal in the graphical interface of your machine.
- ```head -n 30``` : prints out by defual the first 10 lines of a file you provide to the command. -n 30 oututs the first 30 lines.
- ```tail``` : prints out by default the last 10 lines of a file. Outputs end of a file.
- ```date``` : prints out the current date and time. you can specify how it should display the time. 

### Basic concept of Redirecting to a file and Appending to a file: Very Important and Useful:
- ``` date > today.txt``` : it will store the output of date command in the today.txt file. Nice redirection.
- ``` date >> today.txt``` : it will append new information to the old file and not replace it with whatever's inside.

### Concatenating files:
- ```cat file_name.txt```: prints out the entir file and whatever's inside of it.
- ```cat file_name.txt second_file.txt```we can provide more than one file name to ```cat``` and it will provide the contents to all of those files.
- we can redirect a combined file thru ```cat``` command and then redirect them to a new file using ```>``` or ```>>```.
- ```cat -n``` : it also returns line numbers along with the lines.

### Read and view the contents of a file:
- ```less file_name.txt``` : used for viewing a file that's superlong and a massive file in a better gui. The qui is like the ```man``` pages.
- you can also do things like seraching in the less program by adding a ```/``` and putting your keyword in.

### echo command: does one thing, it take a value and just yells it back to me:
- ```echo "HILL"``` : prints it back to me
- used for redirecting a command to a file: ```echo "USERNAME=Milad" > config.txt```
- Or used for adding any text to a file. Very useful.

### Find the line, word and byte counts of a file:
- ```wc file_name.txt``` : prints 3 numbers by default first is line count second word count and the last is byte count.

### Piping: we can take the output of one command and pass it as the input to the second command.
- ``` ls -l | wc ``` : we will see the number of lines, words and bytes for the texts that the ls -l command generated for the second command which was the word count command.
- ``` date | wc ``` : another example

### sort command:
- ```sort file_name.txt``` : it print out the sorted version of a file.
- you can now redirect to a new file using ```>```. Or pipe it to any other command.
- Sorting a file numerically: ```sort -n file_name.txt``` will now recognize numbers in a file.
- Duplicate values: ```sort -nu file_name.txt``` only keeps the uniq numbers and gets rid of duplicates.
- Another example is piping a cat command to a sort: ```cat butcher.txt groceries.txt | sort```