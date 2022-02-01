from db_connection import DatabaseConnection

connection = DatabaseConnection()
conn = connection.dbconnection()
db = conn.cursor(buffered=True)


def all_users_details():
    """
        desc: query to get all users details
        return: users details
    """
    db.execute('select * from users')
    users = [i for i in db]
    return users


def single_emp(user_id):
    """
        desc: query to get user details
        return: users details
    """
    if user_id == "":
        raise Exception(
            {"status": 400, "message": "user Details not able to display", "error": "id should be filled"})
    db.execute(f'select * from users where user_id={user_id}')
    users = [i for i in db]
    if users:
        return users
    else:
        raise Exception(
            {"status": 400, "message": "user Details not able to display", "error": "user id not found"})


def register_user(user_name: str, email_id: str, password: str, mobile_no: str):
    """
            desc: query to insert user details in database
            param: name, email_id, password, mobile_no
            return: employee detail in dictionary format
        """
    query = "insert into users (user_name, email_id, password, mobile_no) VALUES  ('%s','%s', '%s', " \
            "'%s')" \
            % (user_name, email_id, password, mobile_no)
    db.execute(query)
    conn.commit()


def update_user(user_id, Users):
    """
        desc: query to update employee details in database
        param: id, name, profile, gender, department, salary, start date.
        return: employee detail in dictionary format
    """
    show_data_query = "UPDATE users SET user_name = '%s', email_id = '%s', password = '%s', mobile_no " \
                      "= %s WHERE user_id = %d" % (Users.user_name, Users.email_id, Users.password, Users.mobile_no,
                                                   user_id)
    db.execute(show_data_query)
    conn.commit()
    user_data = single_emp(user_id)
    return user_data


def delete_user(user_id):
    """
        desc: query to delete employee details from database
        param: id: user id, which you want to delete.
        return: user id which is deleted from db
    """
    show_data_query = f"delete from users where user_id = {user_id}"
    db.execute(show_data_query)
    conn.commit()
    return user_id


def login_into_book_store(email_id, password):
    """
        desc: query to get a user detail from database
        param: user id
        return: employee detail in dictionary format
    """
    show_data_query = f"SELECT user_id FROM users WHERE email_id = '{email_id}' and password = '{password}'"
    db.execute(show_data_query)
    user = [i for i in db]
    if user:
        return user
    else:
        raise Exception("Credentials Are incorrect, Please Try again!")


def verification(is_verified: int, email_id: str):
    show_data_query = f"UPDATE users SET is_verified = 1 WHERE email_id='{email_id}'"
    db.execute(show_data_query)
    conn.commit()
    return "User Account Successfully Verified!!"


def retrieve_user_by_email_id(email_id: str):
    """
        desc: query to get a user detail from database
        param: user id
        return: employee detail in dictionary format
    """
    show_data_query = f"SELECT * FROM users WHERE email_id='{email_id}'"
    db.execute(show_data_query)
    conn.commit()
    user = [i for i in db]
    if user:
        return user
    else:
        raise Exception("User with this Id doesn't exist in the Database!")
