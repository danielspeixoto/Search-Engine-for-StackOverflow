FROM mysql

ADD my.cnf /etc/mysql/conf.d/

ENV MYSQL_DATABASE qa

ADD statements/ /docker-entrypoint-initdb.d