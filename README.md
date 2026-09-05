# 🎬 AniDong - Anime & Donghua Online Streaming Platform

Zamonaviy, tez va barchaga ochiq Anime va Donghua (Xitoy animatsiyasi) platformasi.

---

## 🌟 Xususiyatlar (Features)

- 🇯🇵 **Anime va 🇨🇳 Donghua Bo'limlari**: Yapon va Xitoy seriallarini alohida filtrlash.
- 🎬 **Custom HD Video Player**: Qismlarni tanlash (Episode switcher), ko'rish tezligini (0.5x - 2.0x) o'zgartirish, serverlarni almashtirish va to'liq ekranda tomosha qilish.
- 🔍 **Jonli Qidiruv (Live Search)**: Seriallar va janrlar bo'yicha lahzali qidiruv.
- 🏷️ **Janrlar va Filtrlar**: Action, Fantasy, Xianxia, Supernatural, Comedy va Ovoz turlari (Sub / Dub) bo'yicha saralash.
- 💖 **Tanlanganlar (Favorites)** va 🕒 **Ko'rishlar Tarixi (Watch History)**: Foydalanuvchi ma'lumotlari brauzer `localStorage`ida saqlanadi.
- 💬 **Muhokamalar (Comments)**: Har bir epizod ostida fikr qoldirish imkoniyati.
- 📱 **Responsive Dark UI**: Mobil va kompyuterlar uchun Glassmorphic zamonaviy qora dizayn.

---

## 🚀 Mahalliy kompyuterda ishga tushirish (Local Run)

Loyiha hech qanday murakkab kutubxona va o'rnatishlarsiz Python bilan ishlaydi:

1. Terminalda loyiha papkasiga o'ting:
   ```bash
   cd C:\Users\user\.gemini\antigravity\scratch\anime-donghua-stream
   ```
2. Serverni ishga tushiring:
   ```bash
   python server.py
   ```
3. Brauzeringizda ushbu manzillardan birini oching:
   - **http://127.0.0.1:5000**
   - **http://localhost:5000**

---

## 🌐 Saytni Internetga Joylash ("Hammaga ko'rinadigan qilish")

Saytingizni butun dunyo (do'stlaringiz va barcha foydalanuvchilar) ko'ra olishi uchun quyidagi bepul hosting platformalaridan foydalanishingiz mumkin:

### 1-usul: Render.com (Tavsiya etiladi - Python Flask Server uchun)
1. Kodingizni [GitHub](https://github.com) ga yuklang (`git push`).
2. [Render.com](https://render.com) saytida ro'yxatdan o'ting va **New Web Service** tugmasini bosing.
3. GitHub repozitoriyangizni ulang.
4. **Build Command**: `pip install -r requirements.txt` (yoki `pip install flask`)
5. **Start Command**: `python server.py`
6. Render sizga tayyor `https://anidong.onrender.com` kabi bepul havola taqdim etadi!

### 2-usul: Vercel / Netlify (Statik Hosting)
1. Kodingizni GitHub ga yuklang.
2. [Vercel.com](https://vercel.com) yoki [Netlify.com](https://netlify.com) saytida ro'yxatdan o'ting.
3. Repozitoriyani import qiling va **Deploy** tugmasini bosing.
4. Bir necha soniyada barcha uchun ochiq veb-sayt havolasiga ega bo'lasiz!

---

## 📁 Loyiha Strukturasi

```
anime-donghua-stream/
├── data/
│   └── catalog.json         # Anime va Donghua seriallar bazasi
├── static/
│   ├── css/
│   │   └── styles.css       # Tailwind & Glassmorphism stillari
│   └── js/
│       └── app.js           # Frontend mantiq, player va state
├── index.html               # Asosiy HTML interfeysi
├── server.py                # Python Flask REST API va fayl serveri
└── README.md                # Qo'llanma va hujjatlar
```
