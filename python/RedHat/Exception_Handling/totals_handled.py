def main():
    total = 0
    msg = "Please enter a number, or 'end' to quit: "
    while True:
        value = input(msg)
        if value == "end":
            break
        try:
            total += int(value)
        except ValueError:
            print("Invalid Number - Please try again")

    print("Total is", total)


if __name__ == "__main__":
    main()
"""
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
     +-- StopIteration, StopAsyncIteration, AssertionError, AttributeError
     +-- BufferError, EOFError, ImportError, MemoryError, ReferenceError
     +-- SystemError, TypeError
     +-- ArithmeticError
     |    +-- FloatingPointError, OverflowError, ZeroDivisionError
     +-- LookupError
     |    +-- IndexError, KeyError
     +-- NameError
     |    +-- UnboundLocalError
     +-- OSError
     |    +-- BlockingIOError, ChildProcessError, FileExistsError
     |    +-- FileNotFoundError, InterruptedError, IsADirectoryError
     |    +-- NotADirectoryError, PermissionError, ProcessLookupError
     |    +-- TimeoutError
     |    +-- ConnectionError
     |    | +-- BrokenPipeError, ConnectionAbortedError
     |    | +-- ConnectionRefusedError, ConnectionResetError
     +-- RuntimeError
     |   +-- NotImplementedError, RecursionError
     +-- SyntaxError
     |    +-- IndentationError
     |         +-- TabError
     +-- ValueError
     |    +-- UnicodeError
     |         +-- UnicodeDecodeError, UnicodeEncodeError, UnicodeTranslateError
     +-- Warning
          +-- DeprecationWarning, PendingDeprecationWarning, RuntimeWarning
          +-- SyntaxWarning, UserWarning, FutureWarning, ImportWarning
          +-- UnicodeWarning, BytesWarning, ResourceWarning
"""