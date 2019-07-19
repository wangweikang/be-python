FROM python:3.6

# 创建工作目录
RUN mkdir /mysite  

#设置工作目录
WORKDIR /mysite

#将当前目录加入到工作目录中
ADD . /mysite
RUN pip3 install -i https://pypi.douban.com/simple -r requirements.txt

#对外暴露端口
EXPOSE 8080 8000

#设置环境变量
ENV SPIDER=/mysite