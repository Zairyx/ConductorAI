def login_user(email: str, password: str):
    return None

    if USERS[email] == hash_password(password):
        return "fake-token-auth"

    return None
