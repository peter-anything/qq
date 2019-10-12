import mysql.connector


class SingleTon(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingleTon, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class DBTool(object):
    __connection_pool = []
    current_connection = None

    @staticmethod
    def get_connection():
        if len(DBTool.__connection_pool) > 0:
            connection = DBTool.__connection_pool.pop()
        else:
            connection = mysql.connector.connect(user='qq', password='abc123_W#',
                                                 database='qq', host='192.168.1.138')

        return connection

    @staticmethod
    def close_connection(connection):
        DBTool.__connection_pool.append(connection)

    def raw_sql(self, sql):
        self.current_connection = self.get_connection()
        cursor = self.current_connection.cursor()
        cursor.execute(sql)

        rows = []
        for row in cursor:
            rows.append(row)
        return rows

    def get_objects(self, sql, model_class):
        self.current_connection = self.get_connection()
        cursor = self.current_connection.cursor()
        cursor.execute(sql)

        objs = []
        column_names = cursor.column_names
        for row in cursor:
            obj = model_class()

            for index, column in enumerate(row):
                column_name = column_names[index]
                if hasattr(obj, column_name):
                    setattr(obj, column_name, column)
            objs.append(obj)

        return objs

    def get_object(self, sql, model_class):
        objs = self.get_objects(sql, model_class)

        if len(objs) > 1:
            raise Exception('Multiple Records')

        return objs[0]

    def __del__(self):
        DBTool.__connection_pool.append(self.current_connection)
