from concurrent import futures
import grpc
import users_pb2
import users_pb2_grpc


class Users(users_pb2_grpc.UsersServicer):

    def GetUsers(self, request, context):
        return users_pb2.GetUsersResponse(
            users=[
                users_pb2.User(
                    id='1',
                    name='John Doe',
                    email='LpVqH@example.com',
                    password='password123'
                ),
            ]
        )

    def GetUserById(self, request, context):
        return users_pb2.GetUserByIdResponse()

    def CreateUser(self, request, context):
        return users_pb2.CreateUserResponse()

    def UpdateUser(self, request, context):
        return users_pb2.UpdateUserResponse()

    def DeleteUser(self, request, context):
        return users_pb2.DeleteUserResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()