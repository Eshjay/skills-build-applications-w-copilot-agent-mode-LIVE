from pymongo import MongoClient
import json
import os

def populate_database():
    # Connect to MongoDB
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']

    # Load test data from JSON file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(base_dir, 'octofit_tracker/test_data.json')
    with open(test_data_path, 'r') as file:
        test_data = json.load(file)

    # Drop existing collections
    db.users.drop()
    db.teams.drop()
    db.activities.drop()
    db.leaderboard.drop()
    db.workouts.drop()

    # Insert test data into collections
    db.users.insert_many(test_data['users'])
    db.teams.insert_many(test_data['teams'])
    db.activities.insert_many(test_data['activities'])
    db.leaderboard.insert_many(test_data['leaderboard'])
    db.workouts.insert_many(test_data['workouts'])

    print('Successfully populated the database with test data.')

if __name__ == '__main__':
    populate_database()
