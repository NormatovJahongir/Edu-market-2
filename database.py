import sqlite3
import os
import hashlib
from datetime import datetime

# 1. Loyiha papkasini va baza yo'lini aniq belgilaymiz
# Bu Flask va Bot bitta bazaga (edu_market.db) murojaat qilishini ta'minlaydi
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'edu_market.db')

def get_db():
    """Ma'lumotlar bazasiga ulanish yaratish"""
    conn = sqlite3.connect(DB_PATH)
    # Natijalarni ustun nomi bilan olish uchun (masalan: user['username'])
    conn.row_factory = sqlite3.Row
    # SQLite'da Foreign Key (tashqi kalit) cheklovlarini yoqish
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    """Barcha jadvallarni yaratish va bazani sozlash"""
    conn = get_db()
    cursor = conn.cursor()

    # --- 1. USERS JADVALI ---
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id TEXT UNIQUE,
        username TEXT UNIQUE,
        full_name TEXT NOT NULL,
        password TEXT,
        role TEXT NOT NULL CHECK(role IN ('super_admin', 'center_admin', 'teacher', 'student')),
        status TEXT DEFAULT 'active',
        language TEXT DEFAULT 'uz',
        phone TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    # --- 2. CENTERS JADVALI ---
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS centers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        admin_id INTEGER,
        description TEXT,
        address TEXT,
        latitude REAL,
        longitude REAL,
        rating REAL DEFAULT 0,
        student_count INTEGER DEFAULT 0,
        status TEXT DEFAULT 'active',
        telegram_link TEXT,
        photo_path TEXT,
        FOREIGN KEY (admin_id) REFERENCES users (id) ON DELETE SET NULL
    )''')

    # --- 3. SUBJECTS JADVALI ---
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        center_id INTEGER,
        name TEXT NOT NULL,
        price REAL,
        duration TEXT,
        status TEXT DEFAULT 'active',
        FOREIGN KEY (center_id) REFERENCES centers (id) ON DELETE CASCADE
    )''')

    # --- 4. TEACHERS JADVALI ---
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        center_id INTEGER,
        subject_id INTEGER,
        bio TEXT,
        experience TEXT,
        status TEXT DEFAULT 'active',
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
        FOREIGN KEY (center_id) REFERENCES centers (id) ON DELETE CASCADE,
        FOREIGN KEY (subject_id) REFERENCES subjects (id) ON DELETE SET NULL
    )''')

    # --- 5. ENROLLMENTS (Kursga yozilishlar) ---
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        center_id INTEGER,
        subject_id INTEGER,
        teacher_id INTEGER,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES users (id),
        FOREIGN KEY (center_id) REFERENCES centers (id),
        FOREIGN KEY (subject_id) REFERENCES subjects (id),
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
    )''')

    # --- 6. PAYMENTS (To'lovlar) ---
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        center_id INTEGER,
        amount REAL NOT NULL,
        status TEXT DEFAULT 'unpaid',
        payment_method TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES users (id),
        FOREIGN KEY (center_id) REFERENCES centers (id)
    )''')

    # --- 7. REVIEWS (Fikrlar) ---
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        center_id INTEGER,
        rating INTEGER CHECK(rating BETWEEN 1 AND 5),
        comment TEXT,
        status TEXT DEFAULT 'approved',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (center_id) REFERENCES centers (id)
    )''')

    # --- SUPER ADMINNI AVTOMATIK YARATISH ---
    # Bu qism baza har safar yangilanganda adminingiz o'chib ketmasligini ta'minlaydi
    admin_username = 'admin'
    admin_password = 'admin123'
    password_hash = hashlib.sha256(admin_password.encode()).hexdigest()

    cursor.execute('''
        INSERT OR IGNORE INTO users (full_name, username, password, role, status, language)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', ('Bosh Admin', admin_username, password_hash, 'super_admin', 'active', 'uz'))

    conn.commit()
    conn.close()
    print(f"Baza va Super Admin muvaffaqiyatli tayyorlandi: {DB_PATH}")

def calculate_center_rating(center_id):
    """Markaz reytingini fikrlar asosida qayta hisoblash"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT AVG(rating) FROM reviews WHERE center_id = ? AND status = "approved"', (center_id,))
    avg_rating = cursor.fetchone()[0] or 0
    
    cursor.execute('UPDATE centers SET rating = ? WHERE id = ?', (round(avg_rating, 1), center_id))
    conn.commit()
    conn.close()
    return avg_rating
