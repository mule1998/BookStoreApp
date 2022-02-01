from db_connection import DatabaseConnection

connection = DatabaseConnection()
conn = connection.dbconnection()
db = conn.cursor(buffered=True)


def place_new_order(address, user_id):
    """
        desc: place order
        param:  address, book_id
        return: result_args
    """
    args = [user_id, f'{address}']
    result_args = db.callproc('sp_order', args)
    conn.commit()
    return result_args
