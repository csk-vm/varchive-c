create database vforum_db;
CREATE USER 'vforum'@'%' IDENTIFIED BY 'p@ssw0rd';
grant all privileges on vforum_db.* to 'vforum'@'%';
CREATE TABLE vforum_db.comments (submit_date DATETIME, name VARCHAR(100), comment VARCHAR(2000));
