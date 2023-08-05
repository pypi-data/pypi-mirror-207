# Install EditAnything In Local

```shell
bash run.sh
```

## cli publish

> 发布新版本，需要增加setup.py下version版本号

```
# 构建
python setup.py sdist bdist_wheel
# 发布
twine upload dist/*
```

## cli本地安装及访问

```
# 客户端安装
pip install editanything -U
# 启动服务
editanything
# 客户端访问
http://{ip:9911}
```
