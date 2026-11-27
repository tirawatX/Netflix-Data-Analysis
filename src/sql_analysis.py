
import sqlite3
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DB_PATH = PROJECT_ROOT / "data" / "processed" / "netflix.db"


def run_query(query):

    conn = sqlite3.connect(DB_PATH)

    result = conn.execute(query).fetchall()

    conn.close()

    return result


def main():

    # Query 1: Select all data
    print("\n========== QUERY 1 ==========")

    query = """
    SELECT *
    FROM netflix_titles
    LIMIT 5;
    """

    result = run_query(query)

    for row in result:
        print(row)


    # Query 2: Filter Movies
    print("\n========== QUERY 2 ==========")

    query = """
    SELECT title, type, release_year
    FROM netflix_titles
    WHERE type = 'Movie'
    LIMIT 10;
    """

    result = run_query(query)

    for row in result:
        print(row)


    print("\n========== QUERY 3 ==========")
    
    query = """
    SELECT title, release_year
    FROM netflix_titles
    WHERE release_year = 2020
    LIMIT 10;
    """
    
    result = run_query(query)

    for row in result:
        print(row)

    print("\n========== QUERY 4 ==========")
        
    query = """
    SELECT title ,type, release_year
    FROM netflix_titles
    WHERE type = 'TV Show'
    LIMIT 15;
    """
        
    result = run_query(query)

    for row in result:
        print(row)

    print("\n========== QUERY 5 ==========")
            
    query = """
    SELECT title, type, release_year
    FROM netflix_titles
    WHERE release_year >= 2015
    ORDER BY release_year DESC
    LIMIT 10
    ;
    """
        
    result = run_query(query)

    for row in result:
        print(row)


    print("\n========== QUERY 6 ==========")
                
    query = """
    SELECT title, type, release_year
    FROM netflix_titles
    WHERE release_year == 2020 AND type = 'Movie'
    LIMIT 10;
    """
        
    result = run_query(query)

    for row in result:
        print(row)

    print("\n========== QUERY 7 ==========")
                    
    query = """
    SELECT title, type, release_year
    FROM netflix_titles
    WHERE release_year < 2015 AND type = 'TV Show'
    LIMIT 10;
    """
        
    result = run_query(query)

    for row in result:
        print(row)


    print("\n========== QUERY 8 ==========")
                        
    query = """
    SELECT title, type, release_year
    FROM netflix_titles
    WHERE release_year <= 2020 AND release_year >= 2010
    LIMIT 10;
    """
        
    result = run_query(query)

    for row in result:
        print(row)


    print("\n========== QUERY 9 ==========")
                            
    query = """
    SELECT title, type, release_year
    FROM netflix_titles
    ORDER BY release_year DESC
    LIMIT 20;
    """
        
    result = run_query(query)

    for row in result:
        print(row)


if __name__ == "__main__":
    main()
