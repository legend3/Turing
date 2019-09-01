1、安装httplib2
cd tools/httplib2-0.11.3
python setup.py install （需要root账号安装）

2、在客户电脑上登录，然后获取登录后的Cookie

3、启动脚本
python Spider.py cookie (cookie的内容)

4、运行结束后，查看日志，日志中的res和content中是否有内容
tail -n 1000 -f logs/Spider.log