FROM ubuntu:12.04
MAINTAINER YungSang "yungsang@gmail.com"

# http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list

RUN apt-get update && apt-get -y install git python-pip mongodb-org

RUN git clone https://github.com/YungSang/miita.git -b docker

WORKDIR /miita

RUN pip install -r requirements.txt

# Expose the Miita port
EXPOSE 5000

# Add VOLUMEs to allow backup of logs and databases
# VOLUME ["/var/log/mongodb", "/var/lib/mongodb"]

CMD ["./startup.sh"]
