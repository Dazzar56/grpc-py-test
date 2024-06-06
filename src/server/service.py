from src.grpc import test_pb2_grpc as rpc, test_pb2 as protobuf
from src.database.db import Database

from concurrent import futures
import grpc
import logging


class Sum(rpc.SumServicer):
    """
    Класс RPC сервера
    """

    def sum_amount(self, request, context):
        db = Database()

        query = f"""
        SELECT SUM(amount)
        FROM test_transactions
        WHERE
        user_id   =  {request.user_id}    AND
        timestamp >= {request.time_start} AND
        timestamp <= {request.time_end};
        """
        res = db.sql_exec(query, True)

        logging.info(f"Возвращаемый ответ: {res}")
        return protobuf.SumResponse(total=res)


def serve():
    """
    Запустить сервер
    """

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    rpc.add_SumServicer_to_server(Sum(), server)
    server.add_insecure_port('127.0.0.1:4444')
    server.start()
    logging.info('сервер запущен')
    server.wait_for_termination()
