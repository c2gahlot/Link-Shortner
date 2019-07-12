from flask import render_template, abort
from flask_login import login_required, current_user
from ..models import User
from . import admin


# existing code remains

# Employee Views

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


@admin.route('/users')
@login_required
def list_users():
    """
    List all users
    """
    check_admin()

    users = User.query.all()
    return render_template('admin/users/index.html',
                           users=users, title='Users')
