'''
Arthor:		FGO
Usage:		Query SQLite db
Param:
db_name: database file name with full path
stmts: SQL statement

Return:		SQL query result
Example:
records = get_records('access_record', 'SELECT * FROM daily_access_record')
'''
def get_records(db_name, stmts):
    import sqlite3
    with sqlite3.connect(db_name) as db_con:
        result = []
        for stmt in stmts:
            cursor = db_con.execute(stmt)
            result.append(([name[0] for name in cursor.description], [row for row in cursor]))
        return result
