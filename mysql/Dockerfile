FROM mysql:5.7
COPY dump_mysql.sql /mysql/setup.sql
RUN set -e && service mysql start && mysql -u root -e "CREATE DATABASE vulgairedev" && mysql < /mysql/setup.sql && service mysql stop
