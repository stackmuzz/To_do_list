import psycopg2

db_name="tasklistDB"
db_user="tasklist_user"
db_pw="1234"
db_host="localhost"

def getTaskList():
    conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pw,host=db_host)
    cur=conn.cursor()
    cur.execute('SELECT id,task_name,is_done FROM public."taskList"')
    tasklist=cur.fetchall()
    cur.close()
    conn.close()
    return tasklist

def addTask(taskname,duedate):
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute('INSERT INTO public."taskList"(task_name,is_Done) values(\'%s\',\'%s\');commit;'%(taskname,duedate))

    cur.close()
    conn.close()

def updateTask(taskname,id,done):
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute('UPDATE  public."taskList" SET task_name=\'%s\',is_done=\'%s\'  WHERE id=\'%s\'; ' % (taskname,done,id))
    conn.commit()
    cur.close()
    conn.close()
def deleteTask(id):
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute('DELETE FROM public."taskList"  WHERE id=\'%s\'; ' % ( id))
    conn.commit()
    cur.close()
    conn.close()