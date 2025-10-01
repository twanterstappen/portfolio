from flask import Blueprint, render_template, redirect, url_for, request, g, make_response
from datetime import datetime
# from models import db, Project, BlogPost  # Import database and models

bp = Blueprint('main', __name__)

@bp.before_request
def set_current_route():
    g.current_route = request.path

@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/<any>')
def any(any):
    return redirect(url_for('main.coming_soon'), code=302)

# @bp.route('/blogs')
# def blogs():
#     return render_template('blogs/blogs.html')

@bp.route('/achievements')
def achievements():
    return render_template('achievements.html')


@bp.route('/contact')
@bp.route('/get-in-touch')
def contact():
    """Contact page with mailto: form"""
    return render_template('contact.html')


@bp.route('/coming-soon')
def coming_soon():
    return render_template('coming-soon.html')


@bp.route('/sitemap.xml')
def sitemap():
    """Generate sitemap.xml for SEO"""
    pages = []
    ten_days_ago = (datetime.now().replace(microsecond=0).isoformat() + 'Z')
    
    # Add static pages
    pages.append({
        'url': url_for('main.home', _external=True),
        'lastmod': ten_days_ago,
        'changefreq': 'weekly',
        'priority': '1.0'
    })
    
    pages.append({
        'url': url_for('main.achievements', _external=True),
        'lastmod': ten_days_ago,
        'changefreq': 'monthly',
        'priority': '0.8'
    })
    
    # Add other pages as they become available
    # pages.append({
    #     'url': url_for('main.blogs', _external=True),
    #     'lastmod': ten_days_ago,
    #     'changefreq': 'weekly',
    #     'priority': '0.7'
    # })
    
    sitemap_xml = render_template('sitemap.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    
    return response


@bp.route('/robots.txt')
def robots_txt():
    """Generate robots.txt for search engines"""
    robots_content = f"""User-agent: *
Allow: /
Sitemap: {url_for('main.sitemap', _external=True)}

# Block access to admin areas and files
Disallow: /admin/
Disallow: /*.json$
Disallow: /*.xml$
Disallow: /static/images/favicon/
"""
    
    response = make_response(robots_content)
    response.headers["Content-Type"] = "text/plain"
    return response


# @bp.route('/portfolio')
# def portfolio():
#     # Fetch all projects from the database
#     projects = Project.query.all()
#     return render_template('portfolio.html', projects=projects)

# @bp.route('/blog')
# def blog():
#     # Fetch all blog posts from the database
#     posts = BlogPost.query.order_by(BlogPost.date.desc()).all()
#     return render_template('blog.html', posts=posts)
