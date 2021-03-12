FROM prefecthq/prefect:latest-python3.8
RUN apt update && apt install -y git && apt clean && rm -rf /var/lib/apt/lists/*
RUN pip --no-cache-dir install --upgrade pip wheel
COPY . /app/project
WORKDIR /app/project
RUN pip --no-cache-dir install -r requirements.txt
