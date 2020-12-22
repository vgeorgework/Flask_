Clone this project <br />

#minikube start <br />
#eval $(minikube docker-env) <br />
#docker build -t flaskapp . <br />
<br />

Run the application by executing the command python3 app.py

The application runs on localhost:5000
NEED TO EXECUTE THESE COMMANDS AS ROOT IN SQL
SELECT host FROM mysql.user WHERE User = 'root';
CREATE USER 'root'@'%' IDENTIFIED BY 'toor';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'toor';
FLUSH PRIVILEGES;

please check:<br />
https://stackoverflow.com/questions/19101243/error-1130-hy000-host-is-not-allowed-to-connect-to-this-mysql-server <br />

https://stackoverflow.com/questions/49194719/authentication-plugin-caching-sha2-password-cannot-be-loaded <br />



CREATE TABLE users (name varchar(20), email varchar(40));
SELECT * FROM users;

To dump: kubectl exec service/mysql -- mysqldump -uroot -ptoor TEST > dump.sql


