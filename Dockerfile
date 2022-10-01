FROM mysql:latest

RUN mkdir ./sql

COPY ./sql ./sql/
ENV MYSQL_ROOT_PASSWORD=mysql

VOLUME ./db_data:/var/lib/mysql