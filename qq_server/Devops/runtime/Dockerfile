FROM python:3.7

COPY sources.list /etc/apt/sources.list

# 设置时区
RUN set -ex \
    && apt update \
    && echo "${TIME_ZONE}" > /etc/timezone \
    && ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime

COPY requirements.txt .
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com --no-cache-dir