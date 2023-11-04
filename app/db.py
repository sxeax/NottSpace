import pugsql

queries = pugsql.module('./db/queries')

queries.connect('sqlite:///db/nottspacedb.db')
