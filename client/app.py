from __future__ import print_function
import grpc
import users_pb2 as users__pb2
import users_pb2_grpc as users__pb2_grpc


def run():
    response = []
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users__pb2_grpc.UsersStub(channel)
        response = stub.GetUsers(users__pb2.GetUsersRequest())
        print(response)

if __name__ == '__main__':
    run()