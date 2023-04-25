# kinsa-docker-practice
This repo represents a project to be dockerized. We have 1) a python script to run in Docker ( job/hello_world.py) and 2) a requirements.txt file that defines our python environment. We are using a Python 3.7 environment.

hello_world.py will import two of the libraries in our requirements.txt and print the versions. It also accepts an optional command-line argument `var`, which it will also print if found.

<details>
  <summary>Spoilers for the hands-section</summary>
  <br>
  
  1. ```touch Dockerfile``` -- creates an empty Dockerfile
  
  2. Dockerfile
  ```
FROM python:3.7
RUN apt-get update -yqq \ 
    && apt-get upgrade -yqq \ 
    && apt-get install -yqq --no-install-recommends supervisor \ 
    && apt-get -y autoremove \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

RUN rm -rf /root/.cache

COPY job /job
WORKDIR /job
CMD ["python", "hello_world.py", "--var", "foo"]
```
3. ```docker build --platform linux/amd64 -t demo``` -- platform arg is needed for M1/M2 chip compatibility
4. ```docker run demo``` -- runs CMD from Dockerfile
5. ```docker run -it demo bash``` -- `-it`=interactive mode -- ```docker run -it <image>:<tag> <cmd>```
6. ```python hello_world.py --var bar```
</details>
