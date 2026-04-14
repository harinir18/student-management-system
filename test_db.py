import pymysql

common_passwords = ['', 'root', 'password', '1234', '12345', '123456', 'admin', 'mysql', 'test']
found = False

for p in common_passwords:
    try:
        conn = pymysql.connect(host='localhost', user='root', password=p)
        conn.close()
        print(f"SUCCESS: '{p}'")
        found = True
        break
    except pymysql.Error:
        pass

if not found:
    print("FAILED")
