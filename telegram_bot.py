import os
import logging
import hashlib
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)
from database import get_db, init_db

# Logging sozlamalari
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot Tokeni (Render Environment Variable'dan olish tavsiya etiladi)
TOKEN = "8383832866:AAHr35OWeBfuKdbnSLRq_rqAmKXytns2Z2s"

# Holatlar (Conversation states)
FULL_NAME, PHONE, LANGUAGE = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Botni boshlash va foydalanuvchini tekshirish"""
    user = update.effective_user
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (str(user.id),))
    db_user = cursor.fetchone()
    conn.close()

    if db_user:
        welcome_text = {
            'uz': f"Xush kelibsiz, {db_user['full_name']}! Saytga kirish uchun login: {db_user['username']}",
            'ru': f"Добро пожаловать, {db_user['full_name']}! Ваш логин: {db_user['username']}",
            'en': f"Welcome, {db_user['full_name']}! Your login: {db_user['username']}"
        }
        lang = db_user['language'] if db_user['language'] in welcome_text else 'uz'
        await update.message.reply_text(welcome_text[lang])
        return ConversationHandler.END
    else:
        await update.message.reply_text(
            "Assalomu alaykum! Edu Market botiga xush kelibsiz.\n"
            "Ro'yxatdan o'tish uchun to'liq ismingizni kiriting (F.I.O):"
        )
        return FULL_NAME

async def get_full_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ismni saqlash"""
    context.user_data['full_name'] = update.message.text
    await update.message.reply_text("Telefon raqamingizni yuboring (masalan: +998901234567):")
    return PHONE

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Telefonni saqlash va tilni so'rash"""
    context.user_data['phone'] = update.message.text
    
    reply_keyboard = [['O\'zbekcha', 'Русский', 'English']]
    await update.message.reply_text(
        "Muloqot tilini tanlang:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True),
    )
    return LANGUAGE

async def get_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ma'lumotlarni bazaga saqlash va tugatish"""
    lang_map = {'O\'zbekcha': 'uz', 'Русский': 'ru', 'English': 'en'}
    selected_lang = lang_map.get(update.message.text, 'uz')
    
    user = update.effective_user
    full_name = context.user_data['full_name']
    phone = context.user_data['phone']
    # Username sifatida telegram id yoki random nom (saytga kirish uchun)
    username = f"user_{user.id}"
    
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (telegram_id, username, full_name, phone, language, role, status)
            VALUES (?, ?, ?, ?, ?, 'student', 'active')
        ''', (str(user.id), username, full_name, phone, selected_lang))
        conn.commit()
        
        success_text = {
            'uz': f"Muvaffaqiyatli ro'yxatdan o'tdingiz!\nLogin: {username}\nSaytda kurslarni ko'rishingiz mumkin.",
            'ru': f"Вы успешно зарегистрировались!\nЛогин: {username}",
            'en': f"Success! Your login: {username}"
        }
        await update.message.reply_text(success_text[selected_lang], reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logger.error(f"Xatolik: {e}")
        await update.message.reply_text("Xatolik yuz berdi. Qaytadan urinib ko'ring.")
    finally:
        conn.close()

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Amal bekor qilindi.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main():
    """Botni ishga tushirish (bu funksiya app.py dan chaqiriladi)"""
    # Bazani tekshirish
    init_db()

    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FULL_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_full_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            LANGUAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_language)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conv_handler)
    
    # Render'da bot polling rejimida ishlaydi
    print("Bot pollingni boshladi...")
    application.run_polling()

if __name__ == '__main__':
    main()
