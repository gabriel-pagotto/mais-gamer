from werkzeug.security import generate_password_hash, check_password_hash


def set_password_hash(password):
    return generate_password_hash(password)


def check_password(password, password_hash):
    return check_password_hash(password_hash, password)
