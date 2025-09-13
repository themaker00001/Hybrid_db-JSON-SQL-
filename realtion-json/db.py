from SQL import SQLEngine

db=SQLEngine()

db.execute("CREATE TABLE USERS (id INT, name TEXT, payload JSON)")
db.execute("INSERT INTO USERS VALUES (1,'Vaibhav','{\"lives\":\"in delhi\"}')") 