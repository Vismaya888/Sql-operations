import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='vismayasn@55',
    database='python',
)
mycr=mydb.cursor()
def list():
    mycr.execute("select * from data")
    r=mycr.fetchall()
    for i in r:
        print("id",i[0],"\tname :","\tage :",i[2],"\tsalary :",i[3])

def add():
    id=int(input("enter the id:"))
    n_name=input("enter the name:")
    n_age=int(input("enter your age:"))
    n_sal=int(input("enter the Salary:"))
    sql="insert into data values(%s,%s,%s,%s)"
    val=(id,n_name,n_age,n_sal)
    mycr.execute(sql,val)
    mydb.commit()
    print("Employee added successfully!")

def edit():
    id=int(input("enter the Employee Id to edit:"))
    n_name=input("enter the Employee new Name:")
    n_age=int(input("enter Employee new Age:"))
    n_sal=int(input("enter Employee new Salary:"))
    mycr.execute("update data set name=%s,age=%s,salary=%s where id=%s",(n_name,n_age,n_sal,id))
    mydb.commit()
    print("Employee information updated successfully!")

def delete():
    id=int(input("enter id of employee to delete: "))
    mycr.execute("delete from data where id=%s",(id,))
    mydb.commit()
    print("employee deleted successfully!")

c=6
while c!=5:
    print("----------------------------------")
    c=int(input("Meny\nPlease select your input \n1.List\n2.Add\n3.Edit\n4.Delete\n5.Exit\nSelect your choice: "))
    if c==1:
        list()
    elif c==2:
        add()
    elif c==3:
        edit()
    elif c==4:
        delete()
    if c==5:
        exit()

