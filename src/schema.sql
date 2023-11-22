CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE "References" (
    id SERIAL PRIMARY KEY,
    type TEXT,
    visible BOOLEAN,
    author TEXT,
    title TEXT,
    journal TEXT,
    year INTEGER,
    volume TEXT,
    publisher TEXT,
    booktitle TEXT,
    
);

CREATE TABLE UserReferences (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    reference_id INTEGER REFERENCES "References"(id),
    UNIQUE(user_id, reference_id)
);

CREATE TABLE Tags (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    reference_id INTEGER REFERENCES "References"(id)
);


