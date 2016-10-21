FROM python:2.7.11
MAINTAINER dan.leehr@duke.edu

# Install docker client so that cwltool can call it
RUN curl -sSL https://get.docker.com/ | sh

ADD requirements.txt /opt/predict-tf-binding-service/
WORKDIR /opt/predict-tf-binding-service
RUN pip install -r requirements.txt

ADD . /opt/predict-tf-binding-service/
ENV PATH /opt/predict-tf-binding-service/:$PATH

CMD predict_service/main.py
