import sqlite3
from dataclasses import dataclass, field
from pandas import read_sql, Series, DataFrame

@dataclass
class SQLiteDB:
    """
    Class for keeping track of project
    """

    dbpath: str
    conn: sqlite3.Connection = field(init=False)
    cur: sqlite3.Cursor = field(init=False)

    def __post_init__(self):
        self.conn = sqlite3.connect(self.dbpath)
        self.cur = self.conn.cursor()

    def crt_tb_sql(self):
        """files
        proid: subproject id
        ptype: project product type, which product type's autoconf.py program in commander.yml needs to be invoked
        workdir: workdir path
        dirstat: workdir status [Y|N], default: N
        info: info.xlsx file status [Y|N], default: N
        data: data status [Y|N], default: N
        autoconf: auto config status [Y|N|err|-], default: -
        qsubsge_sh: work_qsubsge.sh file path
        pid: qsubsge_sh run pid
        p_args: qsubsge_sh run command args
        stime: qsubsge_sh execute start time
        etime: qsubsge_sh execute end time
        pstat: project status, qsubsge_work.sh execute status [run|done|err|-], default: -
        run_num: project re-run number
        """
        crt_tb_sql_c = """
        create table if not exists projects(
        id integer primary key autoincrement unique not null,
        proid text unique not null,
        ptype text,
        workdir text,
        dirstat text,
        info text,
        data text,
        autoconf text,
        qsubsge_sh text,
        pid text,
        p_args text,
        stime text,
        etime text,
        pstat text,
        run_num text,
        );"""

        self.cur.execute(crt_tb_sql_c)
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def insert_tb_sql(self, proid: str, ptype: str, workdir: str):
        insert_sql = "insert into projects (proid, ptype, workdir) values (?,?,?)"
        self.cur.execute(insert_sql, (proid, ptype, workdir))
        self.conn.commit()

    def update_tb_value_sql(self, proid: str, name: str, value: str):
        update_sql = f"update projects set \'{name}\'=\'{value}\' where proid=\'{proid}\'"
        self.cur.execute(update_sql)
        self.conn.commit()

    def query_recored(self, key: str, value: str) -> DataFrame:
        df = read_sql(f'SELECT * FROM files where {key}=\"{value}\"',con=self.conn)
        return df
    
    def query_project(self, projectid: str) -> Series:
        df = read_sql(f'SELECT * FROM files where proid=\"{projectid}\"',con=self.conn)
        return df.iloc[0,]

    def close_db(self):
        self.cur.close()
        self.conn.close()
