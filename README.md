````markdown
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=240&color=0:dc2626,100:0f172a&text=Clash%20of%20Saied&fontColor=ffffff&fontSize=50&fontAlignY=40&desc=2D%20Action%20Side-Scroller%20Game%20with%20Pygame&descAlignY=63&animation=twinkling" width="100%" />

# 🎮 بازی اکشن دو بعدی سعید (با فیزیک پرش و سیستم شلیک)

### توسعه داده شده توسط تیم تخصصی CODE RAH 💻

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-00979D?style=for-the-badge)
![GameDev](https://img.shields.io/badge/Game%20Development-7A42F4?style=for-the-badge)
![Physics](https://img.shields.io/badge/Game%20Physics-dc2626?style=for-the-badge)
![Collision](https://img.shields.io/badge/Collision%20Detection-00C896?style=for-the-badge)
![Sprite](https://img.shields.io/badge/Sprite%20Animation-FF6B00?style=for-the-badge)

</div>

---

# 🛑 بیانیه کپی‌رایت و مالکیت معنوی

> ⚠️ این پروژه توسط **امیر فرخانی** و تیم **CODE RAH** توسعه داده شده است.
>
> استفاده، بازنشر یا آموزش این پروژه با ذکر منبع و نام **CODE RAH** مجاز است.
>
> لطفاً در صورت استفاده از پروژه، حقوق معنوی توسعه‌دهندگان را رعایت کنید.

---

# 📝 درباره پروژه

**Clash of Saied** یک بازی اکشن دو بعدی از سبک **Side-Scroller** است که با زبان **Python** و کتابخانه **Pygame** توسعه یافته است.

در این بازی کنترل شخصیت **سعید** را برعهده می‌گیرید و باید با پرش از موانع و نابود کردن دشمنان، بیشترین تعداد **Kill** را ثبت کنید.

مشخصات اصلی بازی:

- رزولوشن: `800 × 400`
- موتور فیزیک پرش و گرانش
- سیستم شلیک و برخورد گلوله
- دشمنان متحرک با AI ساده
- سیستم سلامت (HP)
- شمارنده امتیاز و Kill

---

# ⚡ ویژگی‌های فنی و معماری بازی

### 🎨 گرافیک مبتنی بر Sprite

تمامی شخصیت‌ها و عناصر بازی با استفاده از Spriteها و انیمیشن‌های روان رندر می‌شوند.

### 🦘 موتور فیزیک پرش

- Gravity: `0.60`
- Jump Velocity: `-15`

جهت ایجاد حس طبیعی در پرش و فرود بازیکن.

### 💥 سیستم برخورد

استفاده از:

```python
pygame.Rect
````

برای تشخیص برخورد بازیکن، دشمن و گلوله‌ها.

### 🤖 هوش مصنوعی دشمنان

دشمنان به صورت خودکار به سمت بازیکن حرکت می‌کنند.

### ❤️ سیستم سلامت

نمایش HP بازیکن با آیکون قلب در رابط کاربری.

### 🎯 سیستم امتیازدهی

با نابودی هر دشمن:

```text
Kill +1
```

### 🧩 ساختار ماژولار

توابع اصلی پروژه:

```python
draw_player()
move_enemies()
player_shoot()
check_collisions()
```

---

# 🚀 راهنمای نصب و اجرا

## 📥 مرحله اول: دریافت پروژه

### روش اول — Clone با Git

```bash
git clone https://github.com/CODRAH/clash-of-saied.git
cd clash-of-saied
```

### روش دوم — دانلود ZIP

از بالای صفحه GitHub روی دکمه **Code** کلیک کرده و گزینه **Download ZIP** را انتخاب کنید.

سپس فایل را Extract نمایید.

---

## 🧩 مرحله دوم: نصب Python

نسخه `Python 3.8` یا بالاتر را نصب کنید.

هنگام نصب گزینه زیر را فعال کنید:

**Add Python to PATH**

---

## 📦 مرحله سوم: نصب کتابخانه‌ها

```bash
pip install pygame
```

---

## ▶️ مرحله چهارم: اجرای بازی

```bash
python main.py
```

> اگر فایل اصلی پروژه نام دیگری دارد، آن را جایگزین `main.py` کنید.

---

# 🎮 کنترل‌های بازی

| کلید     | عملکرد                 |
| -------- | ---------------------- |
| ⬅️ LEFT  | حرکت به چپ             |
| ➡️ RIGHT | حرکت به راست           |
| ⬆️ UP    | پرش                    |
| SPACE    | شلیک                   |
| 🎯 هدف   | ثبت بیشترین تعداد Kill |

---

# 📜 قوانین بازی

* با کشتن هر دشمن یک امتیاز دریافت می‌کنید.
* برخورد دشمن با بازیکن باعث کاهش HP می‌شود.
* با صفر شدن HP بازی پایان می‌یابد.
* هدف نهایی ثبت بیشترین تعداد Kill است.

---

# 📂 ساختار پروژه

```text
clash-of-saied/
│
├── assets/
│   ├── images/
│   ├── sprites/
│   └── sounds/
│
├── main.py
├── player.py
├── enemy.py
├── bullets.py
│
└── README.md
```

---

# 🧠 درباره تیم CODE RAH

تیم **CODE RAH** در حوزه‌های زیر فعالیت می‌کند:

* 💻 برنامه‌نویسی و توسعه نرم‌افزار
* 🌐 طراحی وب و Backend
* 🤖 هوش مصنوعی و بینایی ماشین
* 🔒 امنیت سایبری
* ⚙️ اینترنت اشیاء (IoT)
* 🎮 توسعه بازی

---

# 🎓 دوره‌های آموزشی

در CODE RAH دوره‌های تخصصی زیر برگزار می‌شود:

* Python Programming
* Game Development
* Artificial Intelligence
* OpenCV & YOLO
* Cyber Security
* Web Development

---

# 🌟 نسخه‌های آینده

برنامه‌های توسعه پروژه:

* 🔊 افزودن افکت‌های صوتی
* 👹 دشمنان متنوع‌تر
* 🏆 سیستم رکورد و ذخیره امتیاز
* 🎨 بهبود جلوه‌های گرافیکی
* ⚔️ Boss Fight

---

# 🌐 ارتباط با ما

برای دریافت آموزش‌ها و دنبال کردن پروژه‌های جدید، صفحات CODE RAH را دنبال کنید.

---

<div align="center">

# 💻 CODE RAH

### کدنویسی فقط نوشتن برنامه نیست؛ ساختن آینده است.

⭐ اگر از پروژه خوشتان آمد، فراموش نکنید به آن Star بدهید ⭐

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:0f172a,100:dc2626&section=footer" width="100%" />

</div>
```
