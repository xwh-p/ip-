# Django


## MySQL驱动
- 驱动作用
    - 连接
    - 统一操作
        - IDL
- 驱动
    - mysqlclient
        - python2， python3， 不用额外声明驱动初始化
        - 对mysql安装有要求
    - mysql-python
        - python2 支持很好
        - python3 装不上，有小毛病
    - pymysql
        - python2， python3都支持
        - 支持伪装成 mysqldb 驱动器
        
        
### 后台管理
- 快速集成服务端的总的管理


### 端
- 电商
    - 所有商品是直营的
        - 服务器开发端（商家端）
            - 商品
            - 订单
            - 用户
        - 用户端
            - 操作
    - 商品是来自商家的（第三方）
        - 服务器开发端（平台）
            - 商家
            - 用户
            - 商品
            - 订单
            - 评价
        - 商家端
            - 商品
        - 用户端
            - 购买
            - 收藏
            - 评论

### Django内置的权限
- 主表
    - 用户
    - 权限
    - 组
- 关系表
    - 用户权限表
        - 多对多的关系表
        - 用户id
        - 权限id
    - 用户组
        - 多对多的关系表
        - 用户id
        - 组id
    - 组权限
        - 多对多关系表
        - 组id
        - 权限id
- 用户权限
    - 用户权限表
    - 用户所属组，组的权限
    
### 视图函数
- FBV
    - function base view
- CBV
    - class  base view
    - 继承系统的View
    
#### CBV 执行流程
- as_view()
    - 预校验，校验参数合法不合法
    - 分发请求
        - 根据请求方法
        - 根据请求 去你的类中获取请求的方法 对应的函数
            - 获取到了函数的句柄
                - 调用你的函数
            - 没有获取到，使用NotAllowed这个函数进行填充
                - 调用这个不允许函数

    
