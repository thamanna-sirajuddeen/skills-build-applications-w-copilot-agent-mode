from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.db import connection

from bson import ObjectId

from django.conf import settings

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index('email', unique=True)

        # Teams
        marvel_team = {'_id': ObjectId(), 'name': 'Team Marvel'}
        dc_team = {'_id': ObjectId(), 'name': 'Team DC'}
        db.teams.insert_many([marvel_team, dc_team])

        # Users
        users = [
            {'_id': ObjectId(), 'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_team['_id']},
            {'_id': ObjectId(), 'name': 'Captain America', 'email': 'cap@marvel.com', 'team_id': marvel_team['_id']},
            {'_id': ObjectId(), 'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_team['_id']},
            {'_id': ObjectId(), 'name': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_team['_id']},
        ]
        db.users.insert_many(users)

        # Activities
        activities = [
            {'_id': ObjectId(), 'user_email': 'ironman@marvel.com', 'activity': 'Running', 'duration': 30},
            {'_id': ObjectId(), 'user_email': 'cap@marvel.com', 'activity': 'Cycling', 'duration': 45},
            {'_id': ObjectId(), 'user_email': 'wonderwoman@dc.com', 'activity': 'Swimming', 'duration': 60},
            {'_id': ObjectId(), 'user_email': 'batman@dc.com', 'activity': 'Yoga', 'duration': 40},
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {'_id': ObjectId(), 'name': 'HIIT', 'suggested_for': 'marvel'},
            {'_id': ObjectId(), 'name': 'Pilates', 'suggested_for': 'dc'},
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {'_id': ObjectId(), 'team': 'Team Marvel', 'points': 150},
            {'_id': ObjectId(), 'team': 'Team DC', 'points': 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
