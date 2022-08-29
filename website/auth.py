
from flask import Blueprint, render_template, redirect, url_for, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'login'

@auth.route('/signup')
def signup():
    return 'signup'

@auth.route('/logout')
def logout():
    return 'logout'