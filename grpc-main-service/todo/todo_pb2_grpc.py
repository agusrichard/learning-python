# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import todo_pb2 as todo__pb2


class TodoServiceStub(object):
    """Missing associated documentation comment in .proto file."""
    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTodo = channel.unary_unary(
            '/todo.TodoService/CreateTodo',
            request_serializer=todo__pb2.CreateTodoRequest.SerializeToString,
            response_deserializer=todo__pb2.CreateTodoResponse.FromString,
        )
        self.GetTodos = channel.unary_unary(
            '/todo.TodoService/GetTodos',
            request_serializer=todo__pb2.GetTodosRequest.SerializeToString,
            response_deserializer=todo__pb2.GetTodosResponse.FromString,
        )


class TodoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""
    def CreateTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CreateTodo':
        grpc.unary_unary_rpc_method_handler(
            servicer.CreateTodo,
            request_deserializer=todo__pb2.CreateTodoRequest.FromString,
            response_serializer=todo__pb2.CreateTodoResponse.SerializeToString,
        ),
        'GetTodos':
        grpc.unary_unary_rpc_method_handler(
            servicer.GetTodos,
            request_deserializer=todo__pb2.GetTodosRequest.FromString,
            response_serializer=todo__pb2.GetTodosResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'todo.TodoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler, ))


# This class is part of an EXPERIMENTAL API.
class TodoService(object):
    """Missing associated documentation comment in .proto file."""
    @staticmethod
    def CreateTodo(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/todo.TodoService/CreateTodo',
            todo__pb2.CreateTodoRequest.SerializeToString,
            todo__pb2.CreateTodoResponse.FromString, options,
            channel_credentials, insecure, call_credentials, compression,
            wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTodos(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
        return grpc.experimental.unary_unary(
            request, target, '/todo.TodoService/GetTodos',
            todo__pb2.GetTodosRequest.SerializeToString,
            todo__pb2.GetTodosResponse.FromString, options,
            channel_credentials, insecure, call_credentials, compression,
            wait_for_ready, timeout, metadata)
