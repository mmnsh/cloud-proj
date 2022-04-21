# pull the official base image
FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000

RUN apk add --no-cache bash
COPY ./command.sh /usr/src/app
RUN chmod -R 777 command.sh
CMD ["/usr/src/app/command.sh"]