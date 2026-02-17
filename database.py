import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash
import os

# Use in-memory database for serverless environments (Vercel)
# This will be ephemeral but works for demo purposes
IS_SERVERLESS = os.environ.get('VERCEL', False) or os.environ.get('AWS_LAMBDA_FUNCTION_NAME', False)
DATABASE_NAME = ':memory:' if IS_SERVERLESS else 'fixapp.db'

# Global in-memory database connection for serverless
_in_memory_conn = None

def close_connection(conn):
    """Close connection only if not in-memory"""
    if not IS_SERVERLESS and conn:
        conn.close()

def get_db_connection():
    """Create and return a database connection"""
    global _in_memory_conn
    
    if IS_SERVERLESS:
        # Use persistent in-memory connection for serverless
        if _in_memory_conn is None:
            _in_memory_conn = sqlite3.connect(':memory:', check_same_thread=False)
            _in_memory_conn.row_factory = sqlite3.Row
            # Initialize database on first connection
            init_database_tables(_in_memory_conn)
        return _in_memory_conn
    else:
        # Use file-based database for local
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row
        return conn

def init_database_tables(conn):
    """Initialize database tables on given connection"""
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            full_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP,
            is_active INTEGER DEFAULT 1
        )
    ''')
    
    # Create sessions table for session management
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            session_token TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Check if demo user exists, if not create it
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", ('admin',))
    if cursor.fetchone()[0] == 0:
        # Create demo admin user (password: fix123)
        demo_password_hash = generate_password_hash('fix123')
        cursor.execute('''
            INSERT INTO users (username, email, password_hash, full_name)
            VALUES (?, ?, ?, ?)
        ''', ('admin', 'admin@fixapp.com', demo_password_hash, 'Demo Admin'))
        print("✓ Demo admin user created (username: admin, password: fix123)")
    
    conn.commit()
    print("Database tables initialized successfully")

def init_database():
    """Initialize the database with required tables"""
    if IS_SERVERLESS:
        # For serverless, connection is already initialized in get_db_connection()
        # Just ensure it's been called once
        get_db_connection()
        print("In-memory database ready for serverless")
    else:
        # For local file-based database
        conn = get_db_connection()
        init_database_tables(conn)
        conn.commit()
        close_connection(conn)
        print("File-based database initialized")

def create_user(username, email, password, full_name=None):
    """Create a new user"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        password_hash = generate_password_hash(password)
        cursor.execute('''
            INSERT INTO users (username, email, password_hash, full_name)
            VALUES (?, ?, ?, ?)
        ''', (username, email, password_hash, full_name))
        conn.commit()
        user_id = cursor.lastrowid
        close_connection(conn)
        return user_id
    except sqlite3.IntegrityError as e:
        close_connection(conn)
        return None

def get_user_by_username(username):
    """Get user by username"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    close_connection(conn)
    return user

def get_user_by_email(email):
    """Get user by email"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    close_connection(conn)
    return user

def update_last_login(user_id):
    """Update user's last login timestamp"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users 
        SET last_login = CURRENT_TIMESTAMP 
        WHERE id = ?
    ''', (user_id,))
    conn.commit()
    close_connection(conn)

def create_session(user_id, session_token, expires_at):
    """Create a new session"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sessions (user_id, session_token, expires_at)
        VALUES (?, ?, ?)
    ''', (user_id, session_token, expires_at))
    conn.commit()
    close_connection(conn)

def get_session(session_token):
    """Get session by token"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.*, u.username, u.email, u.full_name
        FROM sessions s
        JOIN users u ON s.user_id = u.id
        WHERE s.session_token = ? AND s.expires_at > CURRENT_TIMESTAMP
    ''', (session_token,))
    session = cursor.fetchone()
    close_connection(conn)
    return session

def delete_session(session_token):
    """Delete a session (logout)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sessions WHERE session_token = ?', (session_token,))
    conn.commit()
    close_connection(conn)

# Initialize database when module is imported
if __name__ == '__main__':
    init_database()
