import pymysql
import pymysql.cursors

class HRDao:
    SELECT_STATEMENT = "SELECT e.emp_id, e.emp_name, d.dept_name, j.job_title, e.hire_date, concat('$',format(e.salary, 0)) as salary"
    def __init__(self, host:str, port:int, user:str, password:str, db:str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db=db
        self.join_sql = """"""

    def get_connection(self) -> pymysql.Connection:
        return pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
    
    def select_job(self):
        """
        업무 조회 메소드
        return tuple[job_id, job_name]
        """
        sql = "SELECT job_id, job_title FROM job ORDER BY job_title"
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    def select_dept(self):
        """
        부서조회 메소드
        return tuple[dept_id, dept_name, loc]
        """
        sql = "SELECT dept_id, dept_name, loc FROM dept ORDER BY dept_name"
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()