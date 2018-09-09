FROM mysql

ADD my.cnf /etc/mysql/conf.d/

ENV MYSQL_DATABASE new_schema

ADD data /custom
ADD statements/ /docker-entrypoint-initdb.d