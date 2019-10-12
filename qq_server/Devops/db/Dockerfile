FROM mysql

COPY sources.list /etc/apt/sources.list

# 设置时区
RUN set -ex \
    && apt update \
    && echo "${TIME_ZONE}" > /etc/timezone \
    && ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime

COPY db.cnf /etc/mysql/conf.d/

RUN chmod 664 /etc/mysql/conf.d/db.cnf