from app import db

posts_categories = db.Table('posts_categories', db.metadata, db.Column('post_id', db.Integer, db.ForeignKey('posts.id', ondelete='cascade')),
                            db.Column('category_id', db.Integer, db.ForeignKey('categories.id', ondelete='cascade'))
                            )


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.String(256), nullable=True, unique=False)
    slug = db.Column(db.String(128), nullable=False, unique=True)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    summary = db.Column(db.String(256), nullable=True, unique=False)
    content = db.Column(db.TEXT, nullable=False, unique=False)
    slug = db.Column(db.String(128), nullable=False, unique=True)
