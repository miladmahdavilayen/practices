## How to use the CURL command

### Allows us to querry urls from the cmd; we can post form data; authenticate users and save responses to files in our system

- Run a simple curl command:
  ```
  curl https://coreyms.com
  ```
  The response that we get back will be all of the html and scripts and everything in text form.

- Test RestAPIs; let's try a route that returns json reponse:
  ```
  curl http://api.plos.org/search?q=title:DNA
  ```

- See the response header and other information in the rest api:
  ```
  curl -i https://api.plos.org/search?q=title:DNA
  ```

- Post, update or delete information using the -d option:
  ```
  curl -d "first=milad"&last=mahdavi" https://sample_website.com/methods

  ```

- How to download a response with curl:
  ```
  curl -o test.jpg https://url-to-image.com
  ```
