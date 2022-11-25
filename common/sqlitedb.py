import datetime
import sqlite3

from common.util import get_path_db

conn = sqlite3.connect(get_path_db())
cur = conn.cursor()
param = ('USIM5',)
sql = 'select * from alert where ticker1 = ?'

alerts = cur.execute(sql, param)

for a in alerts:
    print(str(a[4]))

conn.close()
