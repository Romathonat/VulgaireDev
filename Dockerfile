FROM python:3.5  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /config  
ADD ./config/requirements.txt/ config/ 
RUN pip install -r /config/requirements.txt
RUN mkdir /src  
RUN export GITHUB_PASSWORD=Souirnarlor45
WORKDIR /src  

