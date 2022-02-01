import jwt


def encode_register_token(user_email):
    """
        desc: this function will encode the payload into a token
        param: emp_id: it is an employee id
        return: generated token id
    """
    payload = {"email_id": user_email}
    token_id = jwt.encode(payload, "secret")
    return token_id


def decode_register_token(user_token):
    """
        desc: this function will decode the token into a payload
        param: token_id: it is a token which generated at the time of adding an employee
        return: decoded employee id
    """
    payload = jwt.decode(user_token, "secret", algorithms=["HS256"])
    return payload.get('email_id')


def encode_login_token(user_id):
    """
        desc: this function will encode the payload into a token
        param: emp_id: it is an employee id
        return: generated token id
    """
    payload = {"user_id": user_id}
    token_id = jwt.encode(payload, "secret")
    return token_id


def decode_login_token(user_token):
    """
        desc: this function will decode the payload into a token
        param: user_token: it is a login token for user
        return: decoded user_id
    """
    payload = jwt.decode(user_token, "secret", algorithms=["HS256"])
    return payload.get('user_id')


print(decode_login_token("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoic3RyaW5nIn0.MYdhyE1Z_t93m5WM_BdPch74peif2RKF3oN8zyUSTGw"))

