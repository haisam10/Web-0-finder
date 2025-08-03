# Web-0-finder

## Project Overview  
**Web-0-finder** একটি Python স্ক্রিপ্ট যা একটি ওয়েবসাইটের শুরু URL থেকে একই ডোমেইনের সব পেজের লিঙ্কগুলো ক্রল করে।  
প্রতিটি পেজে লিঙ্কের সংখ্যা গোনে এবং URL গুলোর মধ্যে থাকা numeric `id` কুয়েরি প্যারামিটারগুলো আলাদা করে সংগ্রহ করে।

## Features  
- ওয়েবসাইটের অভ্যন্তরীণ সকল পেজ ব্রাউজ করে  
- প্রতিটি পেজে থাকা লিঙ্কের সংখ্যা রিপোর্ট করে  
- URL এর মধ্যে থাকা numeric `id` কুয়েরি প্যারামিটার খুঁজে বের করে  
- বাহিরের ডোমেইনের লিঙ্কগুলো স্ক্যান করে না  
- সহজ ও ব্যবহার বান্ধব কমান্ড-লাইন ইন্টারফেস  

## Requirements  
- Python 3.x  
- requests লাইব্রেরি  
- beautifulsoup4 লাইব্রেরি  

## Installation  
🛠️ Installation
প্রথমে তোমার সিস্টেমে Python 3.x ইনস্টল আছে কি না নিশ্চিত হও। এরপর নিচের ধাপগুলো অনুসরণ করো:

১. প্রজেক্টটি ক্লোন করুন (অথবা কোড ডাউনলোড করুন):
bash
Copy
Edit
git clone https://github.com/your-username/web-0-finder.git
cd web-0-finder
২. প্রয়োজনীয় লাইব্রেরিগুলো ইনস্টল করুন:
bash
Copy
Edit
pip install requests beautifulsoup4
✅ বিকল্পভাবে আপনি চাইলে requirements.txt ফাইল ব্যবহার করেও ইনস্টল করতে পারেন (যদি থাকে):

bash
Copy
Edit
pip install -r requirements.txt
৩. প্রোগ্রামটি চালান:
bash
Copy
Edit
python web_0_finder.py
🔔 নোট:

Windows-এ python এর বদলে python3 কমান্ড লাগতে পারে

MacOS/Linux-এও একইভাবে ব্যবহারযোগ্য
```bash
pip install requests beautifulsoup4

MD Haisam Hoque
Portfolio
Made in Bangladesh 🇧🇩

Happy Hacking (^-^)
