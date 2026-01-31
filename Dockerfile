# 1.指定鏡像檔
FROM python:3.11-slim

# 2.環境變數
# 禁止產出.pyc編譯檔
ENV PYTHONDONTWRITEBYTECODE=1
# Log即使輸出(stdout / stderr 不經緩衝，立刻輸出)g
ENV PYTHONUNBUFFERED=1
# ENV SECRET_KEY=${DJANGO_SECRET_KEY}
# ENV POSTGRESQL_DB_NAME=${POSTGRESQL_DB_NAME}
# ENV POSTGRESQL_DB_USER=${POSTGRESQL_DB_USER}
# ENV POSTGRESQL_DB_PASSWORD=${POSTGRESQL_DB_PASSWORD}
# ENV POSTGRESQL_DB_HOST=${POSTGRESQL_DB_HOST}

# 3.設定工作目錄
WORKDIR /app

# 4.複製專案 -> container工作目錄
COPY requirements.txt .

# 5.pip更新 & 安裝相關套件
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 6.複製專案
COPY . .

# 7.執行DB腳本
# RUN python manage.py migrate

# 8.部署靜態資源
# --noinput, 使用預設行為(yes)
RUN python manage.py collectstatic --noinput

# RUN python manage.py migrate

# 9.(使用docker-compose時，無需使用) 開放8080連接至container
EXPOSE 8080

# 10.預設不啟動 (設定當run images自動執行命令)
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "core.wsgi:application"]