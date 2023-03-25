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

填写好`handlemsg.py`中的api key后运行`main.py`和`go-cqhttp.bat`。

# 相关链接

https://github.com/acheong08/ChatGPT

https://docs.go-cqhttp.org/

https://platform.openai.com/docs/api-reference/chat/create?lang=python

如何注册OpenAI账号: https://sms-activate.org/cn/info/ChatGPT
