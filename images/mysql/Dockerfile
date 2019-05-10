FROM mysql

ADD my.cnf /etc/mysql/conf.d/
RUN chmod 0444 /etc/mysql/conf.d/my.cnf

ENV MYSQL_DATABASE qa

ADD statements/ /docker-entrypoint-initdb.d