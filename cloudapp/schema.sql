DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS device;
DROP TABLE IF EXISTS chat;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    admin BOOLEAN,
    practitioner BOOLEAN,
    patient BOOLEAN,
    engineer BOOLEAN,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE device (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_name TEXT NOT NULL,
    measurement INTEGER,
    units VARCHAR,
    patient_id INTEGER NOT NULL,
    practitioner_id INTEGER NOT NULL,
    engineer_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES user (id),
    FOREIGN KEY (practitioner_id) REFERENCES user (id),
    FOREIGN KEY (engineer_id) REFERENCES user (id)
);

CREATE TABLE communication (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_id INTEGER NOT NULL,
    recipient_id INTEGER NOT NULL,
    chat BOOLEAN,
    voice BOOLEAN,
    transcript VARCHAR NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES user (id),
    FOREIGN KEY (recipient_id) REFERENCES user (id)
);