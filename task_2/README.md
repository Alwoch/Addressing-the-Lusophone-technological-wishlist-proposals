## Addressing the Lusophone technological wishlist proposals - Task 2
### Objective of the task:
  Create a Python script to get and print the `status code` of the response of a list of URLs from a .csv file
### My Solution:
  - create a function `get_status_code()` that accepts a url as a parameter, makes a request to it and returns `(STATUS CODE) URL` if the request is successful and `(none) URL` if a connection to the url fails
  - create a function `process_csv()` that accepts a csv file as a parameter, reads it and calls the `get_status_code()` function to print the status codes and urls in the desired format  
  - call the `process_csv()` function
### set up:
1. clone the repository
   ```
   git clone https://github.com/Alwoch/Addressing-the-Lusophone-technological-wishlist-proposals
   ```
3. change to the project directory
   ```
   cd Addressing-the-Lusophone-technological-wishlist-proposals
   ```
5. enter task_2 directory
   ```
   cd task_2
   ```
7. run the file
   ```
   python3 url.py
   ```

