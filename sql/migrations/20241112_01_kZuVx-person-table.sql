-- person table
-- depends: 

BEGIN;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS "person" (
  "uuid" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "name" VARCHAR(48),
  "title" VARCHAR(164),
  "ts_created" INT NOT NULL DEFAULT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP),
  "ts_born" INT,
  "ts_updated" INT NOT NULL DEFAULT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP)
);

COMMIT;