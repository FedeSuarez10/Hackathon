#!/bin/sh
set -e

# Check if migrations directory exists
if [ -d "migrations" ]; then
  echo "Migrations already applied."
else
  echo "Initializing migrations..."
  flask db init
  flask db migrate -m "Initial migration"
  echo "Database initialized and migration script created."
fi

# Function to wait until the database is ready
wait_for_db() {
  until flask db upgrade > /dev/null 2>&1; do
    echo "Waiting for database to be ready..."
    sleep 5
  done
}

# Wait for the database to be ready
wait_for_db
echo "Database is ready."

echo "Migrations..."
flask db migrate 
echo "Migrations done..."

# Apply migrations
echo "Applying migrations..."
flask db upgrade
echo "Done..."

# Start worker.py in the background
echo "Starting worker process..."
# python worker.py &

# Start the main application server with Gunicorn
exec gunicorn --bind 0.0.0.0:5000 wsgi:app
