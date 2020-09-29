FROM prefecthq/prefect:0.13.8-python3.8
RUN pip --no-cache-dir install --upgrade pip wheel
COPY . /app/project
WORKDIR /app/project
RUN pip --no-cache-dir install -r requirements.txt
