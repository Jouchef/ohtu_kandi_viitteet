CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
);
CREATE TABLE References (
    id SERIAL PRIMARY KEY,
    author TEXT,
    title TEXT,
    year INTEGER,
    booktitle TEXT,
    journal TEXT,
    volume INTEGER,
    pages TEXT,
    publisher TEXT,
    type TEXT,
);
CREATE TABLE UserReferences (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    reference_id INTEGER REFERENCES References(id),
    UNIQUE(user_id, reference_id)
);
CREATE TABLE Tags (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    reference_id INTEGER REFERENCES References(id)
);


