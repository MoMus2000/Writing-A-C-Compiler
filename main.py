import sys
from lexer import Lexer

# Compiler Driver
"""
1. PREPROCESS THE FILE
2. COMPILE
3. Assemble and Link
"""

def help():
    return """
    Usage:
    python3 main.py /path/to/c/file

    OPTIONS:
    python3 main.py /path/to/c/file --lex
    python3 main.py /path/to/c/file --parse
    python3 main.py /path/to/c/file --codegen
    """

def main():
    args = sys.argv

    if len(args) < 2:
        print(help())
        sys.exit(1)

    file_name = args[1]

    src = open(file_name, "r").read()

    if "--lex" in args and len(args) > 2:
        tokens = Lexer().lex(src)
        for token in tokens:
            print(token)

    elif "--parse" in args and len(args) > 2:
        pass

    elif "--codegen" in args and len(args) > 2:
        pass

    else:
        tokens = Lexer().lex(src)
        for token in tokens:
            print(token)

    
if __name__ == "__main__":
    main()
