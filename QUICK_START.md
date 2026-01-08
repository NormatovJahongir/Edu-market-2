# 🚀 TEZKOR ISHGA TUSHIRISH

## 1. Dasturni o'rnatish

```bash
# 1. Kerakli paketlarni o'rnatish
pip install -r requirements.txt

# 2. Ma'lumotlar bazasini yaratish
python database.py

# 3. Ishga tushirish
python app.py
```

## 2. Brauzerda ochish

Web sahifa: **http://localhost:5000**

## 3. Login qilish

### Super Admin:
- **Username:** `superadmin`
- **Password:** `admin123`

## 4. Telegram Bot sozlash

1. Telegram'da **@BotFather** ga boring
2. `/newbot` komandasi bilan yangi bot yarating
3. Bot tokenni nusxalang
4. `bot/telegram_bot.py` faylidagi `BOT_TOKEN` ni yangilang:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

5. Botni ishga tushiring:

```bash
cd bot
python telegram_bot.py
```

## 5. Xususiyatlar

✅ **Marketplace** - Markazlar ro'yxati
✅ **Interactive Map** - Xaritada markazlar
✅ **Admin Dashboard** - Analitika va boshqaruv
✅ **Student Dashboard** - Shaxsiy kabinet
✅ **Telegram Bot** - 3 ta tilda (UZ, RU, EN)

## 6. Folder Strukturasi

```
EduMarket_System/
├── app.py                 # Flask web app
├── database.py            # Ma'lumotlar bazasi
├── requirements.txt       # Python paketlari
├── run.py                # Tezkor ishga tushirish
├── create_demo_data.py   # Demo data yaratish
├── README.md             # To'liq dokumentatsiya
│
├── bot/
│   └── telegram_bot.py   # Telegram bot
│
├── templates/            # HTML sahifalar
│   ├── base.html
│   ├── marketplace.html
│   ├── admin_dashboard.html
│   ├── student_dashboard.html
│   ├── center_detail.html
│   ├── map.html
│   └── login.html
│
├── static/
│   ├── css/
│   │   └── style.css     # Professional CSS
│   └── js/
│       └── main.js       # JavaScript funksiyalar
│
└── uploads/
    └── centers/          # Markazlar logolari
```

## 7. API Endpoints

### Public:
- `GET /` - Marketplace
- `GET /center/<id>` - Markaz detallari
- `GET /map` - Interactive map
- `POST /login` - Login

### API:
- `GET /api/centers` - Markazlar ro'yxati
- `GET /api/center/<id>` - Markaz ma'lumotlari
- `POST /api/user/register` - Ro'yxatdan o'tish
- `POST /api/enroll` - Kursga yozilish

## 8. Texnik Ma'lumotlar

**Backend:** Python 3.9+, Flask, SQLite
**Frontend:** HTML5, CSS3, JavaScript, Leaflet.js, Chart.js
**Bot:** python-telegram-bot

## 9. Production Deployment

```bash
# Gunicorn bilan
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 app:app

# Yoki
python app.py
```

## 10. Yordam

📧 Email: info@edumarket.uz
📱 Telegram: @edumarket_bot
🌐 Website: edumarket.uz

---

**🎓 EduMarket - O'quv markazlari uchun yagona platforma!**
