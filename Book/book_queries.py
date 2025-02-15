book_queries={
    "INSERT_BOOK": "INSERT INTO BOOKS(TITLE, AUTHOR, PRICE, ISBN_NO, SUMMARY, GENRE, OWNER_ID) VALUES(%s,%s,%s,%s,%s,%s,%s)",
    "GET_BOOK": "SELECT TITLE, AUTHOR, PRICE, ISBN_NO, SUMMARY, GENRE FROM BOOKS WHERE ID=%s",
    "DELETE_BOOK": "UPDATE BOOKS SET IS_ACTIVE='0' WHERE ID=%s",
    "UPDATE_BOOK" : "UPDATE BOOKS SET TITLE=%s, AUTHOR=%s, PRICE=%s, ISBN_NO=%s, SUMMARY=%s, GENRE=%s WHERE ID=%s",
    "FIND_BOOK" : "SELECT ID FROM BOOKS WHERE OWNER_ID=%s"
    }