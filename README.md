<div style="font-family: Arial, sans-serif; line-height:1.6;">

<h1 style="color:#2c3e50;">🚀 Django Blog Project</h1>
<h3 style="color:#555;">By Harshdeep Singh</h3>

<hr style="border:1px solid #ddd;">

<h2 style="color:#34495e;">👋 Welcome</h2>
<p>
This repository contains the source code for the <strong>Django Blogging Systemstrong>.
It is a real-world, feature-rich blogging platform built to teach practical Django development —
from models and templates to authentication, dashboards, permissions, and deployment.
</p>

<hr style="border:1px solid #eee;">

<h2 style="color:#34495e;">📚 What You'll Learn</h2>
<ul>
<li>✔ Real-world project structure & folder layout</li>
<li>✔ Models: Blog, Category, Comment, User relations, slugs</li>
<li>✔ Forms: Create/Edit posts, registration, comments</li>
<li>✔ Authentication & Authorization (Groups & Permissions)</li>
<li>✔ Admin customization</li>
<li>✔ Role-based dashboards (Admin / Manager / Editor / Author)</li>
<li>✔ Search, pagination, featured & recent posts</li>
<li>✔ Media & static file handling</li>
<li>✔ Production deployment checklist</li>
</ul>

<hr style="border:1px solid #eee;">

<h2 style="color:#34495e;">✨ Features Implemented</h2>
<ul>
<li>🔐 Multi-role permission system</li>
<li>📝 Full CRUD for posts & categories</li>
<li>🔗 Unique slug generation</li>
<li>🖼 Image upload & media configuration</li>
<li>💬 Authenticated comment system</li>
<li>📊 Manager & Editor dashboards</li>
<li>🔎 Search with retained query</li>
<li>🚀 Deployment-ready setup</li>
</ul>

<hr style="border:1px solid #eee;">

<h2 style="color:#34495e;">⚙ Requirements</h2>
<ul>
<li>Python 3.10+</li>
<li>Django 4.x (latest recommended)</li>
<li>Virtual Environment (venv)</li>
<li>PostgreSQL / MySQL / SQLite</li>
</ul>

<hr style="border:1px solid #eee;">

<h2 style="color:#34495e;">📦 Installation</h2>

<pre style="background:#f4f4f4; padding:10px; border-radius:5px;">
git clone &lt;your-repo-url&gt;
cd project-folder
python -m venv venv
source venv/bin/activate  (Mac/Linux)
venv\Scripts\activate     (Windows)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
</pre>

<hr style="border:1px solid #eee;">

<h2 style="color:#34495e;">🌍 Deployment Notes</h2>
<ul>
<li>Set <code>DEBUG = False</code></li>
<li>Configure <code>ALLOWED_HOSTS</code></li>
<li>Setup static & media files</li>
<li>Use environment variables for secrets</li>
<li>Demo Link - https://deepcode22.pythonanywhere.com/</li>
</ul>

<hr style="border:1px solid #eee;">

<h2 style="color:#34495e;">🐳 Docker Image</h2>

<p>
This project is also containerized and available on <strong>Docker Hub</strong>.
You can quickly run the blogging system using the pre-built Docker image.
</p>

<ul>
<li>📦 Image Name: <code>deepcode22/blog</code></li>
<li>🌐 Docker Hub: https://hub.docker.com/repository/docker/deepcode22/blog/general</li>
</ul>

<h3 style="color:#555;">Run using Docker</h3>

<pre style="background:#f4f4f4; padding:10px; border-radius:5px;">
docker pull deepcode22/blog
docker run -p 8000:8000 deepcode22/blog
</pre>

<p>
After running the container, open:
</p>

<pre style="background:#f4f4f4; padding:10px; border-radius:5px;">
http://127.0.0.1:8000
</pre>

<hr style="border:1px solid #ddd;">

<p style="text-align:center; color:#777;">
© 2026Harshdeep Singh — Premium Django Blogging System
</p>

</div>
