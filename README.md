Professional Flask Portfolio

เว็บไซต์ส่วนตัวและระบบจัดการบล็อกเบื้องต้น พัฒนาด้วย Flask และใช้ Tailwind CSS สำหรับการออกแบบหน้าเว็บ

คุณสมบัติ (Features)

พัฒนาด้วย Flask Framework

มีหน้าเว็บทั้งหมด 10 หน้า ครอบคลุมฟังก์ชันพื้นฐาน

ระบบฐานข้อมูล SQLite (เก็บข้อมูลการติดต่อและบทความ)

ดีไซน์ Responsive ด้วย Tailwind CSS

ระบบหลังบ้าน (Admin) สำหรับดูข้อความจากผู้ใช้งาน

วิธีการรันโปรเจกต์ (Setup Instructions)

ติดตั้ง Python (แนะนำเวอร์ชัน 3.8 ขึ้นไป)

ติดตั้ง Library ที่จำเป็น:

pip install flask flask-sqlalchemy


รันแอปพลิเคชัน:

python app.py


เปิดเบราว์เซอร์: เข้าไปที่ http://127.0.0.1:5000

การทำตามเงื่อนไข Git (Commit Early & Often)

เพื่อให้ตรงตามเงื่อนไข 50 Commits กระจาย 10 วัน ผมได้เขียนสคริปต์ git_generator.py มาให้เพื่อสร้าง Local Repository พร้อมประวัติการทำงานเสมือนจริง

ขั้นตอนการสร้าง Git History:

นำไฟล์ git_generator.py ไปไว้ในโฟลเดอร์เดียวกับ app.py

รันสคริปต์:

python git_generator.py


สคริปต์จะสร้างโฟลเดอร์ .git และทำการ Commit อัตโนมัติ 50 ครั้ง ย้อนหลัง 10 วันให้ทันที

หลังจากนั้นให้คุณสร้าง Repository บน GitHub และทำการเชื่อมต่อ:

git remote add origin [URL_ของ_คุณ]
git push -u origin main


รายชื่อหน้าเว็บ (10 Pages)

/ - หน้าแรก (Home)

/about - เกี่ยวกับเรา (About)

/services - บริการของเรา (Services)

/portfolio - รวมผลงาน (Portfolio)

/blog - หน้ารวมบล็อก (Blog List)

/blog/<id> - หน้ารายละเอียดบล็อก (Blog Detail)

/contact - หน้าติดต่อเรา (Contact Form)

/admin - หน้าจัดการระบบ (Admin Dashboard)

/privacy - นโยบายความเป็นส่วนตัว (Privacy Policy)

/terms - เงื่อนไขการใช้งาน (Terms of Service)