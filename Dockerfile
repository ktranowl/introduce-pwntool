# docker build -t fast-and-smart . && docker run -p 1337:1337 -t fast-and-smart

FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install socat -y
RUN apt-get install python3 -y
COPY game.py game.py

ARG FLAG=flag{hihi_flag_fake_ne}
RUN echo "$FLAG" > /flag.txt

EXPOSE 1337

CMD ["socat", "-v", "tcp-listen:1337,reuseaddr,fork", "EXEC:'./game.py',stderr"]
