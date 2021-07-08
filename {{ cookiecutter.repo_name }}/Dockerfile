FROM prefecthq/prefect:latest-python3.8
RUN pip --no-cache-dir install --upgrade pip wheel poetry
COPY . /app/project
WORKDIR /app/project
RUN poetry export -f requirements.txt --without-hashes --output requirements.txt
RUN pip --no-cache-dir install -r requirements.txt
RUN pip --no-cache-dir install .
