import sqlite3
import os

# Test that companies table exists
def test_companies_table_exists():
    """Verify that the cities table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check if users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='companies';")
    result = cursor.fetchone()
    assert result is not None, "Companies table does not exist"
    
    connection.close()

# Test that candidates table exists
def test_candidates_table_exists():
    """Verify that the cities table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check if users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='candidates';")
    result = cursor.fetchone()
    assert result is not None, "Candidates table does not exist"
    
    connection.close()

# Test that companies table has correct columns
def test_companies_table_columns():
    """Verify the schema of the users table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Get table info
    cursor.execute("PRAGMA table_info(companies);")
    columns = cursor.fetchall()
    print(columns)

    # Expected columns and their types
    expected_columns = [
        (0, 'company_id', 'INTEGER', 0, None, 1),
        (1, 'company_name', 'STRING', 0, None, 0),
        (2, 'industry', 'STRING', 0, None, 0),
        (3, 'location', 'STRING', 0, None, 0),
    ]
    
    # Check number of columns
    assert len(columns) == 4, f"Expected 4 columns, found {len(columns)}"
    
    # Check each column's details
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[1], f"Column name mismatch: expected {expected[1]}, got {actual[1]}"
        assert actual[2] == expected[2], f"Column type mismatch for {actual[1]}: expected {expected[2]}, got {actual[2]}"
        assert actual[5] == expected[5], f"Primary key configuration mismatch for {actual[1]}: expected {expected[5]}, got {actual[5]}"
    
    connection.close()

# Test that candidates table has correct columns
def test_candidates_table_columns():
    """Verify the schema of the users table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Get table info
    cursor.execute("PRAGMA table_info(candidates);")
    columns = cursor.fetchall()
    print(columns)
    
    # Expected columns and their types
    expected_columns = [
        (0, 'candidate_id', 'INTEGER', 0, None, 1),
        (1, 'first_name', 'STRING', 0, None, 0),
        (2, 'last_name', 'STRING', 0, None, 0),
        (3, 'email', 'STRING', 0, None, 0),
        (4, 'years_experience', 'INTEGER', 0, None, 0),
        (5, 'primary_skill', 'STRING', 0, None, 0)
    ]
    
    # Check number of columns
    assert len(columns) == 6, f"Expected 6 columns, found {len(columns)}"
    
    # Check each column's details
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[1], f"Column name mismatch: expected {expected[1]}, got {actual[1]}"
        assert actual[2] == expected[2], f"Column type mismatch for {actual[1]}: expected {expected[2]}, got {actual[2]}"
        assert actual[5] == expected[5], f"Primary key configuration mismatch for {actual[1]}: expected {expected[5]}, got {actual[5]}"
    
    connection.close()

def test_john_email_update():
    """Test that John's email was updated correctly"""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT email FROM candidates WHERE first_name = 'John';")
    email = cursor.fetchone()[0]
    assert email == 'john.smith@gmail.com'  # Updated email value

def test_techcorp_location_update():
    """Test that Techcrop's location was updated correctly"""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT location FROM companies WHERE company_name = 'TechCorp';")
    location = cursor.fetchone()[0]
    assert location == 'New York'  # Updated location value

def test_candidateid_update():
    """Test that individual with candidate_id of 5 had primary_skill updated correctly"""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT primary_skill FROM candidates WHERE candidate_id = 5;")
    skills = cursor.fetchone()[0]
    assert skills == 'Python, SQL'  # Updated location value

def test_deleted_cloudnice():
    """Test that CloudNine was deleted"""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT company_name FROM companies WHERE company_name = 'CloudNine';")
    deleted_company = cursor.fetchall()
    assert len(deleted_company) == 0

def test_deleted_candidates():
    """Test that candidates with primary_skill of 'Cloud Architecture' were deleted"""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM candidates WHERE primary_skill = 'Cloud Architecture';")
    deleted_candidates = cursor.fetchall()
    assert len(deleted_candidates) == 0