# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\"\x07\n\x05\x45mpty\"L\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0cis_completed\x18\x04 \x01(\x08\" \n\x08TodoList\x12\x14\n\x05todos\x18\x01 \x03(\x0b\x32\x05.Todo\"\x14\n\x06TodoId\x12\n\n\x02id\x18\x01 \x01(\t2\x9a\x01\n\x0bTodoService\x12\x1d\n\x06GetAll\x12\x06.Empty\x1a\t.TodoList\"\x00\x12\x1b\n\x07GetById\x12\x07.TodoId\x1a\x05.Todo\"\x00\x12\x18\n\x06\x43reate\x12\x05.Todo\x1a\x05.Todo\"\x00\x12\x18\n\x06Update\x12\x05.Todo\x1a\x05.Todo\"\x00\x12\x1b\n\x06\x44\x65lete\x12\x07.TodoId\x1a\x06.Empty\"\x00\x62\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_TODO = DESCRIPTOR.message_types_by_name['Todo']
_TODOLIST = DESCRIPTOR.message_types_by_name['TodoList']
_TODOID = DESCRIPTOR.message_types_by_name['TodoId']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), {
  'DESCRIPTOR' : _TODO,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:Todo)
  })
_sym_db.RegisterMessage(Todo)

TodoList = _reflection.GeneratedProtocolMessageType('TodoList', (_message.Message,), {
  'DESCRIPTOR' : _TODOLIST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:TodoList)
  })
_sym_db.RegisterMessage(TodoList)

TodoId = _reflection.GeneratedProtocolMessageType('TodoId', (_message.Message,), {
  'DESCRIPTOR' : _TODOID,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:TodoId)
  })
_sym_db.RegisterMessage(TodoId)

_TODOSERVICE = DESCRIPTOR.services_by_name['TodoService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=14
  _EMPTY._serialized_end=21
  _TODO._serialized_start=23
  _TODO._serialized_end=99
  _TODOLIST._serialized_start=101
  _TODOLIST._serialized_end=133
  _TODOID._serialized_start=135
  _TODOID._serialized_end=155
  _TODOSERVICE._serialized_start=158
  _TODOSERVICE._serialized_end=312
# @@protoc_insertion_point(module_scope)
