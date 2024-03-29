import sys
from build_antlr.JSParser import JSParser
from antlr4 import *

class Program:
  def __init__(self, children):
    self.children = children

class Function_declaration:
  def __init__(self, name, body, arg_list, token_scope):
    self.name = name
    self.body = body
    self.arg_list = arg_list
    self.token_scope = token_scope

  def accept(self, visitor):
    return visitor.astVisitFunction_declaration(self)

class Statement:
  def __init__(self, statement):
    self.statement = statement

  def accept(self, visitor):
    return visitor.astVisitStatement(self)

class Function_call:
  def __init__(self, name, arg_list, token):
    self.name = name
    self.arg_list = arg_list
    self.token = token

  def accept(self, visitor):
    return visitor.astVisitFunction_call(self)

class Method_call:
  def __init__(self, object_name, method_name, arg_list):
    self.object_name = object_name
    self.method_name = method_name
    self.arg_list = arg_list

  def accept(self, visitor):
    return visitor.astVisitMethod_call(self)

class Declaration:
  def __init__(self, type_value, name, value, token):
    self.type = type_value
    self.name = name
    self.value = value
    self.token = token

  def accept(self, visitor):
    return visitor.astVisitDeclaration(self)

class Assign:
  def __init__(self, name, operation, value, token):
    self.name = name
    self.operation = operation
    self.value = value
    self.token = token

  def accept(self, visitor):
    return visitor.astVisitAssign(self)

class Expression:
  def __init__(self):
    self.operation = ''
    self.left = ''
    self.right = ''

class BinaryExpression(Expression):
  def __init__(self, operation, left: Expression, right: Expression):
    self.operation = operation
    self.left = left
    self.right = right
  
  def accept(self, visitor):
    return visitor.astVisitBinaryExpression(self)

class Return_statement:
  def __init__(self, value):
    self.value = value

  def accept(self, visitor):
    return visitor.astVisitReturn_statement(self)

class Array_element:
  def __init__(self, name, body):
    self.name = name
    self.body = body

  def accept(self, visitor):
    return visitor.astVisitArray_element(self)

class For_loop:
  def __init__(self, start, condition, step, body, token_scope):
    self.start = start
    self.condition = condition
    self.step = step
    self.body = body
    self.token_scope = token_scope

  def accept(self, visitor):
    return visitor.astVisitFor_loop(self)

class While_loop:
  def __init__(self, condition, body, token_scope):
    self.condition = condition
    self.body = body
    self.token_scope = token_scope

  def accept(self, visitor):
    return visitor.astVisitWhile_loop(self)

class Instruction_if:
  def __init__(self, condition, body, instr_elseif, instr_else, token_scope):
    self.condition = condition
    self.body = body
    self.instuction_elseif = instr_elseif
    self.instuction_else = instr_else
    self.token_scope = token_scope

  def accept(self, visitor):
    return visitor.astVisitInstruction_if(self)

class Instruction_elseif:
  def __init__(self, condition, body, token_scope):
    self.condition = condition
    self.body = body
    self.token_scope = token_scope

  def accept(self, visitor):
    return visitor.astVisitInstruction_elseif(self)
  
class Instruction_else:
  def __init__(self, body, token_scope):
    self.body = body
    self.token_scope = token_scope

  def accept(self, visitor):
    return visitor.astVisitInstruction_else(self)

class Condition:
  def __init__(self, left, operation, right):
    self.left_argument = left
    self.operation = operation
    self.right_argument = right

  def accept(self, visitor):
    return visitor.astVisitCondition(self)

class Object_property:
  def __init__(self, object_name, obj_property):
    self.object_name = object_name
    self.property = obj_property
  
  def accept(self, visitor):
    return visitor.astVisitObject_property(self)

class Integer_literal:
  def __init__(self, value):
    self.value = value
    self.type = 'int'

  def accept(self, visitor):
    return visitor.astVisitorInteger_literal(self)

class String_literal:
  def __init__(self, value):
    self.value = value
    self.type = 'str'

  def accept(self, visitor):
    return visitor.astVisitorString_literal(self)

class Array:
  def __init__(self, list_value):
    self.list_value = list_value
    self.type = 'array'

  def accept(self, visitor):
    return visitor.astVisitorArray(self)

class Id:
  def __init__(self, name, token):
    self.name = name
    self.token = token
  
  def accept(self, visitor):
    return visitor.astVisitId(self)