FROM  ubuntu

# Install packages
RUN apt-get update && \
apt-get install -y curl

COPY questions.json /
COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]