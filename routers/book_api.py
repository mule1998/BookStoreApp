from fastapi import FastAPI, APIRouter, File, UploadFile
from logger import logging
from schemas.book_pydantic import Books
from service import queries
import handler
from service import book_crud


route = APIRouter(tags=["BOOKS"])
logging.basicConfig(filename='user.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')


@route.post("/book/", tags=["BOOKS"])
def add_new_book(books: Books):
    """
        desc: created api to add the book into book store app.
        param1: Books class which contains schema
    """
    try:
        book_details = book_crud.add_book(books)
        logging.info("Book Successfully Added")
        logging.debug(f"Book Details are : {book_details}")
        return {"status": 200, "message": f"Successfully Added The Book!!", "data": book_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 402, "message": "Error : Book with this Id Already exist in database"}


@route.get("/books/")
def get_all_users_details():
    """
        desc: created api to get all the books detail.
        return: books detail in SMD format.
    """
    try:
        book_details = book_crud.retrieve_all_books()
        logging.info("Successfully Get All Books Details")
        logging.debug(f"Book Details are : {book_details}")
        return {"status": 200, "message": "Successfully Get All Books Details", "data": book_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.get("/book/", )
def get_book_details(book_id: int):
    """
        desc: created api to get a book details.
        param: book_id: it is a book id.
        return: book details in SMD format.
        """
    try:
        book_details = book_crud.retrieve_book(book_id)
        logging.info("Successfully Get A Book Detail")
        logging.debug(f"Book Details are : {book_details}")
        return {"status": 200, "message": "Successfully Get A Book Details", "data": book_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.delete("/book/", )
def delete_book_details(book_id: int):
    """
    desc: created api to delete the book details using book id
    param: book_id: it is a book id
    return: b_id in SMD format
    """
    try:
        retrieve_book(book_id)
        b_id = delete_book(book_id)
        logging.info("Successfully Deleted The Book Details")
        logging.debug(f"Book ID is : {b_id}")
        return {"status": 204, "message": "Successfully Deleted The Book Details", "data": b_id}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 404, "message": f"Error : {e}"}


@route.put("/book/", )
def update_book_details(book_id: int, books: Books):
    """
    desc: created api to update any book details
    param1: book_id: it is a user id
    param2: Books class which contains schema
    return: updated book details in SMD format
    """
    try:
        book_crud.retrieve_book(book_id)
        book_details = book_crud.update_book(book_id, books)
        logging.info("Successfully Updated The Book Details")
        logging.debug(f"Book Details are : {book_details}")
        return {"status": 200, "message": "Successfully Updated The Book Details", "data": book_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


# @route.post("/uploadFile/")
# async def create_upload_file(file: UploadFile = File(...)):
#     try:
#         detail = await book_crud.insert_data_in_book(file)
#         logging.info("Successfully Updated The Book Details")
#         logging.debug(detail)
#         return {"status": 200, "message": "Successfully Added The Book File"}
#     except Exception as e:
#         logging.error(f"Error: {e}")
#         return {"status": 500, "message": f"Error : {e}"}


@route.post("/upload_file")
async def upload_csv_file(csv_file: UploadFile = File(...)):
    try:
        book_crud.insert_to_database(csv_file)
        logging.info("successfully uploaded the file and inserted into database")
        return {"status": 200, "message": "Books Added to Database Successfully"}
    except Exception as error:
        logging.error(f"error caught :{error}")
        return {"status": 500, "message": f"Error : {error}"}
