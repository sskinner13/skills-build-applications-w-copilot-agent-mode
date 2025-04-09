import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from django.core.management.base import BaseCommand
from pymongo import MongoClient
from octofit_tracker.test_data import test_data

print('populate_db command is being loaded')

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Insert test data into collections
        db.users.insert_many(test_data['users'])
        db.teams.insert_many(test_data['teams'])
        db.activity.insert_many(test_data['activities'])
        db.leaderboard.insert_many(test_data['leaderboard'])
        db.workouts.insert_many(test_data['workouts'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
