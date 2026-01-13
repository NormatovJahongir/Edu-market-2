import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css"; // Tailwind va asosiy stillar uchun
import Link from "next/link";
import { 
  GraduationCap, Home, MapPinned, 
  LayoutDashboard, LogOut, LogIn, 
  Phone, Mail, Send, Instagram, Facebook 
} from "lucide-react";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "EduMarket & Management System",
  description: "O'quv markazlari uchun yagona platforma",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  // Bu qismlar keyinchalik haqiqiy auth va til bilan almashtiriladi
  const isLoggedIn = false; 
  const userRole = 'student'; 

  return (
    <html lang="uz">
      <body className={`${inter.className} min-h-screen flex flex-col bg-gray-50 text-gray-900`}>
        
        {/* Navigation */}
        <nav className="bg-white border-b sticky top-0 z-50 shadow-sm">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16 items-center">
              
              {/* Brand */}
              <Link href="/" className="flex items-center gap-2 group">
                <div className="bg-blue-600 p-2 rounded-lg group-hover:bg-blue-700 transition">
                  <GraduationCap className="text-white" size={24} />
                </div>
                <span className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600">
                  EduMarket
                </span>
              </Link>

              {/* Nav Links */}
              <div className="hidden md:flex items-center gap-6">
                <Link href="/" className="flex items-center gap-1.5 text-gray-600 hover:text-blue-600 transition font-medium">
                  <Home size={18} /> Marketplace
                </Link>
                <Link href="/map" className="flex items-center gap-1.5 text-gray-600 hover:text-blue-600 transition font-medium">
                  <MapPinned size={18} /> Xarita
                </Link>

                {isLoggedIn ? (
                  <>
                    <Link 
                      href={userRole === 'super_admin' ? '/admin/dashboard' : '/student/dashboard'} 
                      className="flex items-center gap-1.5 text-gray-600 hover:text-blue-600 transition font-medium"
                    >
                      <LayoutDashboard size={18} /> Dashboard
                    </Link>
                    <button className="flex items-center gap-1.5 text-red-500 hover:text-red-600 transition font-medium">
                      <LogOut size={18} /> Chiqish
                    </button>
                  </>
                ) : (
                  <Link href="/login" className="bg-blue-600 text-white px-5 py-2 rounded-full flex items-center gap-2 hover:bg-blue-700 transition font-medium shadow-md shadow-blue-100">
                    <LogIn size={18} /> Kirish
                  </Link>
                )}
                
                {/* Lang Switcher */}
                <div className="flex gap-2 border-l pl-6 ml-2">
                  <button className="text-xs font-bold text-blue-600 border-b-2 border-blue-600">UZ</button>
                  <button className="text-xs font-bold text-gray-400 hover:text-gray-600">RU</button>
                  <button className="text-xs font-bold text-gray-400 hover:text-gray-600">EN</button>
                </div>
              </div>
            </div>
          </div>
        </nav>

        {/* Main Content */}
        <main className="flex-grow container mx-auto px-4 py-8 max-w-7xl">
          {children}
        </main>

        {/* Footer */}
        <footer className="bg-white border-t mt-auto">
          <div className="max-w-7xl mx-auto px-4 py-12 sm:px-6 lg:px-8">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-12 text-center md:text-left">
              
              <div className="space-y-4">
                <div className="flex items-center justify-center md:justify-start gap-2">
                  <GraduationCap className="text-blue-600" size={28} />
                  <h3 className="text-xl font-bold">EduMarket</h3>
                </div>
                <p className="text-gray-500 max-w-xs mx-auto md:mx-0">
                  O'quv markazlari uchun yagona platforma va boshqaruv tizimi.
                </p>
              </div>

              <div className="space-y-4">
                <h4 className="font-bold text-gray-900">Bog'lanish</h4>
                <ul className="space-y-3 text-gray-500">
                  <li className="flex items-center justify-center md:justify-start gap-2">
                    <Phone size={18} className="text-blue-600" /> +998 99 295 49 57
                  </li>
                  <li className="flex items-center justify-center md:justify-start gap-2">
                    <Mail size={18} className="text-blue-600" /> info@edumarket.uz
                  </li>
                </ul>
              </div>

              <div className="space-y-4">
                <h4 className="font-bold text-gray-900">Ijtimoiy tarmoqlar</h4>
                <div className="flex justify-center md:justify-start gap-4">
                  <a href="#" className="bg-gray-100 p-3 rounded-full hover:bg-blue-50 hover:text-blue-600 transition">
                    <Send size={20} />
                  </a>
                  <a href="#" className="bg-gray-100 p-3 rounded-full hover:bg-pink-50 hover:text-pink-600 transition">
                    <Instagram size={20} />
                  </a>
                  <a href="#" className="bg-gray-100 p-3 rounded-full hover:bg-blue-100 hover:text-blue-800 transition">
                    <Facebook size={20} />
                  </a>
                </div>
              </div>

            </div>
            <div className="border-t mt-12 pt-8 text-center text-gray-400 text-sm">
              <p>&copy; {new Date().getFullYear()} EduMarketBiznes. Barcha huquqlar himoyalangan.</p>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
