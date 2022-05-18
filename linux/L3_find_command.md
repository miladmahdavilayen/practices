## How to use the "find" command in Linux or Mac

- Look at the manual page of the "find" command:
  ```
  man find
  ```

- Look for all the files within a dir
  ```
  find .
  find testdir/
  ```

- Filtering out some of the results:
  ```
  find . -type d    ## if I wanted to find all of the directories and exclude the files within the current dir

  find . -type f    ## returns all of the files and not dirs
  ```

- Look for a specific name or just a part of the name that you remember:
  ```
  find . -type f -name "test1.txt"   ## if I remember the whole name
  
  find . -type f -name "tes*.txt"   ## only recall a part of the name of the file I'm looking for

  find . -type f -iname "tes*"   # looks for all the files with those letters and insensetive to letter cases

  find . -type f -iname "*.txt"
  ```

- Find the files that were modified in the last X minutes:
  ```
  find . -type f -mmin -10

  find . -type f -mmin +1 -mmin -10   # more thatn one min ago and less than 10 min ago

  find . -type f -mtime -20   ## less or more than 20 DAYs ago
  ```
  
- Find and search by file sizes:
  ```
  find . -size +5M   # files that are over 5 mbs
  +5K   # over 5 kbs
  +5G  # over 5 Gbs
  ```

- Find all the files that are empty
  ```
  find . -empty
  ```

- How to search based on permissions:
  ```
  find . -perm 777  ## search for a file with specific permission 777 is a read write and execute permission type you gotta research and learn
  ```

- Let's see how to change permissions using find:
  ```
  find website_demo -exec chown milad:www-data {} +   ## first we change the owner of the websitte to milad

  find website_demo -type d -exec chmod 775 {} +   ## change permission of all directories or files to 775
  ```

- How to delete all the files in the current directory with the same specific extension:
  ```
  find . -type f -name "*.jpg"
  ## this will return all the files with jpg extension within the current directory and all its subdirectories. It could be dangerous to use rm here.

  find . -type f -name "*.jpg" -maxdepth 1 -exec rm {} +
  ## this will first find all the jpg files within only the current dir and removes them after
  ```





