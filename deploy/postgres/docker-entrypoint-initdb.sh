#!/bin/bash

set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
CREATE TABLE  IF NOT EXISTS site_metrics (
    kafka_id int PRIMARY KEY,
    code varchar(10),
    request_time varchar(40),
    method varchar(10),
    content_type varchar(90)
);
EOSQL

exec "$@"


