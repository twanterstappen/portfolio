from flask import Blueprint, render_template, redirect, url_for, request, g
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


@bp.route('/coming-soon')
def coming_soon():
    return render_template('coming-soon.html')


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
