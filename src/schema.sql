CREATE TABLE Users_Table (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- With Book type Author/Editor field should be saved into Author column, not into Editor column
CREATE TABLE References_Table (
    id SERIAL PRIMARY KEY,
    type TEXT,
    visible BOOLEAN,
    author TEXT,
    title TEXT,
    journal TEXT,
    year TEXT,
    volume TEXT,
    publisher TEXT,
    booktitle TEXT,
    number TEXT,
    pages TEXT,
    month TEXT,
    doi TEXT,
    note TEXT,
    key TEXT,
    series TEXT,
    address TEXT,
    edition TEXT,
    url TEXT,
    editor TEXT,
    organization TEXT
);

CREATE TABLE UserReferences_Table (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    reference_id INTEGER REFERENCES References_Table(id),
    UNIQUE(user_id, reference_id)
);

CREATE TABLE Tags_Table (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    reference_id INTEGER REFERENCES References_Table(id)
);


