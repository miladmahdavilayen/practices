## How to create copy move rename and delete files from Terminal

- How to create a directoy
  ```
  mkdir testdir/
  ```

- How to create a file in a directory:
  ```
  touch test.txt
  open test.txt
  ```

- How to copy a file in terminal:
  ```
  cp text.txt ../other_dir/copy_file.txt
  ```

- How to move or rename a file:
  ```
  mv test.txt new_name.txt
  ```

- How to remove a file or a directory
  ```
  rm test.txt
  rmdir testdir/  # this will only delete an empty dir
  rm -r testdir/   # this will delete a dir with all the files within
  ```

- How to cp or mv a whole dire with all the fils within
    ```
    cp -r testdir/ copydir/
    mv -r testdir/ mvdir/
    ```

- Force deletion of a directory
  ```
  rm -rf testdir/
  ```
