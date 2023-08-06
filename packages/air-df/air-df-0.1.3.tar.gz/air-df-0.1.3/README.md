## base_handler -- tornado handler 基类

>主要提供参数检查，并初始化get、post、delete、option等方法

## plugins -- 插件集合

#### 1. `OrmClient` -- Sqlalchemy管理器

>支持类别：Mysql、Sqlserver、Postgresql。\_\_enter__ 方法返回session 对象


#### 2. `MongoClient` -- MongoDB管理器

>MongoDB 连接管理器

#### 3. `RedisClient` -- Redis管理器

>Redis管理器，重写push、set（支持自定义文件夹）、get、delete方法

#### 4. `LocalFaker` -- 随机数据生成工具

>基于Faker，提供姓名、地址、邮箱、银行、公司、职业、md5、bool、密码、手机、身份证生成工具

#### 5. `AlchemyEncoder` -- sqlalchemy 模型转字典
>sqlalchemy 模型转字典，特殊类型处理类，使用方式
    json.dumps(dict, cls=AlchemyEncoder)

#### 6.`CryptoHelper` -- 加密工具

>提供md5加密、aes加密、aes解密

#### 7.`Tools` -- 常用工具汇总
>1. `get_birth_from`
>2. `make_captcha`
>3. `transform_unix`
>4. `transfrom_datetime`
>5. `make_logger`
>6. `get_excel_data`
>7. `save_xls`
>8. `excel_color`

        
        
        