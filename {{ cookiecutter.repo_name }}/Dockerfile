FROM prefecthq/prefect:0.13.8-python3.8
RUN apt update && apt install -y git && apt clean && rm -rf /var/lib/apt/lists/*
RUN pip --no-cache-dir install --upgrade pip wheel
WORKDIR /app/project
COPY requirements.txt /app/project/
RUN pip --no-cache-dir install -r requirements.txt
COPY . /app/project
RUN pip --no-cache-dir install -r requirements.self
