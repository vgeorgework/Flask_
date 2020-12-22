Clone this project <br />

#minikube start <br />
#eval $(minikube docker-env) <br />
#docker build -t flaskapp . <br />
<br />

Run the application by executing the command python3 app.py

The application runs on localhost:5000

CREATE TABLE users (name varchar(20), email varchar(40));
SELECT * FROM users;

To dump: kubectl exec service/mysql -- mysqldump -uroot -ptoor TEST > dump.sql


