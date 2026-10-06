FROM python:3.13-slim

# GDAL/GEOS/PROJ for GeoDjango — this is why Django runs in Docker
# instead of natively on Windows.
RUN apt-get update \
    && apt-get install -y --no-install-recommends gdal-bin libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .

EXPOSE 8000
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "schoolrun.asgi:application"]
