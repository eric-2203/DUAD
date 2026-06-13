import psycopg2.extras

class PgManager:
    def __init__(self, dbname, user, password, host, port=5432):
        self.db_name = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.create_connection()
        if self.connection:
            print("Connected to the database.")
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def create_connection(self):
        try:
            connection = psycopg2.connect(
                dbname = self.db_name,
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port,

            )
            return connection
        except Exception as error:
            print("Error connecting to the database: ", error)
            return None
        
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")


    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

        result = None

        if self.cursor.description:
            result = self.cursor.fetchall()

        return result