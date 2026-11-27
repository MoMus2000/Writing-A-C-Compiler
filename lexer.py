class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

    def __str__(self):
        return f"Token({self.token_type},{self.lexeme})"

class Lexer:
    keywords = {
        "return": Token("RETURN", ""),
        "int": Token("INT", ""),
        "void": Token("VOID", ""),
    }

    def lex(self, stream_of_words):
        tokens = []
        cursor = 0
        while cursor < len(stream_of_words):
            character = stream_of_words[cursor]

            if character == "\n":
                cursor += 1
                continue

            if character == " ":
                cursor += 1
                continue

            if character == "(":
                tokens.append(Token("LEFT_PAREN", "("))
                cursor += 1
            if character == ")":
                tokens.append(Token("RIGHT_PAREN", ")"))
                cursor += 1
            if character == "{":
                tokens.append(Token("LEFT_BRACE", "{"))
                cursor += 1
            if character == "}":
                tokens.append(Token("RIGHT_BRACE", "}"))
                cursor += 1
            if character == ";":
                tokens.append(Token("SEMICOLON", ";"))
                cursor += 1

            if character.isalnum():
                initial = cursor
                while stream_of_words[cursor].isalnum():
                    cursor += 1
                text = stream_of_words[initial:cursor]
                if text in Lexer.keywords:
                    tokens.append(Lexer.keywords[text])

                else:
                    tokens.append(Token("IDENTIFIER", text))

            if character.isdigit():
                initial = cursor
                while stream_of_words[cursor].isdigit():
                    cursor += 1
                number = stream_of_words[initial:cursor]

                tokens.append(Token("CONSTANT", number))

        return tokens

