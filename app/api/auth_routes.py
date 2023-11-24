from flask import Blueprint, request
from app.models import ClanUsers, commit_document_to_db
from app.forms import LoginForm, SignUpForm
from flask_login import current_user, login_user, logout_user
from .user.User_Repository import User_Repository

auth_routes = Blueprint('auth', __name__)

def clan_member_check(user_id):
    """
    Checks if user is in a clan. If not, returns FALSE. If the user is, returns TRUE.
    """
    isClanMember = ClanUsers.query.filter_by(user_id=user_id).first()
    if isClanMember:
        return True
    else:
        return False

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{error}')
    return errorMessages


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}, 403


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User_Repository.login(form.data['email'], form.data['password'])
        # Add the user to the session, we are logged in!
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User_Repository.create_user(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password']
        )
        commit_document_to_db(user)
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
