from django.test import TestCase
from octofit.models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.name, "Test User")

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        team = Team.objects.create(name="Test Team", members=[user])
        self.assertEqual(team.name, "Test Team")
        self.assertIn(user, team.members)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        activity = Activity.objects.create(user=user, type="Running", duration=30, date="2025-04-09")
        self.assertEqual(activity.type, "Running")
        self.assertEqual(activity.duration, 30)
        self.assertEqual(activity.date, "2025-04-09")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Morning Run", description="A quick morning run.")
        self.assertEqual(workout.name, "Morning Run")
        self.assertEqual(workout.description, "A quick morning run.")
