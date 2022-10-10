"""
SimpleMessageQueue implementation

Not to be used for any real system, no matter how tempting

"""

__author__ = "prussell"

import queue
import threading
import socket
import json

# Table-of-Queues. This is the Data Structure in the Server. We're not
# using a Heap anywhere because we don't need to support
# Priorities/Run-Levels

GIL = threading.Lock()


class MQRecord:
    def __init__(self):
        self.Q = queue.Queue()
        self.L = threading.Lock()


QUEUE_TABLE = {
    "tax_return": MQRecord(),
    "qbo_invoice": MQRecord(),
    # Etc. Pre-allocate queues based on popular/most-requsted Types
}


def put(K, DO):

    with GIL:
        if K not in QUEUE_TABLE:
            QUEUE_TABLE[K] = MQRecord()

    record = QUEUE_TABLE[K]

    with record.L:
        record.Q.put(DO)


def get(K):

    record = QUEUE_TABLE.get(K, None)

    if not record:
        return None

    with record.L:
        if not record.Q.empty():
            return record.Q.get()
        else:
            return None


class Request:
    PUT = 0
    GET = 1

    def __init__(self, K, V, operation):
        self.K = K
        self.V = V
        self.operation = operation

    # Not required to be implemented by the Interviewee, here for
    # completeness
    def to_bytes(self) -> bytes:
        return json.dumps({"K": self.K, "V": self.V, "operation": self.operation}).encode('utf-8')

    # Not required to be implemented by the Interviewee, here for
    # completeness
    @classmethod
    def from_bytes(cls, json_bytes):
        O = json.loads(json_bytes.decode('utf-8'))
        return Request(O["K"], O["V"], O["operation"])


class Response:
    def __init__(self, K, V, error=None):
        self.K = K
        self.V = V
        self.error = error

    # Not required to be implemented by the Interviewee, here for
    # completeness
    def to_bytes(self) -> bytes:
        return json.dumps({"K": self.K, "V": self.V, "error": self.error}).encode('utf-8')

    # Not required to be implemented by the Interviewee, here for
    # completeness
    @classmethod
    def from_bytes(cls, json_bytes):
        O = json.loads(json_bytes.decode('utf-8'))
        return Response(O["K"], O["V"], O["error"])


def handle_connection(conn, addr):
    with conn:
        # Just assume a RequestMessage is less than 4096 bytes
        message = Request.from_bytes(conn.recv(4096))
        if message.operation == Request.GET:
            K = message.K
            data = get(K)
            response = Response(K, data)
        elif message.operation == Request.PUT:
            K = message.K
            V = message.V
            put(K, V)
            response = Response(K, True)

        conn.sendall(response.to_bytes())


def server_loop(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(1)
        print("Ready to accept connections")
        while True:
            # Just wait until a connection comes in, dispatch to Thread
            conn, addr = s.accept()
            print("Connected to client {addr}".format(addr=addr))
            thread = threading.Thread(target=handle_connection, args=(conn, addr))
            thread.start()


# Not required to be implemented by the Interviewee, here for
# completeness
class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def put(self, K, V) -> Response:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            req = Request(K, V, Request.PUT)
            sock.sendall(req.to_bytes())
            resp = Response.from_bytes(sock.recv(4096))
            return resp

    def get(self, K) -> Response:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            req = Request(K, None, Request.GET)
            sock.sendall(req.to_bytes())
            resp = Response.from_bytes(sock.recv(4096))
            return resp


# Not required to be implemented by the Interviewee, here for
# completeness
if __name__ == "__main__":
    import os

    host = os.getenv("SMQ_HOST", "0.0.0.0")
    port = os.getenv("SMQ_PORT", 8080)
    print(">>>>>>>> SimpleMessageQueue Running on host={host}, port={port} >>>>>>>>>>".format(host=host, port=port))
    server_loop(host, port)
