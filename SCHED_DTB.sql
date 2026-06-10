CREATE TABLE User (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE Host (
    id SERIAL PRIMARY KEY
);

CREATE TABLE Attendee (
    id SERIAL PRIMARY KEY
);

CREATE TABLE Calendar (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    period TSRANGE
);

CREATE TABLE Create_Schedule (
    hostID SERIAL PRIMARY KEY REFERENCES Host(id),
    calendarID SERIAL PRIMARY KEY REFERENCES  Calendar(id),
    time_create TIME
);

CREATE TABLE Vote (
    attendeeID SERIAL PRIMARY KEY REFERENCES Attendee(id),
    calendarID SERIAL PRIMARY KEY REFERENCES Calendar(id)
);

