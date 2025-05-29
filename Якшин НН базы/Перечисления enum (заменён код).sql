CREATE TYPE request_state AS ENUM (
    'created',
    'in_progress',
    'completed',
    'rejected'
);

CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    title VARCHAR(30),
    status request_state
);

INSERT INTO requests(title, status)
VALUES ('Request 1', 'created');