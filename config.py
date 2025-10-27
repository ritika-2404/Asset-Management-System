import cx_Oracle

DSN = cx_Oracle.makedsn("localhost", 1521, service_name="ORCLPDB1")
CONN = cx_Oracle.connect(user="username", password="password", dsn=DSN)
