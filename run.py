#!/usr/bin/env python3
"""
EduMarket System - Quick Start Script
Bu script tizimni tez ishga tushirish uchun
"""

import subprocess
import sys
import os

def print_banner():
    banner = """
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║      🎓 EduMarket & Management System         ║
    ║                                               ║
    ║   O'quv Markazlari Boshqaruv Tizimi          ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
    """
    print(banner)

def check_requirements():
    """Check if required packages are installed"""
    print("🔍 Checking requirements...")
    try:
        import flask
        import telegram
        print("✅ All requirements installed")
        return True
    except ImportError as e:
        print(f"❌ Missing requirement: {e}")
        print("\n💡 Installing requirements...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        return True

def initialize_database():
    """Initialize database if not exists"""
    if not os.path.exists('edumarket.db'):
        print("\n📦 Initializing database...")
        import database
        database.init_db()
        print("✅ Database initialized")
        
        # Ask if user wants demo data
        response = input("\n❓ Do you want to create demo data? (y/n): ").lower()
        if response == 'y':
            print("\n🔄 Creating demo data...")
            import create_demo_data
            create_demo_data.create_demo_data()
    else:
        print("✅ Database already exists")

def run_web_app():
    """Run Flask web application"""
    print("\n🚀 Starting Web Application...")
    print("📍 Web Interface: http://localhost:5000")
    print("🔑 Super Admin: superadmin / admin123")
    print("\n⏹  Press Ctrl+C to stop\n")
    
    subprocess.run([sys.executable, 'app.py'])

def run_telegram_bot():
    """Run Telegram bot"""
    print("\n🤖 Starting Telegram Bot...")
    print("⚠️  Remember to set BOT_TOKEN in bot/telegram_bot.py")
    print("\n⏹  Press Ctrl+C to stop\n")
    
    subprocess.run([sys.executable, 'bot/telegram_bot.py'])

def main():
    print_banner()
    
    # Check requirements
    check_requirements()
    
    # Initialize database
    initialize_database()
    
    # Show menu
    print("\n" + "="*50)
    print("Select an option:")
    print("="*50)
    print("1. Run Web Application")
    print("2. Run Telegram Bot")
    print("3. Run Both (Web + Bot)")
    print("4. Create Demo Data")
    print("5. Exit")
    print("="*50)
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        run_web_app()
    elif choice == '2':
        run_telegram_bot()
    elif choice == '3':
        print("\n🚀 Starting both services...")
        print("⚠️  Open 2 terminal windows and run:")
        print("   Terminal 1: python app.py")
        print("   Terminal 2: python bot/telegram_bot.py")
    elif choice == '4':
        print("\n🔄 Creating demo data...")
        import create_demo_data
        create_demo_data.create_demo_data()
    elif choice == '5':
        print("\n👋 Goodbye!")
        sys.exit(0)
    else:
        print("\n❌ Invalid choice!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down gracefully...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
