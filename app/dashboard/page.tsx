"use client";

import React from 'react';
import { 
  UserCircle, BookOpen, CalendarCheck, 
  ChartLine, Wallet, School, UserTie, 
  Calendar, Check, X, Clock, ChevronRight,
  GraduationCap, Info
} from 'lucide-react';
import Link from 'next/link';

export default function StudentDashboard() {
  // Mock data - bular API orqali keladi
  const stats = [
    { label: "Faol kurslar", value: "3", icon: BookOpen, color: "text-blue-600", bg: "bg-blue-50" },
    { label: "Qatnashgan darslar", value: "42", icon: CalendarCheck, color: "text-emerald-600", bg: "bg-emerald-50" },
    { label: "O'rtacha natija", value: "85%", icon: ChartLine, color: "text-purple-600", bg: "bg-purple-50" },
    { label: "To'lovlar kutilmoqda", value: "1", icon: Wallet, color: "text-orange-600", bg: "bg-orange-50" },
  ];

  return (
    <div className="space-y-8 pb-10">
      {/* Welcome Header */}
      <header className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white p-8 rounded-[2rem] border border-gray-100 shadow-sm">
        <div className="flex items-center gap-4">
          <div className="bg-blue-600 p-3 rounded-2xl text-white">
            <UserCircle size={40} />
          </div>
          <div>
            <h1 className="text-2xl md:text-3xl font-bold text-gray-900">Xush kelibsiz, Jamshid!</h1>
            <p className="text-gray-500">Sizning o'quv jarayoningiz haqida barcha ma'lumotlar</p>
          </div>
        </div>
        <Link href="/profile" className="flex items-center gap-2 text-blue-600 font-semibold hover:underline">
          Profilni tahrirlash <ChevronRight size={18} />
        </Link>
      </header>

      {/* Stats Grid */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, idx) => (
          <div key={idx} className="bg-white p-6 rounded-3xl border border-gray-100 shadow-sm">
            <div className={`${stat.bg} ${stat.color} w-12 h-12 rounded-2xl flex items-center justify-center mb-4`}>
              <stat.icon size={24} />
            </div>
            <div className="text-2xl font-black text-gray-900">{stat.value}</div>
            <div className="text-sm text-gray-500 font-medium">{stat.label}</div>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Column: Courses & Attendance */}
        <div className="lg:col-span-2 space-y-8">
          {/* My Courses Section */}
          <section className="bg-white p-6 rounded-[2rem] border border-gray-100 shadow-sm">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-bold flex items-center gap-2">
                <GraduationCap className="text-blue-600" /> Mening kurslarim
              </h2>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <CourseCard 
                title="Frontend Dasturlash" 
                center="Zehn Akademiyasi" 
                teacher="Anvar Toshkentov" 
                status="Faol" 
                date="12.10.2025"
              />
              <CourseCard 
                title="IELTS 7.5+" 
                center="Everest Learning" 
                teacher="Sarah Jenkins" 
                status="Yakunlangan" 
                date="05.08.2025"
              />
            </div>
          </section>

          {/* Attendance Tracker */}
          <section className="bg-white p-6 rounded-[2rem] border border-gray-100 shadow-sm">
            <h2 className="text-xl font-bold flex items-center gap-2 mb-6">
              <Calendar className="text-blue-600" /> Davomat (Oxirgi 10 dars)
            </h2>
            <div className="flex flex-wrap gap-3">
              {[...Array(10)].map((_, i) => (
                <div key={i} className={`flex flex-col items-center p-3 rounded-2xl border-2 transition-all ${i % 3 === 0 ? 'border-red-100 bg-red-50 text-red-600' : 'border-emerald-100 bg-emerald-50 text-emerald-600'}`}>
                  <span className="text-[10px] font-bold uppercase opacity-60">Jan {10+i}</span>
                  {i % 3 === 0 ? <X size={20} /> : <Check size={20} />}
                </div>
              ))}
            </div>
          </section>
        </div>

        {/* Right Column: Results & Payments */}
        <div className="space-y-8">
          {/* Results Section */}
          <section className="bg-white p-6 rounded-[2rem] border border-gray-100 shadow-sm">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-bold flex items-center gap-2">
                <ChartLine className="text-purple-600" size={20} /> Natijalar
              </h2>
            </div>
            <div className="space-y-4">
              <ResultItem name="Mok-IELTS Writing" score={75} />
              <ResultItem name="React.js Basic Test" score={92} />
              <ResultItem name="JavaScript Algorithm" score={60} />
            </div>
          </section>

          {/* Payments Section */}
          <section className="bg-white p-6 rounded-[2rem] border border-gray-100 shadow-sm">
            <h2 className="text-xl font-bold flex items-center gap-2 mb-6">
              <Wallet className="text-orange-600" size={20} /> To'lovlar
            </h2>
            <div className="space-y-4">
              <PaymentItem center="Zehn Akad." amount="800,000" status="To'langan" color="text-emerald-600" />
              <PaymentItem center="Everest Learn." amount="1,200,000" status="Kutilmoqda" color="text-orange-600" />
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}

// Sub-components for cleaner code
function CourseCard({ title, center, teacher, status, date }: any) {
  return (
    <div className="p-5 rounded-2xl border border-gray-100 bg-gray-50/50 hover:bg-white hover:shadow-md transition-all group">
      <div className="flex justify-between items-start mb-3">
        <h3 className="font-bold text-gray-900 group-hover:text-blue-600">{title}</h3>
        <span className={`px-2 py-1 rounded-lg text-[10px] font-bold uppercase ${status === 'Faol' ? 'bg-emerald-100 text-emerald-700' : 'bg-gray-200 text-gray-600'}`}>
          {status}
        </span>
      </div>
      <div className="space-y-1.5 mb-4">
        <p className="text-xs text-gray-500 flex items-center gap-1.5"><School size={12} /> {center}</p>
        <p className="text-xs text-gray-500 flex items-center gap-1.5"><UserTie size={12} /> {teacher}</p>
      </div>
      <div className="flex items-center justify-between pt-3 border-t">
        <span className="text-[10px] text-gray-400 flex items-center gap-1"><Calendar size={10} /> {date}</span>
        <button className="text-xs font-bold text-blue-600 flex items-center gap-1">Batafsil <ChevronRight size={14} /></button>
      </div>
    </div>
  );
}

function ResultItem({ name, score }: any) {
  return (
    <div className="flex items-center justify-between p-3 bg-gray-50 rounded-xl">
      <div className="text-sm font-medium text-gray-700">{name}</div>
      <div className={`font-bold ${score >= 80 ? 'text-emerald-600' : score >= 70 ? 'text-blue-600' : 'text-orange-600'}`}>
        {score}%
      </div>
    </div>
  );
}

function PaymentItem({ center, amount, status, color }: any) {
  return (
    <div className="flex items-center justify-between p-3 border-b border-dashed last:border-0">
      <div>
        <div className="text-sm font-bold text-gray-800">{center}</div>
        <div className="text-[10px] text-gray-400">{amount} so'm</div>
      </div>
      <div className={`text-xs font-bold ${color}`}>{status}</div>
    </div>
  );
}
