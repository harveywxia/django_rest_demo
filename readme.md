xiawei
rest123456
## 使用方法
### 依赖
参见根目录requirment.txt
### 安装
安装依赖环境：
``` bash
pip install -r requirment.txt
```
### 运行
#### 数据库设置
初始化，命令会建立apps所必须的库表
``` bash
$ python manage.py migrate
```
若修改models，执行以下命令：
```
$ python manage.py makemigrations api
```
#### 创建管理员用户

``` python
$ pyhton manage.py createsuperuser
```

#### 运行代码
``` bash
$ python manage.py runserver
````
或直接通过pycharm运行
