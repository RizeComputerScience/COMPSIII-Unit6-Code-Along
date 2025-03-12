from tech_talent import *
import sqlite3
import os

# Test that the companies table has been created
def test_companies_table_exists():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='companies';")
    result = cursor.fetchone()
    assert result is not None
    connection.close()

# Test that the candidates table has been created
def test_candidates_table_exists():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='candidates';")
    result = cursor.fetchone()
    assert result is not None
    connection.close()

# Test that the companies table has the correct columns
def test_companies_table_columns():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(companies);")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    assert 'company_id' in column_names
    assert 'company_name' in column_names
    assert 'industry' in column_names
    assert 'location' in column_names
    connection.close()

# Test that the candidates table has the correct columns
def test_candidates_table_columns():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("PRAGMA table_info(candidates);")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    assert 'candidate_id' in column_names
    assert 'first_name' in column_names
    assert 'last_name' in column_names
    assert 'email' in column_names
    assert 'years_experience' in column_names
    assert 'primary_skill' in column_names
    connection.close()

# Test that python_candidates holds all the candidates that have Python as a primary_skill
def test_python_candidates_genre():
    assert len(python_candidates) == 2

# Test that the John's email has been updated
def test_email_update():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Fetch the updated row
    updated = cursor.execute("SELECT * FROM candidates WHERE first_name = 'John';").fetchone()
    
    # Assert that the email has been updated
    assert updated[3] == 'john.smith@gmail.com'
    connection.close()

def test_candidate5_update():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Fetch the updated row
    updated = cursor.execute("SELECT * FROM candidates WHERE candidate_id = 5;").fetchone()
    
    # Assert that the primary_skill has been updated
    assert updated[5] == 'Python, SQL'
    connection.close()

# Test that 'Cloud Nine was deleted from the companies table
def test_cloud_nine_deleted():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Attempt to fetch the deleted row
    deleted = cursor.execute("SELECT * FROM companies WHERE company_name = 'CloudNine';").fetchone()
    
    # Assert that the row no longer exists
    assert deleted is None
    connection.close()

# Test that all `candidates` that have a `primary_skill` of `"Cloud Architecture"`. 
def test_cloud_architecture_deleted():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Fetch the updated row
    candidates = cursor.execute("SELECT * FROM candidates;").fetchall()
    
    # Assert that the company has been deleted
    assert len(candidates) == 4
    connection.close()

# Verify that the final company and candidate tables have the correct number of rows
def test_final_tables():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # Fetch the updated row
    companies = cursor.execute("SELECT * FROM companies;").fetchall()
    candidates = cursor.execute("SELECT * FROM candidates;").fetchall()
    
    # Assert that the tables have the correct number of rows
    assert len(companies) == 2
    assert len(candidates) == 4
    connection.close()