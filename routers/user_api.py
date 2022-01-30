from fastapi import FastAPI, APIRouter, Header
from logger import logging
from service import email

from schemas.book_pydantic import Books
from service import queries
from schemas.model import Users
import handler
from service import book_crud


route = APIRouter(tags=["USERS"])
logging.basicConfig(filename='user.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')


@route.get("/")
async def root():
    return {"message": "Welcome to BookStore app"}


@route.post("/user/registration/")
async def user_registration(user: Users):
    """
    desc: created api to register the user into book store app.
    param1: Users class which contains schema
    return: user_token in SMD format
    """
    try:
        user_details = queries.register_user(user.user_name, user.email_id, user.password, user.mobile_no)
        logging.info("User Successfully Registered")
        logging.debug(f"User Details are : {user_details}")
        user_token = handler.encode_register_token(user.email_id)
        await email.send_mail(user.email_id, user_token)
        return {"status": 200, "message": "Successfully Registered The User", "token": user_token}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": "Error : User with this Id Already exist in database"}


@route.get("/users")
def get_all_users_details():
    """
        desc: created api to get all the users details.
        return: user details in SMD format.
    """
    try:
        user_details = queries.all_users_details()
        logging.info("Successfully Get All User Details")
        logging.debug(f"User Details are : {user_details}")
        return {"status": 200, "message": "Successfully Get All User Details", "data": user_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.get("/user/", tags=["USERS"])
def get_user_details(user_id: int):
    """
        desc: created api to get a single user details.
        param: user_id: it is a user id.
        return: user details in SMD format.
    """
    try:
        user_details = queries.single_emp(user_id)
        logging.info("Successfully Get A User Detail")
        logging.debug(f"User Details are : {user_details}")
        return {"status": 200, "message": "Successfully Get A User Details", "data": user_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.put("/user/detail/", tags=["USERS"])
def update_user_details(user_id: int, users: Users):
    """
    desc: created api to update any item in the database table
    param1: user_id: it is a user id
    param2: Users class which contains schema
    return: user details in SMD format
    """
    try:
        queries.single_emp(user_id)
        user_details = queries.update_user(user_id, users)
        logging.info("Successfully Updated The User Details")
        logging.debug(f"User Details are : {user_details}")
        return {"status": 200, "message": "Successfully Updated The User Details", "data": user_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@route.delete("/user/", tags=["USERS"])
def delete_user_details(user_id: int):
    """
    desc: created api to delete the user details using user id
    param: user_id: it is a user id
    return: u_id in SMD format
    """
    try:
        queries.single_emp(user_id)
        u_id = queries.delete_user(user_id)
        logging.info("Successfully Deleted The User Details")
        logging.debug(f"User ID is : {u_id}")
        return {"status": 204, "message": "Successfully Deleted The User Details", "data": u_id}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.post("/user/login/", tags=["USERS"])
def user_login(email_id: str, password: str):
    """
    desc: created api to login into boost store app
    param1: id: it is a user email id
    param2: password: user password
    return: user details in SMD format
    """
    try:
        user_details = queries.login_into_book_store(email_id, password)
        logging.info("Successfully Login into Book Store App!!")
        logging.debug(f"User Details are : {user_details}")
        user_token = handler.encode_login_token(user_details[0][1])
        return {"status": 200, "message": "Successfully Generated the token", "token": user_token, "data": user_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 401, "message": f"Error : {e}"}


@route.get("/user/verification/{token}")
def user_verification(token: str = Header(None)):
    """
        desc: user verification by entering the token number generated at registration
        param: token: encoded user email id
    """
    try:
        token_id = decode_register_token(token)
        check_user = retrieve_user_by_email_id(token_id)
        verify_user = verification(check_user[0]["is_verified"], token_id)
        return {"status": 200, "message": "Successfully Done User Verification!!", "data": verify_user}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 401, "message": f"{e}"}


def verify_token(token: str = Header(None)):
    if token is None:
        raise HTTPException(status_code=401, detail="Token is not given in Header")
    try:
        user_id = decode_login_token(token)
        return user_id
    except Exception as exc:
        raise HTTPException(status_code=403, detail="You are not a authorized person")


