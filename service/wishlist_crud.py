from db_connection import DatabaseConnection

connection = DatabaseConnection()
conn = connection.dbconnection()
db = conn.cursor(buffered=True, dictionary=True)


def retrieve_wishlist(user_id):
    """
        desc: query to get all wishlist detail from database
        return: wishlist detail in dictionary format
    """
    get_wishlist_query = '''SELECT books.author_name, books.title, books.price, books.image from books
                            join wishlist on wishlist.book_id = books.book_id where user_id = %d''' % user_id
    db.execute(get_wishlist_query)
    wish_list = [i for i in db]
    if wish_list:
        return wish_list
    else:
        raise Exception("There is no result for the Wishlist.")


def add_to_wishlist(user_id, wishlist):
    """
        desc: query to insert book details in wishlist
        param: user_id, wishlist model.
    """
    show_data_query = "INSERT INTO wishlist (user_id, book_id) VALUES(%d, %d)" % (user_id, wishlist.book_id)
    db.execute(show_data_query)
    conn.commit()
    return "Book Successfully Added in Wishlist"


def remove_book(user_id, wishlist):
    """
        desc: query to delete book details from wishlist
        param: id: book id, which you want to delete.
        return: book id which is deleted from wishlist
    """
    show_data_query = "delete from wishlist where user_id = %d and book_id = %d" % (user_id, wishlist.book_id)
    db.execute(show_data_query)
    conn.commit()
    return wishlist.book_id
