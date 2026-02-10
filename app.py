import os
from flask import Flask, render_template_string, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-999"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# --- Database Models ---
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)


# --- Base Layout Template ---
def layout(content, title="My Website"):
    return render_template_string(
        f"""
    <!DOCTYPE html>
    <html lang="th">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-50 flex flex-col min-h-screen">
        <nav class="bg-indigo-700 text-white p-4 shadow-md sticky top-0 z-50">
            <div class="container mx-auto flex justify-between items-center">
                <a href="/" class="text-2xl font-bold tracking-tight">PORTFOLIO.PY</a>
                <div class="space-x-6 hidden md:flex">
                    <a href="/" class="hover:text-indigo-200">หน้าแรก</a>
                    <a href="/about" class="hover:text-indigo-200">เกี่ยวกับเรา</a>
                    <a href="/services" class="hover:text-indigo-200">บริการ</a>
                    <a href="/portfolio" class="hover:text-indigo-200">ผลงาน</a>
                    <a href="/blog" class="hover:text-indigo-200">บล็อก</a>
                    <a href="/contact" class="hover:text-indigo-200">ติดต่อ</a>
                </div>
            </div>
        </nav>

        <main class="container mx-auto flex-grow mt-8 p-4">
            {content}
        </main>

        <footer class="bg-gray-900 text-white p-10 mt-12">
            <div class="container mx-auto text-center">
                <p>&copy; 2024 Professional Flask Project | Developed for Assignment</p>
                <div class="mt-4 space-x-4 text-sm text-gray-400">
                    <a href="/privacy" class="hover:text-white">Privacy Policy</a>
                    <a href="/terms" class="hover:text-white">Terms of Service</a>
                    <a href="/admin" class="hover:text-white">Admin Access</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """,
        title=title,
    )


# --- Routes (10 Pages) ---


@app.route("/")
def home():
    content = """
    <div class="py-16 text-center">
        <h1 class="text-6xl font-black text-indigo-900 mb-6 uppercase">Modern Web Solution</h1>
        <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">สร้างสรรค์เว็บไซต์ที่มีประสิทธิภาพสูงด้วย Flask และเทคโนโลยีระดับโลก</p>
        <div class="flex justify-center gap-4">
            <a href="/portfolio" class="bg-indigo-600 text-white px-8 py-3 rounded-full font-bold shadow-lg hover:bg-indigo-700 transition">ดูผลงาน</a>
            <a href="/contact" class="bg-white text-indigo-600 border-2 border-indigo-600 px-8 py-3 rounded-full font-bold hover:bg-indigo-50 transition">ปรึกษาเรา</a>
        </div>
    </div>
    """
    return layout(content, "ยินดีต้อนรับ")


@app.route("/about")
def about():
    content = '<div class="max-w-4xl mx-auto"><h2 class="text-4xl font-bold mb-6">เกี่ยวกับเรา</h2><p class="text-lg leading-relaxed">เราเป็นทีมพัฒนาซอฟต์แวร์ที่มุ่งเน้นผลลัพธ์ที่ใช้งานได้จริง...</p></div>'
    return layout(content, "เกี่ยวกับเรา")


@app.route("/services")
def services():
    content = '<h2 class="text-3xl font-bold mb-8">บริการของเรา</h2><div class="grid md:grid-cols-3 gap-6"><div class="p-6 bg-white shadow rounded-lg">Web App</div><div class="p-6 bg-white shadow rounded-lg">API Design</div><div class="p-6 bg-white shadow rounded-lg">Cloud Setup</div></div>'
    return layout(content, "บริการ")


@app.route("/portfolio")
def portfolio():
    content = '<h2 class="text-3xl font-bold mb-8">ผลงานที่ผ่านมา</h2><div class="grid md:grid-cols-2 gap-4"><div class="h-40 bg-gray-200 rounded">Project A</div><div class="h-40 bg-gray-200 rounded">Project B</div></div>'
    return layout(content, "ผลงาน")


@app.route("/blog")
def blog():
    posts = BlogPost.query.all()
    posts_html = "".join([f'<div class="mb-4"><h3>{p.title}</h3></div>' for p in posts])
    return layout(
        f'<h2 class="text-3xl font-bold mb-8">บล็อกยอดนิยม</h2>{posts_html}', "บล็อก"
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        msg = ContactMessage(
            name=request.form["name"],
            email=request.form["email"],
            message=request.form["message"],
        )
        db.session.add(msg)
        db.session.commit()
        return "ขอบคุณที่ติดต่อเรา!"
    return layout(
        '<h2>ติดต่อเรา</h2><form method="POST"><input name="name" placeholder="ชื่อ" class="block w-full border p-2 mb-2"><input name="email" placeholder="อีเมล" class="block w-full border p-2 mb-2"><textarea name="message" class="block w-full border p-2 mb-2"></textarea><button class="bg-indigo-600 text-white p-2">ส่ง</button></form>',
        "ติดต่อเรา",
    )


@app.route("/admin")
def admin():
    msgs = ContactMessage.query.all()
    return layout(
        f"<h2>Admin Dashboard</h2><p>Messages total: {len(msgs)}</p>", "Admin"
    )


@app.route("/privacy")
def privacy():
    return layout("<h2>Privacy Policy</h2>", "Privacy")


@app.route("/terms")
def terms():
    return layout("<h2>Terms of Service</h2>", "Terms")


@app.route("/blog/<int:id>")
def blog_detail(id):
    return layout(f"<h2>Blog ID: {id}</h2>", "Blog Detail")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
