# python base Image
FROM python:3.11.1

# コンテナ内作業ディレクトリ
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app/ .
