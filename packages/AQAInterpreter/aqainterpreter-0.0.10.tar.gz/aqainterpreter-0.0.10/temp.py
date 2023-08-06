import AQAInterpreter

code = """
FOR i <- 1 TO 3
    OUTPUT i
ENDFOR
"""

print(AQAInterpreter.run(code, transpile=True))
