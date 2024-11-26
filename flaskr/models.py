from flask_sqlalchemy import SQLAlchemy

# Initialize database instance (used in app.py)
db = SQLAlchemy()

# Define Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200))

    def __repr__(self):
        return f"<Project {self.title}>"

# Define BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<BlogPost {self.title}>"
