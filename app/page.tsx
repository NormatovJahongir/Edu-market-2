"use client";

import React, { useState } from 'react';
import { 
  Search, Filter, School, Users, 
  BookOpen, Star, Rocket, Info, 
  UserPlus, Store, GraduationCap 
} from 'lucide-react';
import Link from 'next/link';

export default function MarketplacePage() {
  const [searchTerm, setSearchTerm] = useState("");

  // Mock ma'lumotlar (Backend ulanganda API orqali keladi)
  const centers = [
    { id: 1, name: "Zehn Akademiyasi", rating: 4.9, students: 1200, subjects: 12, address: "Chilonzor", desc: "Zamonaviy IT va xorijiy tillar markazi." },
    { id: 2, name: "Smart School", rating: 4.5, students: 850, subjects: 8, address: "Yunusobod", desc: "Matematika va fizika fanlariga ixtisoslashgan." },
    { id: 3, name: "Everest Learning", rating: 4.7, students: 2100, subjects: 15, address: "Mirzo Ulug'bek", desc: "IELTS va til o'rgatish bo'yicha yetakchi." },
  ];

  return (
    <div className="space-y-12 pb-20">
      
      {/* Hero Section */}
      <section className="relative overflow-hidden bg-blue-600 rounded-[2.5rem] py-16 px-8 text-center text-white shadow-2xl">
        <div className="absolute top-0 right-0 -mt-10 -mr-10 w-64 h-64 bg-white/10 rounded-full blur-3xl"></div>
        <div className="relative z-10 max-w-3xl mx-auto space-y-6">
          <div className="inline-flex items-center gap-2 bg-white/20 px-4 py-2 rounded-full backdrop-blur-md text-sm font-medium">
            <Store size={18} /> O'quv markazlari bozori
          </div>
          <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight">
            Kelajagingiz uchun eng yaxshi bilim maskanini toping
          </h1>
          <p className="text-blue-100 text-lg md:text-xl max-w-2xl mx-auto">
            Barcha o'quv markazlari endi yagona platformada. Solishtiring, sharhlarni o'qing va bir marta bosish bilan ro'yxatdan o'ting.
          </p>

          {/* Search Bar */}
          <div className="max-w-2xl mx-auto flex flex-col md:flex-row gap-3 bg-white p-2 rounded-2xl shadow-xl">
            <div className="flex-1 relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" size={20} />
              <input 
                type="text" 
                placeholder="Markaz nomi, fan yoki manzil..."
                className="w-full pl-12 pr-4 py-3 text-gray-800 outline-none rounded-xl"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
            <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-xl font-bold transition flex items-center justify-center gap-2">
              <Search size={18} /> Qidirish
            </button>
          </div>
        </div>
      </section>

      {/* Statistics */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard icon={School} value="150+" label="Markazlar" color="blue" />
        <StatCard icon={Users} value="25,000+" label="O'quvchilar" color="indigo" />
        <StatCard icon={BookOpen} value="400+" label="Kurslar" color="emerald" />
        <StatCard icon={Star} value="4.8" label="O'rtacha reyting" color="amber" />
      </div>

      {/* Centers Grid */}
      <section className="space-y-8">
        <div className="flex items-center justify-between border-b pb-4">
          <h2 className="text-2xl font-bold flex items-center gap-2">
            <Rocket className="text-orange-500" /> Mashhur markazlar
          </h2>
          <div className="flex gap-2">
            <select className="bg-white border rounded-lg px-3 py-1.5 text-sm outline-none">
              <option>Barcha fanlar</option>
              <option>IT / Dasturlash</option>
              <option>Ingliz tili</option>
            </select>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {centers.map((center) => (
            <div key={center.id} className="bg-white rounded-3xl border border-gray-100 shadow-sm hover:shadow-xl transition-all duration-300 overflow-hidden group">
              <div className="h-48 bg-gray-100 relative overflow-hidden">
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent z-10"></div>
                {/* Markaz Logosi o'rniga rangli fon yoki rasm */}
                <div className="absolute inset-0 flex items-center justify-center text-gray-300">
                  <GraduationCap size={64} />
                </div>
                <div className="absolute top-4 right-4 z-20 bg-white px-2 py-1 rounded-lg flex items-center gap-1 text-sm font-bold shadow-sm">
                  <Star size={14} className="text-yellow-500 fill-yellow-500" /> {center.rating}
                </div>
              </div>
              
              <div className="p-6 space-y-4">
                <h3 className="text-xl font-bold group-hover:text-blue-600 transition">{center.name}</h3>
                <p className="text-gray-500 text-sm line-clamp-2">{center.desc}</p>
                
                <div className="grid grid-cols-2 gap-4 pt-2 border-t">
                  <div className="flex items-center gap-2 text-xs text-gray-400">
                    <Users size={14} className="text-blue-500" /> {center.students} o'quvchi
                  </div>
                  <div className="flex items-center gap-2 text-xs text-gray-400">
                    <BookOpen size={14} className="text-blue-500" /> {center.subjects} fan
                  </div>
                </div>

                <div className="flex gap-2 pt-2">
                  <Link 
                    href={`/center/${center.id}`} 
                    className="flex-1 bg-gray-50 text-gray-700 py-3 rounded-xl text-center font-bold hover:bg-gray-100 transition flex items-center justify-center gap-1"
                  >
                    <Info size={16} /> Batafsil
                  </Link>
                  <Link 
                    href={`/center/${center.id}#enroll`} 
                    className="flex-1 bg-blue-600 text-white py-3 rounded-xl text-center font-bold hover:bg-blue-700 transition flex items-center justify-center gap-1 shadow-lg shadow-blue-100"
                  >
                    <UserPlus size={16} /> Kirish
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-slate-900 rounded-[2.5rem] p-12 text-white relative overflow-hidden">
        <div className="absolute bottom-0 right-0 w-96 h-96 bg-blue-600/20 rounded-full blur-[100px]"></div>
        <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-8 text-center md:text-left">
          <div className="space-y-4">
            <h2 className="text-3xl font-bold">O'quv markazingiz bormi?</h2>
            <p className="text-slate-400 text-lg max-w-md">
              Minglab o'quvchilarga o'z kurslaringizni taklif qiling va boshqaruvni avtomatlashtiring.
            </p>
          </div>
          <Link href="/login" className="bg-white text-slate-900 px-10 py-4 rounded-2xl font-bold text-lg hover:bg-blue-50 transition flex items-center gap-2 shadow-xl shadow-white/5">
            <Rocket size={20} className="text-blue-600" /> Hoziroq qo'shiling
          </Link>
        </div>
      </section>

    </div>
  );
}

// Yordamchi StatCard Komponenti
function StatCard({ icon: Icon, value, label, color }: any) {
  const colors: any = {
    blue: "bg-blue-50 text-blue-600",
    indigo: "bg-indigo-50 text-indigo-600",
    emerald: "bg-emerald-50 text-emerald-600",
    amber: "bg-amber-50 text-amber-600"
  };

  return (
    <div className="bg-white p-6 rounded-3xl border border-gray-100 shadow-sm flex items-center gap-4">
      <div className={`${colors[color]} p-4 rounded-2xl`}>
        <Icon size={28} />
      </div>
      <div>
        <div className="text-2xl font-bold text-gray-900">{value}</div>
        <div className="text-sm text-gray-500">{label}</div>
      </div>
    </div>
  );
}
