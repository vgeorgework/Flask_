FROM mysql:latest
#add db TEST
ENV MYSQL_DATABASE TEST
COPY ./scripts/ /docker-entrypoint-initdb.d/
EXPOSE 3306
