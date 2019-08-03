FROM python:3.5
ENV PYTHONUNBUFFERED 1  

RUN mkdir /config  
ADD ./config/requirements.txt/ config/ 

RUN pip install -r /config/requirements.txt
RUN mkdir /src  

RUN apt-get update
RUN apt-get install -y netcat

ADD ./src /src
ADD ./launch_web.sh ./src

WORKDIR /src  


CMD ["./launch_web.sh"]
