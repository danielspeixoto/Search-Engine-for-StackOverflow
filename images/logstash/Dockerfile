FROM docker.elastic.co/logstash/logstash:6.4.0

ADD . /

ENV MYSQL_HOST mysql
ENV CONNECTOR_PATH /connector/connector.jar
ENV MYSQL_PASS admin

CMD sleep 120 && logstash -f /logstash.conf