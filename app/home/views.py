from flask import render_template, abort, flash, current_app, redirect
from flask_login import login_required, current_user
from .forms import ShortenUrlForm
from ..models import Link
from . import home
from .. import db

import string
import random


def create_tiny_url():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))


def retrieve_tiny_url(url, user_id):
    tiny_url = ''
    link = Link.query.filter_by(url=url, user_id=user_id).first()
    if not link:
        tiny_url = create_tiny_url()
        link = Link(url=url,
                    tiny_url=tiny_url,
                    user_id=user_id)
        db.session.add(link)
        db.session.commit()
    else:
        tiny_url = link.tiny_url
    return tiny_url


@home.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Render the homepage template on the / route
    """
    form = ShortenUrlForm()
    if form.validate_on_submit():
        user_id = None
        tiny_url = retrieve_tiny_url(form.url.data, user_id)
        flash('Here is your shortened url : ' + current_app.config['BASE_URL'] + tiny_url)
    return render_template('home/index.html', form=form, title="Welcome")


@home.route('/<tiny_url>', methods=['GET', 'POST'])
def url_redirect(tiny_url):
    """
    Render the homepage template on the / route
    """
    link = Link.query.filter_by(tiny_url=tiny_url).first()
    if not link:
        abort(404)
    return redirect(link.url)


@home.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    links = Link.query.filter_by(user_id=current_user.get_id())
    form = ShortenUrlForm()
    if form.validate_on_submit():
        user_id = current_user.get_id()
        tiny_url = retrieve_tiny_url(form.url.data, user_id)
        flash('Here is your shortened url : ' + current_app.config['BASE_URL'] + tiny_url)
    return render_template('home/dashboard.html', form=form, links=links, title="Dashboard")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")
