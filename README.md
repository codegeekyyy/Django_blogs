<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Blogs - README</title>
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #34495e;
            --accent-color: #3498db;
            --text-color: #333;
            --bg-color: #f4f7f6;
            --white: #ffffff;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 900px;
            margin: 40px auto;
            background: var(--white);
            padding: 40px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }

        header {
            text-align: center;
            border-bottom: 2px solid var(--accent-color);
            margin-bottom: 30px;
            padding-bottom: 20px;
        }

        h1 {
            color: var(--primary-color);
            margin-bottom: 10px;
        }

        h2 {
            color: var(--secondary-color);
            border-left: 5px solid var(--accent-color);
            padding-left: 15px;
            margin-top: 30px;
        }

        p {
            margin-bottom: 15px;
        }

        code {
            background-color: #eee;
            padding: 2px 5px;
            border-radius: 4px;
            font-family: 'Courier New', Courier, monospace;
        }

        pre {
            background-color: #2d3436;
            color: #dfe6e9;
            padding: 20px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 0.9em;
        }

        ul {
            margin-bottom: 15px;
        }

        li {
            margin-bottom: 8px;
        }

        .badge {
            display: inline-block;
            padding: 5px 12px;
            background-color: var(--accent-color);
            color: white;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
            text-transform: uppercase;
        }

        footer {
            text-align: center;
            margin-top: 40px;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>

<body>
    <div class="container">
        <header>
            <h1>Django Blogs</h1>
            <p>A professional, feature-rich blogging platform built with Django.</p>
            <div class="badge">Django 5.2</div>
            <div class="badge">Bootstrap 4</div>
            <div class="badge">SQLite</div>
        </header>

        <section>
            <h2>Description</h2>
            <p>
                <strong>Django Blogs</strong> is a modern blogging application designed for versatility and ease of use.
                It features a clean user interface, category management, featured posts, and a responsive design powered
                by Bootstrap 4.
            </p>
        </section>

        <section>
            <h2>Key Features</h2>
            <ul>
                <li><strong>Dynamic Categories:</strong> Organize posts into various categories for better navigation.
                </li>
                <li><strong>Featured Posts:</strong> Highlight important blogs on the homepage.</li>
                <li><strong>Comment System:</strong> Engagement through comments on blog details.</li>
                <li><strong>Rich Media Support:</strong> Integrated support for featured images and media uploads.</li>
                <li><strong>Crispy Forms:</strong> Beautifully rendered Django forms using Bootstrap 4.</li>
                <li><strong>Admin Dashboard:</strong> Comprehensive admin panel for content management.</li>
            </ul>
        </section>

        <section>
            <h2>Quick Start</h2>
            <p>Follow these steps to get the project running locally:</p>
            <pre>
# Clone the repository
git clone &lt;repository_url&gt;

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver</pre>
        </section>

        <section>
            <h2>Project Structure</h2>
            <ul>
                <li><code>blogs/</code>: Main application containing models, views, and logic for the blog.</li>
                <li><code>blogs_main/</code>: Project configuration folder (settings, urls, wsgi).</li>
                <li><code>static/</code>: CSS, JavaScript, and static assets.</li>
                <li><code>templates/</code>: HTML templates for the frontend.</li>
                <li><code>media/</code>: User-uploaded content (e.g., featured images).</li>
            </ul>
        </section>

        <section>
            <h2>Deployment</h2>
            <p>Suitable for deployment on cloud platforms like <strong>PythonAnywhere</strong>, Heroku, or DigitalOcean.
            </p>
        </section>

        <footer>
            &copy; 2026 Django Blogs Project. Built for professional storytelling.
        </footer>
    </div>
</body>

</html>
