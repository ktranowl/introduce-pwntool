Run the following command to build and run docker:

docker build -t fast-and-smart . && docker run -p 1337:1337 -t fast-and-smart

Then connect to that file on docker:

nc localhost 1337

