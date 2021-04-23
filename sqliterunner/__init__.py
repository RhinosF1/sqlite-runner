from sqlite3 import connect


def make_sql_query(dbfile, query, commit=True, fetch=False):
    fetchtypes = ['one', 'all']
    if fetch not in fetchtypes:
        raise ValueError(f'{fetch} is not one of {fetchtypes}')
    if commit and fetch:
        raise ValueError("You can not commit & fetch an sql query.")
    if not commit and not fetch:
        raise ValueError("One of commit or fetch must be True.")
    with connect(dbfile) as dbconn:
        dbconn = connect(dbfile)
        queryres = dbconn.execute(query)
        if commit:
            dbconn.commit()
            queryres = True
        elif fetch == 'all':
            queryres = queryres.fetchall()
        elif fetch == 'one':
            queryres = queryres.fetchone()
        else:
            raise Exception("Fatal: Request not understood.")
    return queryres
