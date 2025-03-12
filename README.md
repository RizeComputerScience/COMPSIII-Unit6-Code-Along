# COMPS III: Unit 5 Code Along

You are working for a recruiting firm called Tech Talent and need to create a database that allows the company to store information about (1) companies that use your service and (2) candidates that you have sourced. This week we will be creating, reading, updating, and deleting values stored in companies and candidates tables in order to begin building out our database functionality. The values that will be stored in each of these tables are represented in the entity diagrams shown below.

![Companies and Candidates ER Diagrams](./Recruiting_W1.png)

By the end of this code along, our recruiting firm will be able to store information about all of the companies and candidates that use the service.

> **NOTE** This week’s code utilizes SQLite to implement the commands in our SQL file. Directions for how to install will vary based on your operating system
> - **Windows**: [Follow these directions](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm).
> - **Apple**: Nothing at all! SQLite comes installed on all Macs. If for some reason you don’t have it, you can download it using [Homebrew](https://formulae.brew.sh/formula/sqlite).
> - **Linux**: Follow [these directions](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-sqlite-on-ubuntu-20-04).

### Running Your Code File

To run SQL in your terminal using SQLite3, use the following command:

```bash
sqlite3 tech_talent.db < tech_talent.sql
```

## Steps
1. Create a database file called `tech_talent.db`.
2. The rest of this code along should be done in the `tech_talent.sql` file. Create two `DROP` commands for the tables you will be creating so that you can reset the file every time you run the file.
3. Create a `companies` tables that has `company_id`, `company_name`, `industry`, and `location` columns. `company_id` should be the primary key and should be set to autoincrement.
4. Create a `candidates` table that has a `candidate_id`, `first_name`, `last_name`, `email`, `years_experience`, and `primary_skill` columns. `candidate_id` should be the primary key and should be set to autoincrement.
5. Run your code file to create the table.
6. Run the tests! The tests `test_companies_table_exists` and `test_candidates_table_exists` should now be passing.
7. Insert the following values into the `companies` table using the `INSERT INTO` command.

| `company_name` | `industry` | `location` |
| -------------- | ---------- | ---------- |
| TechCorp | Software | San Francisco |
| DataDynamics | Data Analytics | Boston |
| CloudNine | Cloud Computing | Seattle |

8. Insert the following values into the `candidates` table using the `INSERT INTO` command.

| `first_name` | `last_name` | `email` | `years_experience` | `primary_skill` |
| ------------ | ----------- | ------- | ------------------ | --------------- |
| John | Smith | john.smith@email.com | 5 | Python |
| Sarah | Johnson | sarah.j@email.com | 3 | Data Science |
| Michael | Lee | michael.lee@email.com | 7 | Cloud Architecture |
| Emma | Wilson | emma.w@email.com | 2 | Frontend Development |
| James | Brown | james.b@email.com | 4 | Python |

9. Run your code file using the same command as step 4 `sqlite3 tech_talent.db < tech_talent.sql`. 
10. Run the tests! `test_companies_table_columns` and `test_candidates_table_columns` should now be passing.
11. Select all the values in the `companies` and `candidates` tables and print them to the terminal.
12. Using a `SELECT` command, print out only the `candidates` that have a `primary_skill` of `"Python"`.
10. Using a `SELECT` command, print out only the `companies` that are in an `industry` of `"Software"`.
11. Using a `SELECT` command, print out only those `candidates` that have more than 3 years of experience.
12. Uh oh! John Smith's email is incorrect. Update John's email to the correct value of `john.smith@gmail.com`. Run your code and verify that it has been updated.
13. Run the tests! The `test_john_email_update` test should now be passing.
14. Techcorp has moved office locations. They are now based on New York. Update the `location` of Techcorp to reflect this change. Run your code and verify that it has been updated.
15. Run the tests! The `test_techcorp_location_update` test should now be passing.
16. The candidate with a `candidate_id` of 5 wants to update their `primary_skill` to be `Python, SQL`. Run your code and verify that it has been updated.
17. Run the tests! The `test_candidateid_update` test should now be passing.
18. `CloudNine` has canceled their contract with the company. Delete this row from the `companies` table. Run your code and verify that it has been updated.
19. Run the tests! The `test_deleted_cloudnice` test should now be passing.
20. Since this company has been removed, delete all `candidates` that have a `primary_skill` of `"Cloud Architecture"`. Run your code and verify that it has been updated.
21. Run the tests! The `test_deleted_candidates` test should now be passing.
22. Print out the remaining values in each table.