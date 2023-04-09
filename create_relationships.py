"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from random import randint, choice
from faker import Faker

# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')


def main():
    create_relationships_table()
    populate_relationships_table()


def create_relationships_table():
    """Creates the relationships table in the DB"""
    conn = sqlite3.connect('social_network.db')
    cursor_obj = conn.cursor()

    # SQL query that creates a table named 'relationships'.
    create_relation_query = """ CREATE TABLE IF NOT EXISTS relationships ( id INTEGER PRIMARY KEY, person1 INTEGER NOT NULL, person2 INTEGER NOT NULL, type TEXT NOT NULL, init_date DATE NOT NULL, FOREIGN KEY (person1) REFERENCES people (id), FOREIGN KEY (person2) REFERENCES people (id) ); """

    # Execute the SQL query to create the 'relationships' table.
    cursor_obj.execute(create_relation_query)
    conn.commit()
    conn.close()


def populate_relationships_table():
    """Adds 100 random relationships to the DB"""

    conn = sqlite3.connect('social_network.db')
    cursor_obj = conn.cursor()

    for i in range(100):
        # SQL query that inserts a row of data in the relationships table.

        insert_query = """ INSERT INTO relationships ( person1, person2, type, init_date ) VALUES (?, ?, ?, ?); """

        fak_obj = Faker()

        # Randomly select first person in relationship
        person1 = randint(1, 200)

        # Randomly select second person in relationship
        # Loop ensures person will not be in a relationship with themself
        person2 = randint(1, 200)
        while person2 == person1:
            person2 = randint(1, 200)

        # Randomly select a relationship type
        type_rel = choice(('friend', 'spouse', 'partner', 'relative'))
        # Randomly select a relationship start date between now and 50 years ago
        init_date = fak_obj.date_between(start_date='-50y', end_date='today')
        # Create tuple of data for the new relationship

        relation_new = (person1, person2, type_rel, init_date)

        # Add the new relationship to the DB
        cursor_obj.execute(insert_query, relation_new)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
