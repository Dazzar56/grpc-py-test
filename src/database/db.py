import psycopg2


class Database:
    """
    Класс работы с PostgreSQL
    """
    db_handle = None

    def __init__(self) -> None:
        """
        Подключиться к БД по-молчанию
        """
        self.db_handle = psycopg2.connect(user="*",
                                          password="*",
                                          database='*',
                                          host="/var/run/postgresql",
                                          port=5432)

    def __del__(self) -> None:
        """
        Закрыть подключение в деструкторе
        """
        if self.db_handle is not None:
            self.db_handle.close()

    def sql_exec(self, query, fetch_rows = False):
        """
        Исполнить произвольный SQL и вернуть список результатов по требованию
        """
        with self.db_handle as handle:
            with handle.cursor() as cursor:
                cursor.execute(query)
                if fetch_rows:
                    return cursor.fetchall()[0][0]
