FROM python:3.12-slim

# 環境変数
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# 🧩 MySQLclient ビルドに必要なパッケージを追加！
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# requirements.txtをコピーしてインストール
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# コードをコピー
COPY . /code/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
