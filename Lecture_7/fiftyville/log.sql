-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Getting details of the crime
SELECT * FROM crime_scene_reports
WHERE year = 2024 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Finding interviews from people who mentioned the theft on the same day
SELECT * FROM interviews
WHERE year = 2024 AND month = 7 AND day = 28;

-- Finding cars that exited from 10:16 to 10:25
SELECT * FROM bakery_security_logs
WHERE year = 2024 AND month = 7 AND day = 28
  AND hour = 10 AND minute BETWEEN 15 AND 25;

-- Finding names of those people
SELECT * FROM people WHERE license_plate IN (
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2024 AND month = 7 AND day = 28
    AND hour = 10 AND minute BETWEEN 15 AND 25
);

-- Finding who withdrawn money from Leggett Street ATM
SELECT * FROM atm_transactions
WHERE year = 2024 AND month = 7 AND day = 28
AND atm_location = 'Leggett Street';

-- Finding their names
SELECT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE account_number IN (
    SELECT account_number FROM atm_transactions
    WHERE year = 2024 AND month = 7 AND day = 28
    AND atm_location = 'Leggett Street'
);

-- Looking for short phone calls
SELECT * FROM phone_calls
WHERE year = 2024 AND month = 7 AND day = 28
AND duration <= 60;

-- Getting their numbers

-- caller
SELECT name, phone_number FROM people
WHERE phone_number IN (
    SELECT caller FROM phone_calls
    WHERE year = 2024 AND month = 7 AND day = 28
    AND duration <= 60
);

-- receiver
SELECT name, phone_number FROM people
WHERE phone_number IN (
    SELECT receiver FROM phone_calls
    WHERE year = 2024 AND month = 7 AND day = 28
    AND duration <= 60
);


-- Finding flight
SELECT * FROM flights
WHERE origin_airport_id = (
  SELECT id FROM airports WHERE city = 'Fiftyville'
)
AND year = 2024 AND month = 7 AND day = 29
ORDER BY hour, minute
LIMIT 1;

-- City where flight landed
SELECT city FROM airports
WHERE id = 4;

-- Who was on flight
SELECT passport_number FROM passengers
WHERE flight_id = 36;

SELECT name FROM people
WHERE passport_number IN (
    SELECT passport_number FROM passengers
    WHERE flight_id = 36
);
