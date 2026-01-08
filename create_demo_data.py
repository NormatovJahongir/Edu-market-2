"""
Demo data creation script for EduMarket System
This script creates sample centers, users, and data for testing
"""

import sqlite3
import hashlib
from datetime import datetime, timedelta
import random

def get_db():
    conn = sqlite3.connect('edumarket.db', timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA journal_mode=WAL')
    return conn

def create_demo_data():
    """Create comprehensive demo data"""
    conn = get_db()
    cursor = conn.cursor()
    
    print("🔄 Creating demo data...")
    
    # Sample center names and descriptions
    centers_data = [
        {
            'name': 'IT Academy Tashkent',
            'description': 'Dasturlash va IT sohasida professional ta\'lim. Python, Java, Web Development.',
            'address': 'Toshkent sh., Yunusobod tumani, Abdulla Qodiriy ko\'chasi 12',
            'latitude': 41.3111,
            'longitude': 69.2797,
            'phone': '+998901234567',
            'email': 'info@itacademy.uz',
            'website': 'https://itacademy.uz'
        },
        {
            'name': 'English Excellence Center',
            'description': 'IELTS, CEFR va umumiy ingliz tili kurslari. Tajribali o\'qituvchilar.',
            'address': 'Toshkent sh., Chilonzor tumani, Bunyodkor ko\'chasi 45',
            'latitude': 41.2856,
            'longitude': 69.2034,
            'phone': '+998901234568',
            'email': 'info@englishexcellence.uz',
            'website': 'https://englishexcellence.uz'
        },
        {
            'name': 'Math Genius Academy',
            'description': 'DTM, SAT, va olimpiada matematika tayyorgarlik kurslari.',
            'address': 'Toshkent sh., Mirzo Ulug\'bek tumani, Universitet ko\'chasi 4',
            'latitude': 41.3275,
            'longitude': 69.2869,
            'phone': '+998901234569',
            'email': 'info@mathgenius.uz',
            'website': 'https://mathgenius.uz'
        },
        {
            'name': 'Science Lab Center',
            'description': 'Fizika, Kimyo, Biologiya fanlaridan chuqur bilim. Laboratoriya ishlari.',
            'address': 'Toshkent sh., Yakkasaroy tumani, Shota Rustaveli ko\'chasi 23',
            'latitude': 41.3051,
            'longitude': 69.2622,
            'phone': '+998901234570',
            'email': 'info@sciencelab.uz',
            'website': 'https://sciencelab.uz'
        },
        {
            'name': 'Korean Language Institute',
            'description': 'Koreys tili, TOPIK tayyorgarlik, Koreya madaniyati o\'rganish.',
            'address': 'Toshkent sh., Olmazor tumani, Farobiy ko\'chasi 87',
            'latitude': 41.3147,
            'longitude': 69.2233,
            'phone': '+998901234571',
            'email': 'info@koreanlang.uz',
            'website': 'https://koreanlang.uz'
        }
    ]
    
    # Create center admins and centers
    for i, center_data in enumerate(centers_data, start=2):
        # Create admin
        password_hash = hashlib.sha256(f'admin{i}'.encode()).hexdigest()
        cursor.execute('''
            INSERT INTO users (username, full_name, email, password, phone, role, language, status)
            VALUES (?, ?, ?, ?, ?, 'center_admin', 'uz', 'active')
        ''', (f'admin{i}', f'Admin {i}', center_data['email'], password_hash, center_data['phone']))
        
        admin_id = cursor.lastrowid
        
        # Create center
        cursor.execute('''
            INSERT INTO centers (name, description, address, latitude, longitude, phone, email, website, admin_id, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'active')
        ''', (center_data['name'], center_data['description'], center_data['address'],
              center_data['latitude'], center_data['longitude'], center_data['phone'],
              center_data['email'], center_data['website'], admin_id))
        
        center_id = cursor.lastrowid
        print(f"  ✅ Created: {center_data['name']}")
        
        # Create subjects for each center
        subjects = []
        if 'IT' in center_data['name']:
            subjects = [
                ('Python Programming', 'Python asoslari va Django framework', 800000, 6),
                ('JavaScript & React', 'Frontend development', 900000, 6),
                ('Java Development', 'Backend development', 1000000, 8)
            ]
        elif 'English' in center_data['name']:
            subjects = [
                ('IELTS Preparation', 'IELTS 6.5+ olish uchun', 700000, 4),
                ('General English', 'Beginner dan Advanced gacha', 600000, 6),
                ('Business English', 'Ish uchun ingliz tili', 750000, 3)
            ]
        elif 'Math' in center_data['name']:
            subjects = [
                ('DTM Tayyorgarlik', 'Matematika DTM tayyorlov', 600000, 3),
                ('SAT Math', 'SAT imtihoni matematika', 800000, 4),
                ('Olimpiada Matematika', 'Respublika olimpiadalari', 900000, 8)
            ]
        elif 'Science' in center_data['name']:
            subjects = [
                ('Fizika', 'Umumiy va DTM fizika', 650000, 6),
                ('Kimyo', 'Umumiy va DTM kimyo', 650000, 6),
                ('Biologiya', 'Umumiy va DTM biologiya', 600000, 5)
            ]
        elif 'Korean' in center_data['name']:
            subjects = [
                ('TOPIK I', 'TOPIK 1-2 daraja', 700000, 4),
                ('TOPIK II', 'TOPIK 3-6 daraja', 850000, 6),
                ('Korean Culture', 'Koreya madaniyati', 500000, 3)
            ]
        
        for subj in subjects:
            cursor.execute('''
                INSERT INTO subjects (center_id, name, description, price, duration_months, status)
                VALUES (?, ?, ?, ?, ?, 'active')
            ''', (center_id, subj[0], subj[1], subj[2], subj[3]))
        
        # Create teachers
        for j in range(3):
            teacher_name = f"O'qituvchi {random.choice(['Aziz', 'Dilnoza', 'Shohruh', 'Madina', 'Javohir', 'Zilola'])}"
            password_hash = hashlib.sha256(f'teacher{center_id}{j}'.encode()).hexdigest()
            
            cursor.execute('''
                INSERT INTO users (username, full_name, email, password, role, language, status)
                VALUES (?, ?, ?, ?, 'teacher', 'uz', 'active')
            ''', (f'teacher{center_id}{j}', teacher_name, f'teacher{center_id}{j}@example.uz', password_hash))
            
            teacher_user_id = cursor.lastrowid
            
            cursor.execute('''
                INSERT INTO teachers (user_id, center_id, experience_years, bio, 
                                     kpi_successful_students, kpi_dropout_students, kpi_rating, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'active')
            ''', (teacher_user_id, center_id, random.randint(2, 10), 
                  'Tajribali o\'qituvchi', random.randint(50, 200), 
                  random.randint(5, 20), round(random.uniform(4.0, 5.0), 1)))
        
        # Create students
        for k in range(15):
            student_name = f"O'quvchi {random.choice(['Ali', 'Zarina', 'Bobur', 'Nargiza', 'Sardor', 'Kamola'])}"
            password_hash = hashlib.sha256(f'student{center_id}{k}'.encode()).hexdigest()
            
            cursor.execute('''
                INSERT INTO users (username, full_name, email, password, phone, role, language, status)
                VALUES (?, ?, ?, ?, ?, 'student', 'uz', 'active')
            ''', (f'student{center_id}{k}', student_name, f'student{center_id}{k}@example.uz', 
                  password_hash, f'+99890{random.randint(1000000, 9999999)}'))
            
            student_id = cursor.lastrowid
            
            # Create enrollment
            cursor.execute('SELECT id FROM subjects WHERE center_id = ? LIMIT 1', (center_id,))
            subject_result = cursor.fetchone()
            if subject_result:
                subject_id = subject_result[0]
                
                cursor.execute('SELECT id FROM teachers WHERE center_id = ? LIMIT 1', (center_id,))
                teacher_result = cursor.fetchone()
                if teacher_result:
                    teacher_id = teacher_result[0]
                    
                    cursor.execute('''
                        INSERT INTO enrollments (student_id, center_id, subject_id, teacher_id, 
                                               enrollment_date, status)
                        VALUES (?, ?, ?, ?, ?, 'active')
                    ''', (student_id, center_id, subject_id, teacher_id, 
                          (datetime.now() - timedelta(days=random.randint(1, 180))).strftime('%Y-%m-%d')))
                    
                    enrollment_id = cursor.lastrowid
                    
                    # Create payment
                    cursor.execute('SELECT price FROM subjects WHERE id = ?', (subject_id,))
                    price = cursor.fetchone()[0]
                    
                    payment_status = random.choice(['paid', 'paid', 'paid', 'pending', 'overdue'])
                    cursor.execute('''
                        INSERT INTO payments (enrollment_id, student_id, center_id, amount, 
                                            payment_type, payment_method, payment_date, status)
                        VALUES (?, ?, ?, ?, 'monthly', ?, ?, ?)
                    ''', (enrollment_id, student_id, center_id, price, 
                          random.choice(['cash', 'card', 'payme', 'click']),
                          (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'),
                          payment_status))
                    
                    # Create attendance records
                    for day in range(20):
                        cursor.execute('''
                            INSERT INTO attendance (enrollment_id, student_id, subject_id, date, status)
                            VALUES (?, ?, ?, ?, ?)
                        ''', (enrollment_id, student_id, subject_id,
                              (datetime.now() - timedelta(days=day)).strftime('%Y-%m-%d'),
                              random.choice(['present', 'present', 'present', 'absent', 'late'])))
                    
                    # Create test results
                    for test in range(5):
                        score = random.randint(50, 100)
                        cursor.execute('''
                            INSERT INTO results (student_id, subject_id, test_name, score, 
                                               max_score, percentage, test_date)
                            VALUES (?, ?, ?, ?, 100, ?, ?)
                        ''', (student_id, subject_id, f'Test #{test+1}', score, score,
                              (datetime.now() - timedelta(days=test*7)).strftime('%Y-%m-%d')))
        
        # Create reviews
        for r in range(random.randint(5, 15)):
            cursor.execute('SELECT id FROM users WHERE role = "student" ORDER BY RANDOM() LIMIT 1')
            random_student = cursor.fetchone()
            if random_student:
                comments = [
                    'Juda yaxshi o\'quv markazi! Tavsiya qilaman.',
                    'Professional o\'qituvchilar. Natijaga erishdim.',
                    'Zo\'r sharoit va do\'stona muhit.',
                    'Sifatli ta\'lim. Mamnunman.',
                    'Eng yaxshi markaz! 5 yulduz!'
                ]
                cursor.execute('''
                    INSERT INTO reviews (center_id, user_id, rating, comment, status)
                    VALUES (?, ?, ?, ?, 'approved')
                ''', (center_id, random_student[0], random.randint(4, 5), random.choice(comments)))
    
    # Update all center ratings
    cursor.execute('SELECT id FROM centers')
    centers = cursor.fetchall()
    for center in centers:
        from database import calculate_center_rating
        calculate_center_rating(center[0])
    
    conn.commit()
    conn.close()
    
    print("\n✅ Demo data created successfully!")
    print("\n📊 Summary:")
    print(f"  - Centers: {len(centers_data)}")
    print(f"  - Subjects: ~{len(centers_data) * 3}")
    print(f"  - Teachers: ~{len(centers_data) * 3}")
    print(f"  - Students: ~{len(centers_data) * 15}")
    print(f"  - Total Users: ~{len(centers_data) * 19}")
    print("\n🔐 Login credentials:")
    print("  Super Admin: superadmin / admin123")
    print("  Center Admins: admin2, admin3, admin4, admin5, admin6 / admin2, admin3, etc.")

if __name__ == '__main__':
    try:
        create_demo_data()
    except Exception as e:
        print(f"❌ Error: {e}")
