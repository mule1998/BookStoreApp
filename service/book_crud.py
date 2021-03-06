from db_connection import DatabaseConnection
import pandas as pd
from io import StringIO

connection = DatabaseConnection()
conn = connection.dbconnection()
db = conn.cursor(buffered=True)


def add_book(books):
    """
            desc: query to insert book details in database
            param: author_name, title, image, quantity, price, description.
            return: book detail in dictionary format
        """
    show_data_query = "INSERT INTO books (author_name, title, image, quantity, price, description) " \
                      "VALUES('%s', '%s', '%s', %d, %d, '%s')" % \
                      (books.author_name, books.title, books.image, books.quantity, books.price, books.description)
    db.execute(show_data_query)
    conn.commit()
    return books


def retrieve_book(book_id: int):
    """
        desc: query to get a book detail from database
        param: book_id: id for a particular book
        return: book detail in dictionary format
    """
    show_data_query = f"SELECT * FROM books WHERE book_id={book_id}"
    db.execute(show_data_query)
    book = [i for i in db]
    if book:
        return book
    else:
        raise Exception("Book with this Id doesn't exist in the Database!")


def retrieve_all_books():
    """
        desc: query to get all book detail from database
        return: books detail in dictionary format
    """
    get_books_query = "SELECT * FROM books"
    db.execute(get_books_query)
    books = [i for i in db]
    if books:
        return books
    else:
        raise Exception("There is no result for the book.")


def delete_book(book_id):
    """
        desc: query to delete book details from database
        param: id: book id, which you want to delete.
        return: book id which is deleted from db
    """
    show_data_query = f"delete from books where book_id = {book_id}"
    db.execute(show_data_query)
    conn.commit()
    return book_id


def update_book(book_id: int, books):
    """
        desc: query to update book details in database
        param: book_id, author_name, title, image, quantity, price, description.
        return: book detail in dictionary format
    """
    show_data_query = "UPDATE books SET author_name = '%s', title = '%s', image = '%s', quantity = %d, price = %d, " \
                      "description = '%s' WHERE book_id = %d" % (books.author_name, books.title, books.image,
                                                                 books.quantity, books.price, books.description,
                                                                 book_id)
    db.execute(show_data_query)
    conn.commit()
    book_data = retrieve_book(book_id)
    return book_data


# async def insert_data_in_book(file):
#     """
#         desc: query to insert book details in database
#         param: author_name, title, image, quantity, price, description.
#         return: book detail in dictionary format
#     """
#     books_dataframe = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')
#     column_name = ", ".join([str(i) for i in books_dataframe.columns.tolist()])
#     for i, rows in books_dataframe.iterrows():
#         sql = "INSERT INTO books (" + column_name + ") VALUES (" + "%s," * (len(rows) - 1) + "%s)"
#         db.execute(sql, tuple(rows))
#         conn.commit()
#     return "Books are Added Successfully!!"

def insert_to_database(csv_file):
        """
        desc: to read csv and upload it to database
        param: csv_file: path of csv file
        """
        books_dataframe = pd.read_csv(StringIO(str(csv_file.file.read(), 'utf-8')), encoding='utf-8')
        cols = ", ".join([str(i) for i in books_dataframe.columns.tolist()])
        for i, row in books_dataframe.iterrows():
            sql = "INSERT INTO books (" + cols + ") VALUES (" + "%s," * (len(row) - 1) + "%s)"
            db.execute(sql, tuple(row))
            conn.commit()
