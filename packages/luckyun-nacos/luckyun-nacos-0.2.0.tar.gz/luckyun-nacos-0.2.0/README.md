## luckyun-nacos

nacos接入工具类

## 安装

```
pip install luckyun-nacos
```

## 用法

```

 from luckyun_nacos import Client

 SERVER_ADDRESSES = "http://127.0.0.1:31000"
 NAMESPACE = "dev_env"
 SERVICE_NAME = "python_service"
 SERVICE_IP = "127.0.0.1"
 SERVICE_PORT = 5000

 DATA_ID = "common-dev.yml"
 GROUP = "DEFAULT_GROUP"

 # 注册进nacos服务

 client = Client(SERVER_ADDRESSES, namespace=NAMESPACE,
                        service_name=SERVICE_NAME, service_ip=SERVICE_IP, service_port=SERVICE_PORT,heartbeat_rate=5)

 client.add_instance()

 # 获取配置

 client = Client(SERVER_ADDRESSES, namespace=NAMESPACE,
                        service_name=SERVICE_NAME, service_ip=SERVICE_IP, service_port=SERVICE_PORT)

```
