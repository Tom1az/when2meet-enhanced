-- Sample data for SCHED_DB (PostgreSQL)
-- Run after SCHED_DTB.sql:
--   psql -U postgres -d SCHED_DB -f SCHED_DTB_sample_data.sql

-- Reset sample rows (optional)
TRUNCATE Vote, Create_Schedule, Calendar, Attendee, Host, Web_User RESTART IDENTITY CASCADE;

-- 1. Users
INSERT INTO Web_User (id, username, password) OVERRIDING SYSTEM VALUE VALUES
(1, 'alice_host',   'password123'),
(2, 'bob_host',     'password123'),
(3, 'carol_guest',  'password123'),
(4, 'dave_guest',   'password123'),
(5, 'eve_guest',    'password123');

-- 2. Hosts & Attendees (id must match Web_User.id)
INSERT INTO Host (id) OVERRIDING SYSTEM VALUE VALUES (1), (2);

INSERT INTO Attendee (id) OVERRIDING SYSTEM VALUE VALUES (3), (4), (5);

-- 3. Calendars
INSERT INTO Calendar (id, name, period) OVERRIDING SYSTEM VALUE VALUES
(1, 'Team Standup Week',  tsrange('2026-06-09 09:00', '2026-06-13 17:00')),
(2, 'Project Kickoff',    tsrange('2026-06-16 13:00', '2026-06-20 18:00')),
(3, 'Study Group',        tsrange('2026-06-10 08:00', '2026-06-12 20:00'));

-- 4. Host creates schedules
INSERT INTO Create_Schedule (hostID, calendarID, time_create) OVERRIDING SYSTEM VALUE VALUES
(1, 1, '2026-06-01 10:00:00'),
(1, 3, '2026-06-02 14:30:00'),
(2, 2, '2026-06-03 09:15:00');

-- 5. Attendees vote on calendars
INSERT INTO Vote (attendeeID, calendarID) OVERRIDING SYSTEM VALUE VALUES
(3, 1),
(4, 1),
(5, 1),
(3, 2),
(4, 3),
(5, 3);

-- Verify
SELECT 'Web_User' AS table_name, COUNT(*) AS row_count FROM Web_User
UNION ALL SELECT 'Host',       COUNT(*) FROM Host
UNION ALL SELECT 'Attendee',   COUNT(*) FROM Attendee
UNION ALL SELECT 'Calendar',   COUNT(*) FROM Calendar
UNION ALL SELECT 'Create_Schedule', COUNT(*) FROM Create_Schedule
UNION ALL SELECT 'Vote',       COUNT(*) FROM Vote;
