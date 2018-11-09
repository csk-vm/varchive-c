FROM mysql:5.6

COPY ./create_table.sql /docker-entrypoint-initdb.d/
COPY ./my.cnf /etc/mysql/conf.d/