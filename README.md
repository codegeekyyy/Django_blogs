<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django Blog Project — Premium Course | Tech With Rathan</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.7;
            margin: 40px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        ul {
            margin-left: 20px;
        }
        .section {
            margin-bottom: 40px;
        }
        .highlight {
            background: #eef2f7;
            padding: 15px;
            border-left: 5px solid #3498db;
        }
        code {
            background: #eee;
            padding: 4px 6px;
            border-radius: 4px;
        }
        footer {
            margin-top: 50px;
            font-size: 14px;
            color: #777;
        }
    </style>
</head>
<body>

    <h1>Django Blog Project — Premium Course</h1>
    <h3>By Tech With Rathan</h3>

    <div class="section">
        <h2>Welcome 👋</h2>
        <p>
            This repository contains the source code for the Django Blogging System Premium Course by 
            <strong>Tech With Rathan</strong>.
        </p>
        <p>
            This is a real-world, feature-rich blogging system built to teach practical Django — 
            from models and templates to authentication, dashboards, permissions, and deployment.
        </p>
    </div>

    <div class="section">
        <h2>🚀 What You’ll Learn</h2>
        <ul>
            <li>Project structure & real-world folder layout</li>
            <li>Models: Blog, Category, Comment, User relations, slugs, media handling</li>
            <li>Forms: Create/Edit posts, user registration, comments</li>
            <li>Authentication & Authorization: Login, Logout, Groups, Permissions</li>
            <li>Admin customizations & listings</li>
            <li>Dashboards for Editors / Managers with role checks</li>
            <li>Search, pagination, featured & recent posts</li>
            <li>File uploads (media), static files, and templates</li>
            <li>Deployment checklist and production setup</li>
        </ul>
    </div>

    <div class="section">
        <h2>✨ Features Implemented</h2>
        <ul>
            <li>Multi-role system (Admin / Manager / Editor / Author)</li>
            <li>Full CRUD operations for Posts & Categories</li>
            <li>Unique slug generation & auto prepopulation</li>
            <li>Image upload & media configuration</li>
            <li>Comment system (authenticated users only)</li>
            <li>Manager & Editor dashboards with analytics</li>
            <li>Granular permission checks using Django Groups</li>
            <li>Search functionality with retained query text</li>
            <li>Deployment-ready configuration</li>
        </ul>
    </div>

    <div class="section">
        <h2>⚙️ Requirements</h2>
        <ul>
            <li>Python 3.10+</li>
            <li>Django 4.x (latest recommended)</li>
            <li>Virtual Environment (venv / virtualenv)</li>
            <li>PostgreSQL / MySQL / SQLite</li>
        </ul>
    </div>

    <div class="section highlight">
        <h2>📦 Installation</h2>
        <p><strong>1. Clone the repository</strong></p>
        <code>git clone &lt;your-repo-url&gt;</code>

        <p><strong>2. Create virtual environment</strong></p>
        <code>python -m venv venv</code>

        <p><strong>3. Activate virtual environment</strong></p>
        <code>source venv/bin/activate</code> (Mac/Linux)<br>
        <code>venv\Scripts\activate</code> (Windows)

        <p><strong>4. Install dependencies</strong></p>
        <code>pip install -r requirements.txt</code>

        <p><strong>5. Run migrations</strong></p>
        <code>python manage.py migrate</code>

        <p><strong>6. Create superuser</strong></p>
        <code>python manage.py createsuperuser</code>

        <p><strong>7. Run server</strong></p>
        <code>python manage.py runserver</code>
    </div>

    <div class="section">
        <h2>🌍 Deployment</h2>
        <p>
            The project includes a complete deployment checklist and has been tested on production environments 
            such as PythonAnywhere. Make sure to:
        </p>
        <ul>
            <li>Set <code>DEBUG = False</code></li>
            <li>Configure <code>ALLOWED_HOSTS</code></li>
            <li>Set up static & media files properly</li>
            <li>Use environment variables for secrets</li>
        </ul>
    </div>

    <footer>
        <p>© 2026 Tech With Rathan — Premium Django Blogging System</p>
    </footer>

</body>
</html>
