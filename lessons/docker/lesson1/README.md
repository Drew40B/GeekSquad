# Lesson 1

Use Docker container for python dev

## Steps

### Download code from git

`git clone https://github.com/Drew40B/GeekSquad.git`

### Download and test python image

- `docker run -it --rm --net=host  python /bin/bash`
- `python` _[verify python running within container]_

### Run python container and mount local code folder

- `docker run -it --rm --net=host -v ${PWD}/src:/code python /bin/bash`
- `cd /code`
- `ls -l   (Should see same files as ./src folder)`
- `pip install debugpy`
- `python -m debugpy --listen localhost:3000 --wait-for-client hello.py`
- `From within vs code put a breakpoint on line 1`
- debug -> Python Remote

### Automate the above steps using docker build

 `docker docker build  --network=host --tag pythondev:latest .` **<-- make sure you get the persiod**
