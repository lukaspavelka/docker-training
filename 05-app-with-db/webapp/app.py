from flask import Flask
import os
import psycopg2
import time

app = Flask(__name__)

def get_db_connection():
    conn = None
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST", "db"), # Service name in docker-compose
                database=os.getenv("POSTGRES_DB", "mydatabase"),
                user=os.getenv("POSTGRES_USER", "user"),
                password=os.getenv("POSTGRES_PASSWORD", "password")
            )
            return conn
        except psycopg2.OperationalError as e:
            app.logger.error(f"Database connection attempt failed: {e}")
            retries -= 1
            if retries == 0:
                app.logger.error("Max retries reached. Could not connect to database.")
                return None
            app.logger.info(f"Retrying database connection in 5 seconds... ({retries} retries left)")
            time.sleep(5)
    return None


@app.route('/')
def hello():
    return "Hello from the Web App! Check /db_status for database connection."

@app.route('/db_status')
def db_status():
    conn = get_db_connection()
    if conn:
        try:
            # Try to execute a simple query
            cur = conn.cursor()
            cur.execute('SELECT version();')
            db_version = cur.fetchone()
            cur.close()
            conn.close()
            return f"Successfully connected to PostgreSQL! Version: {db_version[0]}"
        except Exception as e:
            app.logger.error(f"Error during database query: {e}")
            if conn: # Ensure connection is closed if it was opened
                conn.close()
            return f"Connected to database server, but failed to query. Error: {e}", 500
    else:
        return "Failed to connect to the database.", 500

if __name__ == '__main__':
    # This is for local development without Docker/Gunicorn
    # The Docker CMD will use Gunicorn or another WSGI server
    app.run(debug=True, host='0.0.0.0', port=5001)
