## MySQL config

```bash
sudo mysql

use mysql;
create user 'admin'@'%' identified by '1724';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' IDENTIFIED BY '1724';
flush privileges;
```

## pipeline

1. 登陆

```
/admin/login  [GET, POST]

form:
{
    'username':,
    'password':
}
```

2. get user

```
/admin/user/data  [GET]

args
```

3. add user

```
/admin/user/save  [POST]

json:
{
    'roleIds': '2',
    'username': 'test',
    'realName': 'test',
    'password': 'test'
}
```

```
/admin/user/enable  [PUT]

json:
{
    'userId': 9
}
```

4. power

```
/admin/power/data  [GET]


/admin/power/save  [POST]
json:
{
    'powerCode': 'admin:measure:main',
    'powerName': 'measure data',
    'powerUrl': '/admin/measure/'
}

{
    "powerCode": "admin:measure:add",
    "powerName": "add measure data"
}
```

5. power and role update

```
/admin/role/saveRolePower  [PUT]
json:
{
    "powerIds": "13,3,4,9,18,48",
    "roleId": 2
}
{
    "powerIds": "48",
    "roleId": 3
}
```

5. measure data

```
/admin/measure/save  [POST]
json:
{
    "coordXyz": "0.12, 0.123, 0.1231",
    "measureAddress": "camera:ip1.1.1.1",
    "measureStatus": 1,
    "measureInfo": "nothing"
}
```

```
bulk_insert

/admin/measure/save [POST]
json:
{
    "data": [
        {"coord_xyz": "0.12 0.123 0.1231", "measure_address": "folder1", "measure_time": "2022-03-12 12:12:00"},
        {"coord_xyz": "0.02 0.923 0.81", "measure_address": "folder1", "measure_time": "2022-03-12 12:56:00"},
    ]
}

```
