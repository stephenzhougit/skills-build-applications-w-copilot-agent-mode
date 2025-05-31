from pymongo import MongoClient
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Initialize MongoDB collections and indexes'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['monafit_db']

        # Create collections
        collections = ['users', 'teams', 'activities', 'leaderboard', 'workouts']
        for collection in collections:
            db.create_collection(collection)

        # Create unique indexes
        db['users'].create_index('email', unique=True)
        db['teams'].create_index('name', unique=True)
        db['activities'].create_index('activity_id', unique=True)
        db['leaderboard'].create_index('team_id', unique=True)
        db['workouts'].create_index('workout_id', unique=True)

        self.stdout.write(self.style.SUCCESS('MongoDB collections and indexes initialized successfully'))
