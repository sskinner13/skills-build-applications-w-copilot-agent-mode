# Test data for the OctoFit app

test_data = {
    "users": [
        {"email": "john.doe@example.com", "name": "John Doe"},
        {"email": "jane.smith@example.com", "name": "Jane Smith"},
    ],
    "teams": [
        {"name": "Team Alpha", "members": ["john.doe@example.com"]},
        {"name": "Team Beta", "members": ["jane.smith@example.com"]},
    ],
    "activities": [
        {"user_id": "john.doe@example.com", "type": "Running", "duration": 30, "date": "2025-04-01"},
        {"user_id": "jane.smith@example.com", "type": "Cycling", "duration": 45, "date": "2025-04-02"},
    ],
    "leaderboard": [
        {"user_id": "john.doe@example.com", "points": 100},
        {"user_id": "jane.smith@example.com", "points": 150},
    ],
    "workouts": [
        {"name": "Morning Run", "description": "A quick morning run to start the day."},
        {"name": "Evening Yoga", "description": "Relaxing yoga session in the evening."},
    ],
}
