FROM python:3.11-slim

RUN apt-get update && apt-get install -y wget unzip \
    && wget https://releases.hashicorp.com/terraform/1.8.4/terraform_1.8.4_linux_amd64.zip \
    && unzip terraform_1.8.4_linux_amd64.zip -d /usr/local/bin \
    && rm terraform_1.8.4_linux_amd64.zip \
    && terraform -version

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]