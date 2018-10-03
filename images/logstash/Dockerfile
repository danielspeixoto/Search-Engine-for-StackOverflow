FROM docker.elastic.co/logstash/logstash:6.4.0

ENV MYSQL_HOST mysql
ENV CONNECTOR_PATH /connector/connector.jar
ENV MYSQL_PASS admin

ADD . /

CMD /scripts/start.sh