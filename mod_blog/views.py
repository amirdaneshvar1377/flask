from . import blog
from flask import render_template
from .models import Post

@blog.route('/')
def index():
    posts = Post.query.all()
    return render_template('blog/index.html', posts=posts)


@blog.route('/<string:slug>/')
def single_post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    return post.title
