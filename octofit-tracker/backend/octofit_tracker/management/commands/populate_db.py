from django.core.management.base import BaseCommand
from pymongo import MongoClient

print('populate_db command is being loaded')

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe"},
            {"email": "jane.smith@example.com", "name": "Jane Smith"},
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": ["john.doe@example.com"]},
            {"name": "Team Beta", "members": ["jane.smith@example.com"]},
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"user_id": "john.doe@example.com", "type": "Running", "duration": 30, "date": "2025-04-01"},
            {"user_id": "jane.smith@example.com", "type": "Cycling", "duration": 45, "date": "2025-04-02"},
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"user_id": "john.doe@example.com", "points": 100},
            {"user_id": "jane.smith@example.com", "points": 150},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"name": "Morning Run", "description": "A quick morning run to start the day."},
            {"name": "Evening Yoga", "description": "Relaxing yoga session in the evening."},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
