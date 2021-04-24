from sqliterunner import make_sql_query

def test_garbage_fetch():
    failed = False
    try:
        make_sql_query("tests/data/game.db", "SELECT * from users", commit=False, fetch='garbage')
    except ValueError as e:
        assert str(e) == "garbage is not one of ['one', 'all', False]"
        failed = True
    assert failed


def test_commit_fetch():
    failed = False
    try:
        make_sql_query("tests/data/game.db", "SELECT * from users", fetch='one')
    except ValueError as e:
        assert str(e) == 'You can not commit & fetch an sql query.'
        failed = True
    assert failed

def test_c_f_false():
    failed = False
    try:
        make_sql_query("tests/data/game.db", "SELECT * from users", commit=False)
    except ValueError as e:
        assert str(e) == 'One of commit or fetch must be True.'
        failed = True
    assert failed
