# 📂 LOYIHA STRUKTURASI

```
EduMarket_System/
│
├── 📄 app.py                      # Flask Web Application (asosiy)
├── 📄 database.py                 # Ma'lumotlar bazasi modeli
├── 📄 requirements.txt            # Python dependencies
├── 📄 run.py                      # Quick start script
├── 📄 create_demo_data.py         # Demo data generator
├── 📄 README.md                   # To'liq dokumentatsiya
├── 📄 QUICK_START.md              # Tezkor boshlash yo'riqnomasi
├── 📄 PROJECT_STRUCTURE.md        # Bu fayl
│
├── 🗄️ edumarket.db                # SQLite Database
│
├── 📁 bot/
│   └── 📄 telegram_bot.py         # 3-tilli Telegram Bot (UZ/RU/EN)
│
├── 📁 templates/                  # HTML sahifalar
│   ├── 📄 base.html               # Asosiy shablon
│   ├── 📄 marketplace.html        # Markazlar bozori
│   ├── 📄 admin_dashboard.html    # Admin panel
│   ├── 📄 student_dashboard.html  # O'quvchi kabineti
│   ├── 📄 center_detail.html      # Markaz detallari
│   ├── 📄 map.html                # Interactive xarita
│   └── 📄 login.html              # Login sahifasi
│
├── 📁 static/
│   ├── 📁 css/
│   │   └── 📄 style.css           # Professional CSS (60KB+)
│   │
│   ├── 📁 js/
│   │   └── 📄 main.js             # JavaScript funksiyalar
│   │
│   └── 📁 images/                 # Rasmlar papkasi
│
└── 📁 uploads/
    └── 📁 centers/                # Markazlar logolari
```

## 🗃 Ma'lumotlar Bazasi Strukturasi

### Asosiy Jadvallar:

1. **users** - Barcha foydalanuvchilar
   - Rollari: super_admin, center_admin, teacher, student, guest
   - Fields: id, telegram_id, username, full_name, email, password, role, language, status

2. **centers** - O'quv markazlari
   - Fields: id, name, description, address, latitude, longitude, phone, email, website, logo, admin_id, rating, student_count, review_count, avg_results, status

3. **subjects** - Fanlar/Kurslar
   - Fields: id, center_id, name, description, price, duration_months, status

4. **teachers** - O'qituvchilar
   - Fields: id, user_id, center_id, subject_id, experience_years, bio, kpi_successful_students, kpi_dropout_students, kpi_rating, status

5. **enrollments** - O'quvchilar ro'yxati
   - Fields: id, student_id, center_id, subject_id, teacher_id, enrollment_date, end_date, status

6. **payments** - To'lovlar
   - Fields: id, enrollment_id, student_id, center_id, amount, payment_type, payment_method, payment_date, due_date, status

7. **attendance** - Davomat
   - Fields: id, enrollment_id, student_id, subject_id, date, status, qr_code, marked_by

8. **results** - Test natijalari
   - Fields: id, student_id, subject_id, test_name, score, max_score, percentage, test_date

9. **reviews** - Sharhlar va reytinglar
   - Fields: id, center_id, user_id, rating, comment, status

10. **notifications** - Bildirishnomalar
    - Fields: id, user_id, type, title, message, send_via, status, scheduled_at, sent_at

11. **bot_states** - Bot holatlari
    - Fields: telegram_id, state, data, updated_at

## 🎨 Dizayn Tizimi

### Color Palette:
- **Primary:** #4F46E5 (Indigo)
- **Primary Dark:** #4338CA
- **Secondary:** #10B981 (Green)
- **Warning:** #F59E0B (Amber)
- **Danger:** #EF4444 (Red)
- **Dark:** #1F2937
- **Light:** #F9FAFB
- **Border:** #E5E7EB
- **Text:** #374151

### Typography:
- Font Family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- Headings: Bold, responsive sizing
- Body: 16px, line-height 1.6

### Responsive Breakpoints:
- Desktop: 1200px+
- Tablet: 768px - 1199px
- Mobile: < 768px

## 🔧 Texnologiyalar Stack

### Backend:
- **Python 3.9+**
- **Flask 3.0.0** - Web framework
- **SQLite** - Database

### Frontend:
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with Flexbox & Grid
- **JavaScript ES6+** - Interactive features
- **Leaflet.js** - Interactive maps
- **Chart.js** - Analytics visualizations
- **Font Awesome** - Icons

### Bot:
- **python-telegram-bot 20.7** - Telegram API
- **Requests** - HTTP library

## 📊 Asosiy Funksiyalar

### 1. Marketplace (Public)
- Markazlar ro'yxati
- Qidirish va filtrlash
- Reyting bo'yicha saralash
- Markaz detallari

### 2. Admin Dashboard
- Statistika va analitika
- Markazlar boshqaruvi
- O'quvchilar va o'qituvchilar
- To'lovlar nazorati
- Davomat boshqaruvi

### 3. Student Dashboard
- Faol kurslar
- To'lovlar tarixi
- Davomat ko'rsatkichlari
- Test natijalari

### 4. Interactive Map
- Geolocation support
- Marker clustering
- Filter by rating
- Search functionality

### 5. Telegram Bot
- Multi-language (UZ/RU/EN)
- User registration
- Center search
- Course enrollment
- Web App integration

## 🔐 Xavfsizlik

- **Authentication:** Session-based
- **Password:** SHA-256 hashing
- **Authorization:** Role-based access control
- **Input validation:** Server-side validation
- **CSRF protection:** Built-in Flask

## 📈 Reyting Algoritmi

```python
Rating = (AvgResults × 0.5) + (StudentCount × 0.3) + (Reviews × 0.2)
```

### Komponentlar:
- **AvgResults (50%)** - O'quvchilarning o'rtacha test natijalari
- **StudentCount (30%)** - Faol o'quvchilar soni
- **Reviews (20%)** - Tasdiqlangan sharhlar soni

## 🚀 Deployment Yo'riqnomasi

### Development:
```bash
python app.py
```

### Production:
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

### Bot:
```bash
cd bot
python telegram_bot.py &
```

## 📝 Kod Standartlari

- **Python:** PEP 8
- **JavaScript:** ES6+ standards
- **CSS:** BEM methodology
- **HTML:** Semantic, accessible markup

## 🧪 Testing

### Manual Testing Checklist:
- [ ] User registration va login
- [ ] Marketplace search va filter
- [ ] Center detail page
- [ ] Admin dashboard analytics
- [ ] Payment creation
- [ ] Attendance marking
- [ ] Map functionality
- [ ] Telegram bot commands

## 📚 API Documentation

### Authentication Required:
- Header: `Cookie: session=<session_id>`

### Endpoints:
```
GET  /                           # Marketplace
GET  /center/<id>                # Center details
GET  /map                        # Interactive map
POST /login                      # Login
GET  /logout                     # Logout
GET  /admin/dashboard            # Admin panel
GET  /student/dashboard          # Student panel

GET  /api/centers                # List centers
GET  /api/center/<id>            # Center info
POST /api/user/register          # Register user
POST /api/enroll                 # Enroll in course
```

## 🎓 Educational Features

### For Centers:
- CRM system
- Student management
- Payment tracking
- Attendance monitoring
- Performance analytics

### For Students:
- Course enrollment
- Payment history
- Attendance tracking
- Test results
- Progress monitoring

### For Parents/Guests:
- Center discovery
- Rating comparison
- Location-based search
- Reviews and feedback

---

**Loyiha versiyasi:** 1.0.0  
**Yaratilgan sana:** 2025-01-04  
**Muallif:** AIRITOM Logistics Center
