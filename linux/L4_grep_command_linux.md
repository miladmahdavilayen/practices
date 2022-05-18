## How to use the "grep" command: Global Regular Expression Print

- Most basic example: searching for some text in a file:
```
grep "Jane Williams" names.txt
```

- Only look for an exact search term:
  ```
  grep -w "Jane Williams" names.txt
  ```

- Tell it to not be case sensetive
```
grep -wi "jane williams" names.txt
```

- Know the line number of where you find your match
  ```
  grep -win "jane williams" names.txt
  ```

- Additional context of where this match is found: see the lines behind and after my match
  ```
  grep -win -B 4 "jane williams" names.txt
  ## this will show 4 lines before yout match

  grep -win -A 4 "jane williams" names.txt
  ## show 4 lines after your matches

  grep -win -C 4 "jane williams" names.txt
  ## 4 lines before and after your match (meaning context of your match)
  ```

- Search for multiple files in a dir:
  ```
  grep -win "jane williams" ./*
  ## searches for all the files within the current and subdirs 
  ```

- Just search all of the text files only
  ```
  grep -win "jane williams" ./*.txt
  ```

- Do a recursive search directly on a directory
  ```
  grep -winr "jane williams" ./
  ```







