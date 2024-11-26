from flask import Blueprint, render_template
from models import db, Project, BlogPost  # Import database and models

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

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
