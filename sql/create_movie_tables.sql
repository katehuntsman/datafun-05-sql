-- database: ../movies.db
CREATE TABLE directors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_year INTEGER
);

CREATE TABLE ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    director_id INTEGER,
    movie_title TEXT NOT NULL,
    rating REAL CHECK (rating >= 0 AND rating <= 10),
    FOREIGN KEY (director_id) REFERENCES directors(id)
);