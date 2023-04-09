"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path
import pandas as pds


def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)


def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    conn = sqlite3.connect(db_path)

    cursor_obj = conn.cursor()
    # SQL query to get all relationships
    fetch_relationships = """ SELECT person1.name, person2.name, init_date, type FROM relationships JOIN people person1 ON person1 = person1.id JOIN people person2 ON person2 = person2.id where \
     type = 'spouse' """

    # Execute the query and get all results
    cursor_obj.execute(fetch_relationships)

    all_relation = cursor_obj.fetchall()

    conn.close()
    # Print sentences describing each relationship

    for person1, person2, init_date, type in all_relation:
        print(f'{person1} has been a {type} of {person2} since {init_date}.')

    return all_relation


def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """

    # Creating dataframe object and using Pandas instance
    dataF = pds.DataFrame(married_couples, columns=['Person 1', 'Person 2', 'Anniversary', 'Relationship'])
    dataF.to_csv(csv_path+'lab_8.csv', index=False)


if __name__ == '__main__':
    main()
