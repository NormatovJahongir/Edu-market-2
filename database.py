import sqlite3
from datetime import datetime
import hashlib
import os

DATABASE =os.environ.get('DATABASE_PATH', 'edumarket.db')

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database with all tables"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Users table (Super Admin, Center Admin, Teachers, Students)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id TEXT UNIQUE,
            username TEXT,
            full_name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            password TEXT,
            role TEXT NOT NULL CHECK(role IN ('super_admin', 'center_admin', 'teacher', 'student', 'guest')),
            language TEXT DEFAULT 'uz' CHECK(language IN ('uz', 'ru', 'en')),
            status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive', 'blocked')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Centers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS centers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            address TEXT,
            latitude REAL,
            longitude REAL,
            phone TEXT,
            email TEXT,
            website TEXT,
            logo TEXT,
            admin_id INTEGER,
            rating REAL DEFAULT 0.0,
            student_count INTEGER DEFAULT 0,
            review_count INTEGER DEFAULT 0,
            avg_results REAL DEFAULT 0.0,
            status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'active', 'inactive', 'blocked')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (admin_id) REFERENCES users(id)
        )
    ''')
    
    # Subjects/Courses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            center_id INTEGER,
            name TEXT NOT NULL,
            description TEXT,
            price REAL,
            duration_months INTEGER,
            status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (center_id) REFERENCES centers(id) ON DELETE CASCADE
        )
    ''')
    
    # Teachers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            center_id INTEGER,
            subject_id INTEGER,
            experience_years INTEGER,
            bio TEXT,
            kpi_successful_students INTEGER DEFAULT 0,
            kpi_dropout_students INTEGER DEFAULT 0,
            kpi_rating REAL DEFAULT 0.0,
            status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (center_id) REFERENCES centers(id) ON DELETE CASCADE,
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        )
    ''')
    
    # Students enrollment
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            center_id INTEGER,
            subject_id INTEGER,
            teacher_id INTEGER,
            enrollment_date DATE DEFAULT CURRENT_TIMESTAMP,
            end_date DATE,
            status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive', 'completed', 'dropout')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (center_id) REFERENCES centers(id) ON DELETE CASCADE,
            FOREIGN KEY (subject_id) REFERENCES subjects(id),
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        )
    ''')
    
    # Payments
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            enrollment_id INTEGER,
            student_id INTEGER,
            center_id INTEGER,
            amount REAL NOT NULL,
            payment_type TEXT CHECK(payment_type IN ('monthly', 'quarterly', 'yearly', 'one_time')),
            payment_method TEXT CHECK(payment_method IN ('cash', 'card', 'transfer', 'payme', 'click')),
            payment_date DATE DEFAULT CURRENT_TIMESTAMP,
            due_date DATE,
            status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'paid', 'overdue', 'cancelled')),
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (enrollment_id) REFERENCES enrollments(id),
            FOREIGN KEY (student_id) REFERENCES users(id),
            FOREIGN KEY (center_id) REFERENCES centers(id)
        )
    ''')
    
    # Attendance
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            enrollment_id INTEGER,
            student_id INTEGER,
            subject_id INTEGER,
            date DATE NOT NULL,
            status TEXT CHECK(status IN ('present', 'absent', 'late', 'excused')),
            qr_code TEXT,
            marked_by INTEGER,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (enrollment_id) REFERENCES enrollments(id),
            FOREIGN KEY (student_id) REFERENCES users(id),
            FOREIGN KEY (subject_id) REFERENCES subjects(id),
            FOREIGN KEY (marked_by) REFERENCES users(id)
        )
    ''')
    
    # Test Results
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            test_name TEXT,
            score REAL,
            max_score REAL,
            percentage REAL,
            test_date DATE DEFAULT CURRENT_TIMESTAMP,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES users(id),
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        )
    ''')
    
    # Reviews and Ratings
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            center_id INTEGER,
            user_id INTEGER,
            rating INTEGER CHECK(rating >= 1 AND rating <= 5),
            comment TEXT,
            status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'approved', 'rejected')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (center_id) REFERENCES centers(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    # Notifications
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT CHECK(type IN ('payment', 'attendance', 'result', 'general')),
            title TEXT,
            message TEXT,
            send_via TEXT DEFAULT 'telegram' CHECK(send_via IN ('telegram', 'sms', 'both')),
            status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'sent', 'failed')),
            scheduled_at TIMESTAMP,
            sent_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    # Bot states (for conversation flow)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bot_states (
            telegram_id TEXT PRIMARY KEY,
            state TEXT,
            data TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    
    # Create super admin if not exists
    cursor.execute("SELECT * FROM users WHERE role='super_admin' LIMIT 1")
    if not cursor.fetchone():
        password_hash = hashlib.sha256('admin123'.encode()).hexdigest()
        cursor.execute('''
            INSERT INTO users (username, full_name, email, password, role, language, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ('superadmin', 'Super Administrator', 'admin@edumarket.uz', password_hash, 'super_admin', 'uz', 'active'))
        conn.commit()
        print("✅ Super Admin created: username='superadmin', password='admin123'")
    
    conn.close()
    print("✅ Database initialized successfully!")

def calculate_center_rating(center_id):
    """Calculate center rating based on formula"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT 
            COALESCE(AVG(r.percentage), 0) as avg_results,
            (SELECT COUNT(*) FROM enrollments WHERE center_id = ? AND status = 'active') as student_count,
            (SELECT COUNT(*) FROM reviews WHERE center_id = ? AND status = 'approved') as review_count
        FROM results r
        JOIN enrollments e ON r.student_id = e.student_id
        WHERE e.center_id = ?
    ''', (center_id, center_id, center_id))
    
    data = cursor.fetchone()
    avg_results = data['avg_results'] if data else 0
    student_count = data['student_count'] if data else 0
    review_count = data['review_count'] if data else 0
    
    # Rating = (AvgResults × 0.5) + (StudentCount × 0.3) + (Reviews × 0.2)
    rating = (avg_results * 0.5) + (student_count * 0.3) + (review_count * 0.2)
    
    cursor.execute('''
        UPDATE centers 
        SET rating = ?, avg_results = ?, student_count = ?, review_count = ?
        WHERE id = ?
    ''', (rating, avg_results, student_count, review_count, center_id))
    
    conn.commit()
    conn.close()
    
    return rating

if __name__ == '__main__':
    init_db()
