FROM mysql/mysql-server:latest
MAINTAINER Al Burns
RUN yum install -y vim
EXPOSE 3306
ENV MYSQL_USER=mysql \
MYSQL_PASSWORD=Viapjor5 \
MYSQL_DATABASE=db
ENTRYPOINT ["/entrypoint.sh"]
CMD ["mysqld"]
