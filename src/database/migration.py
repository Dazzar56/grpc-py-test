from src.database.db import Database
import time
from datetime import timedelta
import logging


def make_migration():
    db = Database()
    # Создаем таблицу
    create_table_query = """
    CREATE TABLE IF NOT EXISTS test_transactions (
        user_id   int,
        amount    int,
        timestamp int
    );
    """

    # И заполняем ее
    current_time = time.time()
    year_before  = current_time - timedelta(days = 365).total_seconds()
    test_table_insert = f"""
    INSERT INTO test_transactions (user_id, amount, timestamp)
    SELECT
        floor(random() * 1000),
        floor(random() * 10000),
        floor(random() * ({current_time} - {year_before} +1) + {year_before})
    FROM generate_series(1, 1000000);
    """

    # Проверяем
    test = """
    SELECT * FROM test_transactions LIMIT 1;
    """

    db.sql_exec(create_table_query)
    db.sql_exec(test_table_insert)
    test_query = db.sql_exec(test, True)

    if len(test_query) == 1:
        logging.info("БД успешно сгенерирована")
    else:
        logging.critical("Ошибка при создании БД!")
        raise
