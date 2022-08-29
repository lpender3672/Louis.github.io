
from flask import Blueprint, render_template, redirect, url_for, request, flash

views = Blueprint('views', __name__, static_folder = 'static', template_folder = 'templates')


# main views

@views.route('/')
@views.route('/index')
@views.route('/home')
def index():
    return render_template('index.html', name="Louis")

@views.route('/about')
@views.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@views.route('blank')
def blank():
    return render_template('blank.html')


ars = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

@views.route('/dev')
def dev():
    return render_template('base.html', articles = ars)