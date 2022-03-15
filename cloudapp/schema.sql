DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS device;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    role TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE device (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_name TEXT NOT NULL,
    measurement INTEGER,
    units VARCHAR,
    patient_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES user (id)
);