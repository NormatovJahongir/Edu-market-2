# 🎓 EduMarket & Management System

**3 ta tilda (O'zbek, Rus, Ingliz) Telegram Bot bilan integratsiya qilingan to'liq ishlaydigan O'quv Markazlari Boshqaruv Tizimi**

---

## 📋 Loyiha haqida

EduMarket & Management System - bu o'quv markazlari faoliyatini avtomatlashtirish (CRM/LMS) va foydalanuvchilar uchun o'quv markazlari reytingini ko'rsatuvchi yagona platforma (Marketplace) hisoblanadi.

### Asosiy imkoniyatlar:

- ✅ **Super Admin Panel** - Barcha markazlarni boshqarish
- ✅ **O'quv Markazi Admini Panel** - O'z markazini boshqarish
- ✅ **Student Dashboard** - O'quvchi shaxsiy kabineti
- ✅ **Marketplace** - Markazlar reytingi va qidirish
- ✅ **Interactive Map** - Xaritada markazlarni ko'rish
- ✅ **Telegram Bot** - 3 ta tilda (UZ, RU, EN)
- ✅ **Payment Management** - To'lovlarni boshqarish
- ✅ **Attendance System** - Davomat tizimi
- ✅ **Analytics & Reports** - Analitika va hisobotlar

---

## 🛠 Texnologiyalar

### Backend:
- Python 3.9+
- Flask (Web Framework)
- SQLite (Database)

### Frontend:
- HTML5, CSS3, JavaScript
- Leaflet.js (Interactive Maps)
- Chart.js (Analytics Charts)

### Bot:
- python-telegram-bot 20.7
- Multi-language support

---

## 📦 O'rnatish

### 1. Repozitoriyni yuklab olish
```bash
cd EduMarket_System
```

### 2. Virtual environment yaratish
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Paketlarni o'rnatish
```bash
pip install -r requirements.txt
```

### 4. Ma'lumotlar bazasini yaratish
```bash
python database.py
```

Standart Super Admin yaratiladi:
- **Username:** `superadmin`
- **Password:** `admin123`

---

## 🚀 Ishga tushirish

### Web Application
```bash
python app.py
```

Web sahifa: `http://localhost:5000`

### Telegram Bot

1. **BotFather**dan bot yaratish:
   - Telegram'da @BotFather ga boring
   - `/newbot` komandasi bilan yangi bot yarating
   - Bot tokenni nusxalang

2. **Bot konfiguratsiyasi:**

`bot/telegram_bot.py` faylidagi `BOT_TOKEN` va `WEB_APP_URL` ni yangilang:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # BotFather dan olgan token
WEB_APP_URL = "http://localhost:5000"  # Yoki server manzili
```

3. **Botni ishga tushirish:**
```bash
cd bot
python telegram_bot.py
```

---

## 📊 Ma'lumotlar Bazasi Strukturasi

### Asosiy Jadvallar:

1. **users** - Foydalanuvchilar (Admin, Teacher, Student)
2. **centers** - O'quv markazlari
3. **subjects** - Fanlar
4. **teachers** - O'qituvchilar
5. **enrollments** - O'quvchilar ro'yxati
6. **payments** - To'lovlar
7. **attendance** - Davomat
8. **results** - Test natijalari
9. **reviews** - Sharhlar va reytinglar
10. **notifications** - Bildirishnomalar

---

## 🎯 Foydalanish

### Super Admin:
1. `http://localhost:5000/login` ga kiring
2. Username: `superadmin`, Password: `admin123`
3. Barcha markazlar va foydalanuvchilarni boshqaring

### Markaz Admini:
1. Super Admin tomonidan yaratilgan akkaunt bilan kiring
2. O'z markazingizni boshqaring
3. O'quvchilar, o'qituvchilar va to'lovlarni nazorat qiling

### O'quvchi:
1. Telegram Bot orqali ro'yxatdan o'ting
2. Marketplace'dan markaz tanlang
3. Shaxsiy kabinetda kurslar, to'lovlar va natijalarni ko'ring

### Guest (Mehmon):
1. Marketplace'da markazlarni ko'ring va qidiring
2. Xaritada joylashuvni ko'ring
3. Ro'yxatdan o'tish uchun login qiling

---

## 🗺 Xususiyatlar

### 1. Reyting Algoritmi
```python
Rating = (AvgResults × 0.5) + (StudentCount × 0.3) + (Reviews × 0.2)
```

### 2. Dashboard Analytics
- O'quvchilar dinamikasi (Line Chart)
- To'lovlar statistikasi (Doughnut Chart)
- Churn Rate (O'quvchilarning ketish koeffitsiyenti)
- O'qituvchilar KPI

### 3. Geolocation
- Leaflet.js orqali interactive xarita
- Markaz joylashuvini ko'rish
- Yaqin markazlarni topish

### 4. Notification System
- To'lov muddati tugagan o'quvchilarga avtomatik eslatma
- Telegram orqali bildirishnoma yuborish

---

## 🔧 Sozlamalar

### Ma'lumotlar Bazasi
`database.py` faylidagi `DATABASE` o'zgaruvchisi:
```python
DATABASE = 'edumarket.db'
```

### Flask Secret Key
`app.py` faylidagi `secret_key`:
```python
app.secret_key = 'edumarket_secret_key_2025'
```

### Upload Directory
```python
app.config['UPLOAD_FOLDER'] = 'uploads/centers'
```

---

## 📱 Telegram Bot Komandalar

### Asosiy komandalar:
- `/start` - Botni boshlash / Ro'yxatdan o'tish
- `🔍 O'quv markazlarini qidirish` - Markazlar ro'yxati
- `📚 Mening kurslarim` - Faol kurslar
- `💳 To'lovlarim` - To'lovlar tarixi
- `📊 Natijalarim` - Test natijalari
- `🗺 Xaritada topish` - Web App xarita

### Tillar:
- 🇺🇿 O'zbek
- 🇷🇺 Русский
- 🇬🇧 English

---

## 🎨 Dizayn Xususiyatlari

### Color Scheme:
- **Primary:** #4F46E5 (Indigo)
- **Secondary:** #10B981 (Green)
- **Warning:** #F59E0B (Amber)
- **Danger:** #EF4444 (Red)

### Responsive Design:
- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1199px)
- ✅ Mobile (< 768px)

---

## 📖 API Endpoints

### Public API:
- `GET /api/centers` - Markazlar ro'yxati
- `GET /api/center/<id>` - Markaz detallari
- `POST /api/user/register` - Foydalanuvchi ro'yxatdan o'tishi

### Protected API:
- `POST /api/enroll` - Kursga yozilish
- `GET /api/payments` - To'lovlar
- `GET /api/attendance` - Davomat

---

## 🔐 Xavfsizlik

- ✅ SHA-256 parol shifrlash
- ✅ Session-based authentication
- ✅ Role-based access control (Super Admin, Center Admin, Teacher, Student)
- ✅ CSRF protection
- ✅ Input validation

---

## 🚀 Production Deployment

### Server Requirements:
- Python 3.9+
- 2GB RAM minimum
- 10GB Disk space
- SSL Certificate (HTTPS)

### Recommended Stack:
```bash
# Nginx + Gunicorn
gunicorn --bind 0.0.0.0:5000 app:app

# Supervisor for process management
# Nginx for reverse proxy
```

### Environment Variables:
```bash
export FLASK_ENV=production
export FLASK_APP=app.py
export BOT_TOKEN=your_bot_token
export SECRET_KEY=your_secret_key
```

---

## 📝 License

MIT License - Bu loyihani erkin foydalanishingiz mumkin.

---

## 👨‍💻 Muallif

**AIRITOM Logistics Center**
- 📧 Email: info@edumarket.uz
- 📱 Telegram: @edumarket_bot

---

## 🤝 Yordam va Qo'llab-quvvatlash

Muammolar yoki savollar bo'lsa:
1. GitHub Issues
2. Telegram: @edumarket_support
3. Email: support@edumarket.uz

---

## 🔄 Yangilanishlar

### v1.0.0 (2025-01-04)
- ✅ Asosiy funksiyalar
- ✅ 3 ta tilda Telegram Bot
- ✅ Marketplace va Dashboards
- ✅ Interactive Map
- ✅ Analytics va Reports

---

**🎓 EduMarket - O'quvchilar va o'quv markazlari uchun yagona platforma!**
