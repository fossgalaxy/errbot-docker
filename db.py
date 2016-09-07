from datetime import datetime
import sqlite3

class LinesTable:
    def __init__(self):
        self._conn = sqlite3.connect('lines.db')

        self._conn.execute('''CREATE TABLE IF NOT EXISTS lines
                              (time TIMESTAMP, source TEXT, target TEXT, arguments TEXT)''')

    def __del__(self):
        self._conn.close()

    def __len__(self):
        c = self._conn.execute('SELECT COUNT(*) FROM lines')
        return c.fetchone()[0]

    def add_line(self, source, target, arguments):
        now = datetime.now()
        self._conn.execute('''INSERT INTO lines(time, source, target, arguments)
                              values (?, ?, ?, ?)''', (now, source, target, arguments))



if __name__ == '__main__':
    lt = LinesTable()
    lt.add_line('source', 'target', 'arguments')
    print('Number of lines = {}'.format(len(lt)))
