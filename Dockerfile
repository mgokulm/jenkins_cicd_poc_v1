FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

MAINTAINER Gokul Methencheri <mgokulm@gmail.com>

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk
RUN apt-get install -y python3-pip python3.7
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

WORKDIR /usr/src/app

RUN useradd jenkins -d /usr/src/app && echo "jenkins:jenkins" | chpasswd
RUN chown -R jenkins:jenkins /usr/src/app