from utilities.connection import DatabaseConnection
from auth.auth_queries import auth_queries

class Helper:
    
    def execute_query(self, query, data=None):
        self.db = DatabaseConnection()
        self.db.connect() 
        result = self.construct_query(query, data)
        self.db.close()
        return result
    
    def construct_query(self, query, data):
        cursor = self.db.get_cursor()
        if type(data) == dict:
            res = list(data.values())
            cursor.execute(query, res)
            return True
        else:
            cursor.execute(query, data)
            if "SELECT" in query:
                result = cursor.fetchall()
                return result
            else:
                return None, True
            
    def check_if_user_exists(self,current_user):
        util_object = Helper()
        return util_object.execute_query(auth_queries['IF_USER_EXISTS'], (current_user,))
    
    