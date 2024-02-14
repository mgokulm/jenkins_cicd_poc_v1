FROM ubuntu

MAINTAINER Gokul Methencheri <mgokulm@gmail.com>

RUN apt-get update
RUN apt-get install -y python3-pip python3.11
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

RUN apt-get install -y openjdk-8-jdk
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

WORKDIR /usr/src/app

RUN useradd jenkins -d /usr/src/app && echo "jenkins:jenkins" | chpasswd
RUN chown -R jenkins:jenkins /usr/src/app

CMD ["echo", "Hello World...! from my first docker image"]
