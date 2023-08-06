""" Run these tests with
pytest AQAInterpreter --verbose
"""

from AQAInterpreter import run


def test_expressions():
    assert run("OUTPUT 1 + 1") == "2\n"
    assert run("OUTPUT 1 - 1") == "0\n"
    assert run("OUTPUT -1") == "-1\n"
    assert run("OUTPUT 2 * 1") == "2\n"
    assert run("OUTPUT 2 × 1") == "2\n"
    assert run("OUTPUT 2 / 1") == "2.0\n"
    assert run("OUTPUT 2 ÷ 1") == "2.0\n"

    assert run('OUTPUT "hi" + "÷"') == "hi÷\n"
    assert run('OUTPUT "a" * 3') == "aaa\n"

    assert run("OUTPUT 1 > 0") == "True\n"
    assert run("OUTPUT 1 ≥ 0") == "True\n"
    assert run("OUTPUT 1 >= 1") == "True\n"
    assert run("OUTPUT 1 < 0") == "False\n"
    assert run("OUTPUT 1 ≤ 0") == "False\n"
    assert run("OUTPUT 1 <= 1") == "True\n"


def test_comments():
    assert run("# comment") == ""


# fmt: off
def test_assignment():
    assert run("""
    a <- 0
    a <- a + 1
    OUTPUT a
    """) == "1\n"


def test_if_statements():
    assert run("""
    IF True THEN
        OUTPUT "hi"
    ENDIF
    """) == "hi\n"

    assert run("""
    IF False:
        OUTPUT "should not fire"
    ELSE:
        OUTPUT "this should"
    ENDIF
    """) == "this should\n"

    assert run("""
    IF True
        IF True
            OUTPUT "nested"
        ENDIF
    ENDIF
    """) == "nested\n"


def test_while_loops():
    assert run("""
    a <- 1
    WHILE a <= 3 DO
        OUTPUT a
        a <- a + 1
    ENDWHILE
    """) == "1\n2\n3\n"

    assert run("""
    a <- 3
    WHILE a >= 1 DO
        OUTPUT a
        a <- a - 1
    ENDWHILE
    """) == "3\n2\n1\n"



def test_for_loops():
    assert run("""
    FOR a <- 1 TO 1
        OUTPUT a
    ENDFOR
    """) == run("""
    FOR a <- 1 TO 1 STEP 1
        OUTPUT a
    ENDFOR
    """) == run("""
    FOR a <- 1 TO 1 STEP -1
        OUTPUT a
    ENDFOR
    """) == "1\n"

    assert run("""
    FOR a <- 1 TO 3
        OUTPUT a
    ENDFOR
    """) == run("""
    FOR a <- 1 TO 3 STEP 1
        OUTPUT a
    ENDFOR
    """) == "1\n2\n3\n"

    assert run("""
    FOR a <- 3 TO 1
        OUTPUT a
    ENDFOR
    """) == run("""
    FOR a <- 3 TO 1 STEP -1
        OUTPUT a
    ENDFOR
    """) == "3\n2\n1\n"

    assert run("""
    FOR a <- 1 TO 5 STEP 2
        OUTPUT a
    ENDFOR
    """) == "1\n3\n5\n"

    assert run("""
    FOR a <- 5 TO 1 STEP -2
        OUTPUT a
    ENDFOR
    """) == "5\n3\n1\n"

    assert run("""
    FOR a <- 1 TO 2
        FOR b <- 1 TO 2
            OUTPUT a
            OUTPUT b
            OUTPUT ""
        ENDFOR
    ENDFOR
    """) == "1\n1\n\n1\n2\n\n2\n1\n\n2\n2\n\n"

    # fibonacci sequence
    assert run("""
    a <- 1
    b <- 1
    c <- 2
    FOR count <- 0 TO 4
        OUTPUT a
        a <- b + c
        OUTPUT b
        b <- c + a
        OUTPUT c
        c <- a + b
        count <- count + 1
    ENDWHILE
    """) == "1\n1\n2\n3\n5\n8\n13\n21\n34\n"
