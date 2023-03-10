# qqchatgpt
极简的qq群聊chatgpt机器人。

@机器人与其进行互动：

`@botname 世界上最高的山是哪座`

`@botname 重置对话`

# 使用

## 安装go-cqhttp

https://github.com/Mrs4s/go-cqhttp/releases

选择`0: HTTP通信`。设置好相关信息后转到第96行：

```yaml
  - http: # HTTP 通信设置
      address: 0.0.0.0:5700 # HTTP监听地址
      timeout: 0      # 反向 HTTP 超时时间, 单位秒，<5 时将被忽略
      long-polling:   # 长轮询拓展
        enabled: false       # 是否开启
        max-queue-size: 2000 # 消息队列大小，0 表示不限制队列大小，谨慎使用
      middlewares:
        <<: *default # 引用默认中间件
      post:           # 反向HTTP POST地址列表
      - url: http://127.0.0.1:5701/                # 地址
      #  secret: ''             # 密钥
        max-retries: 0         # 最大重试，0 时禁用
      #  retries-interval: 1500 # 重试时间，单位毫秒，0 时立即
      #- url:  # 地址
      #  secret: ''                  # 密钥
      #  max-retries: 10             # 最大重试，0 时禁用
      #  retries-interval: 1000      # 重试时间，单位毫秒，0 时立即
```

## 安装依赖

`pip3 install -r requirements.txt`

## 运行

填写好`main.py`中OpenAI账号相关信息后运行`main.py`和`go-cqhttp.bat`

tips:

- 获取access token: https://chat.openai.com/api/auth/session
- 获取session token: 按`F12`打开控制台，选择`应用程序`选项卡，选择`Cookie`，复制`__Secure-next-auth.session-token`的值
- 除了可以填写access token和session token进行登录以外，还可以填写邮箱和密码登录（但不支持谷歌和微软账户）。
- 要么选择使用access token和session token登录，要么使用邮箱和密码登录，不能四个全填上。

# 相关链接

https://github.com/acheong08/ChatGPT

https://docs.go-cqhttp.org/

如何注册OpenAI账号: https://sms-activate.org/cn/info/ChatGPT
