FROM python:2.7.11
MAINTAINER dan.leehr@duke.edu

# Install docker client so that cwltool can call it
RUN curl -sSL https://get.docker.com/ | sh

ADD requirements.txt /opt/tf-predictions-worker/
WORKDIR /opt/tf-predictions-worker
RUN pip install -r requirements.txt

ADD . /opt/tf-predictions-worker/
ENV PATH /opt/tf-predictions-worker/:$PATH

CMD python jobsimulator.py loop
