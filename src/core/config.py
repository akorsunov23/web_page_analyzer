import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite+aiosqlite:///src/database.db')
