-- Create two `DROP` commands for the tables you will be creating so that you can reset the file every time you run the file.
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS candidates;

-- Create a `companies` tables that has `company_id`, `company_name`, `industry`, and `location` columns. `company_id` should be the primary key and should be set to autoincrement.
CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name STRING,
    industry STRING,
    location STRING
);
-- Create a `candidates` table that has a `candidate_id`, `first_name`, `last_name`, `email`, `years_experience`, and `primary_skill` columns. `candidate_id` should be the primary key and should be set to autoincrement.
CREATE TABLE candidates (
    candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name STRING,
    last_name STRING,
    email STRING,
    years_experience INTEGER,
    primary_skill STRING
);

-- Before you run the tests, make sure you run `sqlite3 tech_talent.db < tech_talent.sql` in the terminal to update the database. The tests may fail if you forget to run the file before running the tests!

-- Insert a set of values into the `companies` and `candidates` tables using the `INSERT INTO` command.
INSERT INTO companies (company_name, industry, location) VALUES
    ('TechCorp', 'Software', 'San Francisco'),
    ('DataDynamics', 'Data Analytics', 'Boston'),
    ('CloudNine', 'Cloud Computing', 'Seattle');

INSERT INTO candidates (first_name, last_name, email, years_experience, primary_skill) VALUES
    ('John', 'Smith', 'john.smith@email.com', 5, 'Python'),
    ('Sarah', 'Johnson', 'sarah.j@email.com', 3, 'Data Science'),
    ('Michael', 'Lee', 'michael.lee@email.com', 7, 'Cloud Architecture'),
    ('Emma', 'Wilson', 'emma.w@email.com', 2, 'Frontend Development'),
    ('James', 'Brown', 'james.b@email.com', 4, 'Python');

-- Select all the values in the `companies` and `candidates` tables and print them to the terminal.
SELECT "Company Table";
SELECT * FROM companies;
SELECT "";
SELECT "Candidate Table";
SELECT * FROM candidates;

-- Using a `SELECT` command, print out only the `candidates` that have a `primary_skill` of `"Python"`.
SELECT "";
SELECT "Python Developers";
SELECT * FROM candidates WHERE primary_skill = "Python";

-- Using a `SELECT` command, print out only the `companies` that are in an `industry` of `"Software"`.
SELECT "";
SELECT "Software Companies";
SELECT * FROM companies WHERE industry = "Software";

-- Using a `SELECT` command, print out only those `candidates` that have more than 3 years of experience.
SELECT "";
SELECT "Candidates with more than 3 years of experience";
SELECT * FROM candidates WHERE years_experience > 3;

-- Uh oh! John Smith's email is incorrect. Update John's email to the correct value of `john.smith@gmail.com`.
UPDATE candidates SET email = "john.smith@gmail.com" WHERE candidate_id = 1;
SELECT "";
SELECT "Updated Email for John Smith";
SELECT * FROM candidates WHERE candidate_id = 1;

-- Techcorp has moved office locations. They are now based on New York. Update the `location` of Techcorp to reflect this change.
UPDATE companies
SET location = 'New York'
WHERE company_name = 'TechCorp';

SELECT "";
SELECT "Updated Location for TechCorp";
SELECT * FROM companies WHERE company_name = 'TechCorp';

-- The candidate with a `candidate_id` of 5 wants to update their `primary_skill` to be `Python, SQL`. 
UPDATE candidates
SET primary_skill = 'Python, SQL'
WHERE candidate_id = 5;
SELECT "";
SELECT "Updated Primary Skill for James Brown";
SELECT * FROM candidates WHERE candidate_id = 5;

-- `CloudNine` has canceled their contract with the company. Delete this row from the `companies` table.
DELETE FROM companies WHERE company_name = "CloudNine";
SELECT "";
SELECT "Deleted CloudNine Company";
SELECT * FROM companies;

-- Since this company has been removed, delete all `candidates` that have a `primary_skill` of `"Cloud Architecture"`. 
DELETE FROM candidates WHERE primary_skill = "Cloud Architecture";

-- Print out the remaining values in each table.
SELECT "";
SELECT "Deleted Michael Lee From Candidates";
SELECT * FROM candidates;