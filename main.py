from src.database.migration import make_migration
from src.server.service import serve
from src.server.client import run_client
import sys
import logging

#базовая настройка отправки логов в stderr
logging.basicConfig(level='INFO')

if __name__ == '__main__':
    args = sys.argv[1:]
    usage = """Тестовый gRPC сервер.
    Использование:
        python -m main serve -- запуск сервера на 127.0.0.1:4444
        python -m main test -- прогон 100 запросов на сервер с вычислением суммы транзакций
        python -m main migration --подготовка тестовой БД на 1 000 000 записей"""

    if len(args) < 1 :
        print(usage)
        sys.exit(1)

    # тут можно сделать гораздо более детальные параметры
    # например, задавать ардес и порт
    match args[0]:
        case 'serve':
            serve()
        case 'migration':
            make_migration()
        case 'test':
            run_client()
        case _ :
            print(usage)
            sys.exit(1)