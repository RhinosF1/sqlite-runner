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


def test_selectone():
    query = make_sql_query("tests/data/game.db", "SELECT * FROM user_prefrences WHERE user_id = 1", commit=False, fetch='one')
    assert query == (1, 'prefrence-key', 'test-value')


def test_selectall():
    query = make_sql_query("tests/data/game.db", "SELECT * FROM users", commit=False, fetch='all')
    assert query == [
        (1, 'Test_user1605265142.298722', '072558d4697'),
        (2, 'Test_user1606823952.380141', '8eaa1e0')
        ]

def test_commit():
    query = make_sql_query("tests/data/game.db", "INSERT INTO tokens (public_key, private_key, not_valid_before, not_valid_after) VALUES ('blah1', 'blah2', 'blah3', 'blah4')")
    assert query
    selectq = make_sql_query("tests/data/game.db", "SELECT * from tokens", commit=False, fetch='one')
    assert selectq == (1, 'blah1', 'blah2', 'blah3', 'blah4')
    
