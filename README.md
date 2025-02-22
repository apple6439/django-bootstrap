## 项目概述

该系统是基于武沛齐老师的课程所编写，后端采用 Django 框架，前端使用 Bootstrap。
### 导入的组件
- echarts,toastr,jquery,bootstrap,datapicker

### 注册与登录页面

- 登录注册页面的模板使用 [此处的模版](https://github.com/HQEasy/login-page-template)。

### 错误页面

- 404 和 500 页面使用 [此处的模板](https://github.com/WuSuoV/404)。

### 功能

- **首页功能**：
  - 首页通过 ECharts 动态获取数据库中的内容，确保管理员在操作数据时首页数据会实时刷新。
  
- **模态框与消息提示**：
  - 采用模态框、AJAX 和 Toastr 实现增、删、改、查的功能。当管理员操作成功时，系统将弹出消息框进行提示。
  - datapicker组件让管理员可以选择日期。
    
- **分页功能**：
  - 导入Django中的包from django.core.paginator import Paginator来实现分页功能。

- **订单管理**：
  - 显示商品图片，支持管理员对商品进行修改等操作。

- **个人信息修改**：
  - 用户注册后将拥有一个默认头像，用户可以在个人信息界面进行头像修改。

- **动态信息显示**：
  - 应用 Cookie 和 Session 技术，动态显示不同管理员的不同信息，Cookie 的有效期设置为 7 天。

- **中间件功能**：
  - 使用中间件确保用户必须先登录才能进入系统。

- **数据校验与错误提示**：
  - modelform实现数据的校验，并对错误进行友好的显示。
- **处理上传的图片**：
  - 配置media用来接受用户传来的图片，方便后续的管理。
### 运行服务器
- python manage.py runserve --insecure。
