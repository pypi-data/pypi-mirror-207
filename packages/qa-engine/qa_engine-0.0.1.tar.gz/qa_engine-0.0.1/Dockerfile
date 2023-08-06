FROM python:3.9.16
WORKDIR /app
COPY Shanghai /usr/share/zoneinfo/Asia/Shanghai
RUN echo "Asia/Shanghai" > /etc/timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN apt-get update -y
RUN apt-get install curl -y

COPY . .
RUN pip install -e ombot_utils -i https://pypi.douban.com/simple/

RUN pip install -e .

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyarmor==7.0.1

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

RUN mkdir source/
COPY . ./source/


RUN wget https://airesources.oss-cn-hangzhou.aliyuncs.com/zl/pyarmor.zip
RUN mv pyarmor.zip /root/
RUN unzip /root/pyarmor.zip -d /root

RUN pyarmor licenses --expired 2099-12-01 r001

RUN pyarmor obfuscate --with-license licenses/r001/license.lic --src="./source" -r --output=./ wsgi.py

#RUN pyarmor obfuscate --with-license licenses/r001/license.lic --src="./source" -r --output=./ run.py
#
#RUN rm -rf source


ENV LANG C.UTF-8

#CMD ["uvicorn", "vql_cluster.main:app", "--host", "0.0.0.0", "--port", "8000",  "--workers", "1"]
CMD ["python", "wsgi.py"]