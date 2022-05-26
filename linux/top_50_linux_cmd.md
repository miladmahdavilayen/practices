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

### uniq command:
- you may find the unique values in a file of lines and remove all the duplicates
- ``` uniq file_name.txt``` : will remove only adjacent duplicated values in a file. Not duplicate values that are disperesed in a file.
- You can use this in conjunction with sort and then only keep the unique values in a file like below:
- ``` sort favorites.txt | uniq ```
- ``` uniq -d -u -c``` these options give you more flexibility to your uniq command
- ```-c``` will show the counts of each value with a uniq function


## Expansions:

- ``` echo ~ ``` : This is called "tildee" and it will be expanded to your home directory.
- ``` echo $PATH ``` : This will echo an expansion of the Environment Variable PATH. It specifies the directories in which executable programs are located on the machine that can be started without knowing and typing the whole path to the file on the command line.
- ``` echo $USER ```: Anotehr env variable for the current user name.
- ``` echo *.txt ``` : it will echo any files with txt extension in the current dir
- ``` echo *.?? ``` : will echo any file names with any two characters after the. ? means any single char.


### creating multiple files or a list of names or values using {} curly braces:
- ``` echo {a,b,c}.txt ``` : this will print out or just echo 3 file names as a.txt, b.txt and c.txt
- ``` touch app.{js,html,py,md} ``` : this will create 4 files with the given extenstions all with the same name.
- ``` echo day_{1..365} ``` : will echo 

### diff command:
- ```diff file.txt file_2.txt ``` : simply shows with line numbers where of the two files are differenct by showing a as added, d as removed, and c as changed for each line.
- ``` diff -y -u file.txt file_2.txt``` : will do the same thing except outputs more clear informaiton.


## Find:
- find will search recursivly by default, meaning it will go through all the nested files within each sub directory as well.
- ``` find . -name '7' ``` : any files with the exact name of '7' will be found.
- ``` find . -name '*7*' ``` : any files that contain '7' in their name.
- ``` find . -type d -name '*milad*```: will only look for directories that contain "milad"
- ``` find -type f -iname "*milad*" ``` : case insensetive
- other find options: ``` find -type f/d -iname "*milad.txt" -size +100kb -mtime +3 -exec cat {} \; ``` notice the terminating \; and {} is filled with each found result.

### disk usage: du
- find the sizes of files and directories on our machine: ```du -h``` gives you a human readable output of all the dirs and files on your system along with their sizes.
- ```du -h | sort -n``` : will sort output based on the sizes


### df command: will tell us information about mounted file systems and how much space they take up and is left:
- ```df -h``` : you will see human readable infos aboutn the file system and whether they are mounted.
- find out file system info about your desktop: ``` df -h Desktop``` 

## history command:
- if you want to look for a command you have run a long time ago you can easily use this command to find it.
- you can pip the history commmand to a grep command and search for the desired command by name with RE. ```history | grep -wirl "cookie"```

## ps command: 
- Helps you inspect or view a process on your system: stands for process status
- ps by itself shows all the processes that are currently running.
- ``` ps aux ``` : will print out all the processes running with more info
- ``` ps aux | grep "process_name" ``` : very helpful command to look for a process and likely kill it.

### top command: it will show the top most memeory intensive processes.
- acts like the processes app in Mac. shows you the  memory each memory takes when running. easy way to figure out what's happening in your system.

### kill: use it to kill a process and send other signals
- ```kill -l```: this will list different signals that we can send using kill command.
- Essentially the way that we kill a ps is by theri ps id. We can find the ps id or PID using the grep and ps commands.
- ``` kill -SIGNALTERM <PID>``` : sends the selected signal to the pid chosen.
- ``` kill -KILL 543456``` : this will kill pid 543456
- Force quit and entir application or pid: ``` kill -SIGTERM/15 -SIGKILL/9 <PID>``` 

### killall command: 
- you can provide a name of the progrma to kill:
- ``` killall -KILL/-9 node``` : this will kill the node program by its name.
- it's def. less precise.

## jobs, bg, fg commands:
- you can pause jobs like ```top``` and ```fin``` that might be taking a longer time and resume them later in your terminal.
- By hitting  ```ctrl + Z```  while a job is performing, you may pause that job and store it in the ```jobs``` list.
- Then to resume a job you can use ```fg``` command to resume them in the front ground or ```bg``` to resume them in background.