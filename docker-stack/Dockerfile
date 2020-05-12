FROM python:3.6-alpine
MAINTAINER allwinchristopherj@gmail.com
WORKDIR /opt/data
RUN pip3 install flask && pip3 install redis
CMD ["python3", "docker-compose-webapp.py"]
