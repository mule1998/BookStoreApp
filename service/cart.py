from db_connection import DatabaseConnection

connection = DatabaseConnection()
conn = connection.dbconnection()
db = conn.cursor(buffered=True, dictionary=True)


def retrieve_cart_item(user_id):
    """
        desc: query to get all cart detail from database
        return: cart detail in dictionary format
    """

    get_cart_query = '''SELECT books.book_id,books.author_name, books.title, books.price, books.image from books
                                join cart on cart.book_id = books.book_id where user_id = %d''' % user_id
    db.execute(get_cart_query)
    wish_list = [i for i in db]
    if wish_list:
        return wish_list
    else:
        raise Exception("There is no result for the cart.")


def add_to_cart(user_id, cart):
    """
        desc: query to insert book details in cart
        param: user_id, cart model.
    """
    show_data_query = "INSERT INTO cart (user_id, book_id) VALUES(%d, %d)" % (user_id, cart.book_id)
    db.execute(show_data_query)
    conn.commit()
    return "Book Successfully Added in cart"


def remove_book_from_cart(user_id, book_id):
    """
        desc: query to delete book details from cart
        param: id: book id, which you want to delete.
        return: book id which is deleted from cart
    """
    show_data_query = "delete from cart where user_id = %d and book_id = %d" % (user_id, book_id)
    db.execute(show_data_query)
    conn.commit()
    return book_id


def update_cart(user_id, quantity, cart):
    """
        desc: query to update employee details in database
        param: id, name, profile, gender, department, salary, start date.
        return: employee detail in dictionary format
    """
    show_data_query = "UPDATE cart SET quantity = %d WHERE user_id = %d and book_id = %d" % \
                      (quantity, user_id, cart.book_id)
    db.execute(show_data_query)
    conn.commit()
    user_data = retrieve_cart_item(user_id)
    return user_data
