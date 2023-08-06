TYPE = "type"
VALUE = "value"
DICT = "dict"

GLOBALS = "__globals__"
BUILTINS = "__builtins__"
DOC = "__doc__"

REGEX_TYPE = r"\'(\w+)\'"

NAME_NAME = "__name__"
OBJECT_NAME = "__object_type__"
FIELDS_NAME = "__fields__"
MODULE_NAME = "__module__name__"

TYPE = "type"
VALUE = "value"

CLASS = "class"
OBJECT = "object"

NOT_CLASS_ATTRIBUTES = [
    "__class__",
    "__getattribute__",
    "__new__",
    "__setattr__",
]

FUNCTION = "function"

FUNCTION_ATTRIBUTES = [
    "__code__",
    "__name__",
    "__defaults__",
    "__closure__"
]

CODE = "__code__"
CLOSURE = "__closure__"

LIST = "list"
TUPLE = "tuple"
BYTES = "bytes"

FLOAT = "float"
INT = "int"
NONE_TYPE = "NoneType"
COMPLEX = "complex"
BOOL = "bool"
STRING = "str"


TRUE = "True"

CODE_OBJECT_ARGS = [
    'co_argcount',
    'co_posonlyargcount',
    'co_kwonlyargcount',
    'co_nlocals',
    'co_stacksize',
    'co_flags',
    'co_code',
    'co_consts',
    'co_names',
    'co_varnames',
    'co_filename',
    'co_name',
    'co_firstlineno',
    'co_lnotab',
    'co_freevars',
    'co_cellvars',
]