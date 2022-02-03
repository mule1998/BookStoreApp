from db_connection import DatabaseConnection

connection = DatabaseConnection()
conn = connection.dbconnection()
db = conn.cursor(buffered=True, dictionary=True)


def book_order(user_id, address):
    """
        desc: query to call the procedure where many queries are performed
        param: user_id, order model.
    """
    args = [user_id, f'{address}']
    show_data_query = db.callproc('place_order', args)
    conn.commit()
    return show_data_query


def get_data(user_id):
    """
           desc: query to call order details
           param: user_id.
       """
    query = '''select id from order_details where user_id = %d ''' % user_id
    db.execute(query)
    conn.commit()
    result = db.fetchall()
    return result
