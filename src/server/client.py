from src.grpc import test_pb2_grpc as test_rpc, test_pb2 as protobuf
import grpc
import time
from random import randint
import logging


def exec_request(user_id, start_time, end_time):
    """
    Выполнить запрос суммы транзакций
    """
    with grpc.insecure_channel('127.0.0.1:4444') as channel:
        stub = test_rpc.SumStub(channel)

        request = protobuf.SumRequest(
            user_id=int(user_id),
            time_start=int(start_time),
            time_end=int(end_time)
        )

        response = stub.sum_amount(request)
        return response.total


def run_client():
    """
    тестовый прогон клиента
    """
    stat = []
    for _ in range(100):
        # произвольные тестовые параметры
        test_id = randint(1, 800)
        start = randint(1695743270, 1708170466)
        end = 1708170466

        begin_request = time.time()
        total = exec_request(test_id, start, end)
        end_request = (time.time() - begin_request) * 1000
        stat.append(end_request)

        logging.info(f"сумма транзакций для пользователя ID= {test_id} -- {total}, время запроса: {end_request}")
    logging.info(f"в среднем запрос исполняется за {sum(stat) / len(stat)}")
