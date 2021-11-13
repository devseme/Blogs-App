from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Quote,Blog
from flask_login import login_required
from .. import db,photos
from ..requests import get_quote
from .forms import BlogForm




@main.route('/')
def index():
    '''
    View root function that returns index template
    '''

    quote = get_quote()
    blog_form = BlogForm()
    all_blogs = Blog.query.order_by(Blog.date_posted).all()
    return render_template('index.html',quote =quote,blogs = all_blogs)

@main.route('/blog', methods=['GET', 'POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        category = blog_form.category.data
        content = blog_form.content.data
        created_by = blog_form.created_by.data
        new_blog = Blog(title=title,category=category, content=content, created_by= created_by)
        new_blog.save_blog()
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.index'))

    else:
        all_blogs = Blog.query.order_by(Blog.date_posted).all()

    return render_template('blogs.html', blogs=all_blogs,blog_form = blog_form)

