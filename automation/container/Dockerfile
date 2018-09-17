FROM ubuntu
RUN apt-get update
RUN apt-get -y upgrade 
RUN apt-get install -y git 
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN pip install flask
RUN apt-get install -y cowsay
RUN git clone https://github.com/TDB-UU/csaas.git 
WORKDIR /csaas/cowsay
EXPOSE 5000
ENV PATH="${PATH}:/usr/games/"
CMD ["python","app.py"]
