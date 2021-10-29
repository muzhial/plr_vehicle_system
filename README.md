
```
sudo mysql

use mysql;
create user 'admin'@'%' identified by '1724';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' IDENTIFIED BY '1724';
flush privileges;
```

