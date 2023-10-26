## Addressing the Lusophone technological wishlist proposals - Task 2
### Objective of the task:
  Create a Python script to get and print the `status code` of the response of a list of URLs from a .csv file
### My approach:
  - create a generator function that accepts a csv file as a parameter, reads it and retrieves the urls from it
  - create a function `get_status_code()` that accepts a url as a parameter, makes a request to it and returns `(STATUS CODE) URL` if the request is successful and `(ERROR) URL` if a `RequestException` occurs 
  - loop over the generator function and call `get_status_code` on the urls to print the desired output
