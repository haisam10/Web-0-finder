# Web-0-finder
Project Overview
Web-0-finder একটি Python স্ক্রিপ্ট যা একটি ওয়েবসাইটের শুরু URL থেকে একই ডোমেইনের সব পেজের লিঙ্কগুলো ক্রল করে।
প্রতিটি পেজে লিঙ্কের সংখ্যা গোনে এবং URL গুলোর মধ্যে থাকা numeric id কুয়েরি প্যারামিটারগুলো আলাদা করে সংগ্রহ করে।

Features
ওয়েবসাইটের অভ্যন্তরীণ সকল পেজ ব্রাউজ করে

প্রতিটি পেজে থাকা লিঙ্কের সংখ্যা রিপোর্ট করে

URL এর মধ্যে থাকা numeric id কুয়েরি প্যারামিটার খুঁজে বের করে

বাহিরের ডোমেইনের লিঙ্কগুলো স্ক্যান করে না

সহজ ও ব্যবহার বান্ধব কমান্ড-লাইন ইন্টারফেস

Requirements
Python 3.x

requests লাইব্রেরি

beautifulsoup4 লাইব্রেরি

Installation
লাইব্রেরিগুলো ইনস্টল করতে:

bash
Copy
Edit
pip install requests beautifulsoup4
Usage
bash
Copy
Edit
python web_0_finder.py
প্রোগ্রাম রান করার পর URL দিতে হবে, যেমন:

php
Copy
Edit
Give your URL (include http:// or https://): https://example.com
তারপর প্রোগ্রাম ওয়েবসাইট ক্রল করবে এবং ফলাফল দেখাবে:

bash
Copy
Edit
Total pages found: 10  
Page: https://example.com --> Number of links: 5  
Page: https://example.com/about --> Number of links: 3  
...  
Found id values in URLs:  
id = 12  
id = 34  
id = 101  
Notes
URL অবশ্যই http:// অথবা https:// দিয়ে শুরু করতে হবে

বড় ওয়েবসাইটে স্ক্যান করতে সময় লাগতে পারে, ধৈর্য ধরুন

শুধুমাত্র একই ডোমেইনের লিঙ্কগুলোই ক্রল করবে

Author
MD Haisam Hoque
Portfolio
Made in Bangladesh 🇧🇩

Happy Hacking (^-^)
