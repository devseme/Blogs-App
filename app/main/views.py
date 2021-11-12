from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Quote
from flask_login import login_required,current_user
from .. import db,photos
from ..requests import get_quote




@main.route('/')
def index():
    '''
    View root function that returns index template
    '''
    quote = get_quote()
    return render_template('index.html',quote =quote)

