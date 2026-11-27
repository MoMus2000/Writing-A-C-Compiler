"""
Parser will produce the AST
CODE GEN STAGE will traverse that tree to produce the assembly code

Both GCC and Clang Use Handwritten Parsers, faster to debug, flexible and simpler to 
understand

ZEPHR Abstract Syntax Description Lang (ASDL) is what the book uses

Need to impl this for now:
    program = Program(function_definition)
    function_definition = Function(identifier name, statement body)
    statement = Return(exp)
    exp = Constant(int)
"""

class Program:
    def __init__(self, func):
        self.func = func

    def __repr__(self):
        return f"{self.func}"

class Function:
    def __init__(self, func_name, statements): # For now statements is an array of 1
        self.func_name = func_name
        self.statements = statements

    def __repr__(self):
        return f"""
        Function(
            name={self.func_name},
            body={self.statements}
        )
        """

class ReturnStatement:
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"""
        Return(
            {self.expression}
        )
        """

class ConstantExpression:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"""
        Constant({self.number})
        """

class Parser:
    def __init__(self, stream_of_tokens):
        self.stream_of_tokens = stream_of_tokens

    def parse(self):
        return self.parse_program()

    def parse_function(self):
        self.expect("int", self.stream_of_tokens)
        self.expect("main", self.stream_of_tokens)
        self.expect("(", self.stream_of_tokens)
        self.expect("void", self.stream_of_tokens)
        self.expect(")", self.stream_of_tokens)
        self.expect("{", self.stream_of_tokens)
        return_stmt = self.parse_statement()
        return Function("main", return_stmt)

    def parse_program(self):
        return Program(
                self.parse_function()
                )

    def parse_statement(self):
        self.expect("return", self.stream_of_tokens)
        return_val = self.parse_expression()
        self.expect(";", self.stream_of_tokens)
        return ReturnStatement(return_val)

    def parse_expression(self):
        token = self.take_token(self.stream_of_tokens)
        if token.token_type == "CONSTANT":
            return ConstantExpression(token.lexeme)

    def expect(self, expected, tokens):
        token = self.take_token(tokens)
        if expected != token.lexeme:
            raise Exception("No Mas")

    def take_token(self, tokens):
        token = tokens[0]
        self.stream_of_tokens = tokens[1:]
        return token

