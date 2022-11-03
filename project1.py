import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="aadhik.s",database="sulthana")
print(mydb)
def insert():
    std_id=input("Enter student id:")
    std_name=input("Enter student name:")
    std_aadhar=input("Enter student aadhaar number:")
    std_phone=input("Enter phone number:")
    mother_name=input("Enter mother's name:")
    father_name=input("Enter father's name:")
    clas=input("Enter class:")
    section=input("Enter section:")
    cursor=mydb.cursor()
    cursor.execute("""INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",(std_id,std_name,std_aadhar,std_phone,mother_name,father_name,clas,section))
    mydb.commit()
    print("\n")
    print("record inserted successfully")


def failqu():
    cursor = mydb.cursor()
    cursor.execute("""SELECT std_id FROM std_quaterly_marks WHERE eng<35||tam<35||mat<35||sci<35||social<35""")
    result = cursor.fetchall()
    for row in result:
        print(row)
        print("\n")   
def failhalf():
    cursor = mydb.cursor()
    cursor.execute("""SELECT std_id FROM std_halfyearly_marks WHERE eng<35||tam<35||mat<35||sci<35||social<35""")
    result = cursor.fetchall()
    for row in result:
        print(row)
        print("\n")   
def failann():
    cursor = mydb.cursor()
    cursor.execute("""SELECT std_id FROM std_annual_marks WHERE eng<35||tam<35||mat<35||sci<35||social<35""")
    result = cursor.fetchall()
    for row in result:
        print(row)
        print("\n")   


def view():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM STUDENT")
    result = cursor.fetchall()
    for row in result:
      print(row)
      print("\n")   
      
def update():
    print("1.std name") 
    print("2.std aadhaar") 
    print("3.phone number") 
    print("4.mother name") 
    print("5.father name") 
    print("6.class") 
    print("7.section") 

    option=int(input("enter the field you want to update"))

    if option==1:
        std_id=input("enter student id:")
        std_name=input("enter student name:")
        cur=mydb.cursor()
        sql="update student set std_name=%s where std_id=%s" 
        cur.execute(sql,(std_name,std_id))
        mydb.commit()
        view()
        print("\n")
        print("updated successfully")
    elif option==2:
        std_id=input("enter student id:")
        std_aadhar=input("enter  aadhar:")
        cur=mydb.cursor()
        sql="update student set std_aadhar=%s where std_id=%s" 
        cur.execute(sql,(std_aadhar,std_id))
        mydb.commit()
        view()
        print("\n")
        print("updated successfully")

    elif option==3:
        std_id=input("enter student id:")
        std_phone=input("enter student phone number:")
        cur=mydb.cursor()
        sql="update student set std_phone=%s where std_id=%s" 
        cur.execute(sql,(std_phone,std_id))
        mydb.commit()
        view()
        print("\n")
        print("updated successfully")

    elif option==4:
        std_id=input("enter student id:")
        mother_name=input("enter mother name:")
        cur=mydb.cursor()
        sql="update student set mother_name=%s where std_id=%s" 
        cur.execute(sql,(mother_name,std_id))
        mydb.commit()
        view()
        print("\n")
        print("updated successfully")

    elif option==5:
        std_id=input("enter student id:")
        father_name=input("enter  father name:")
        cur=mydb.cursor()
        sql="update student set father_name=%s where std_id=%s" 
        cur.execute(sql,(father_name,std_id))
        mydb.commit()
        view()
        print("\n")
        print("updated successfully")

    elif option==6:
        std_id=input("enter student id:")
        clas=input("enter class:")
        cur=mydb.cursor()
        sql="update student set class=%s where std_id=%s" 
        cur.execute(sql,(clas,std_id))
        mydb.commit()
        view()
        print("\n")
        print("updated successfully")

    elif option==7:
        std_id=input("enter student id:")
        section=input("enter section:")
        cur=mydb.cursor()
        sql="update student set section=%s where std_id=%s" 
        cur.execute(sql,(section,std_id))
        mydb.commit()
        view()
        print("\n")
        print("updated successfully")
    else:
        print("invalid")

def delete():
    std_id=input("enter your id")
    res=mydb.cursor()
    
    sql="DELETE from student WHERE std_id=%s"
    res.execute(sql,(std_id,))
    mydb.commit()
    print("record deleted successfully")
while True:
    print("press 1 for admin and 2 for teacher")
    v=int(input())
    if v==1:
            print("\n")
            print("1.add record")
            print("2.view record")
            print("3.update record")
            print("4.delete record")
            print("5.exit")
            print("\n")
            choice=int(input("enter your choice:"))
            if choice==1:
                insert()
            elif choice==2:
                view()
            elif choice==3:
                update()
            elif choice==4:
                delete()
            elif choice==5:
                quit()
            else:
                print("invalid option....!!!")
    elif v==2:
        print("ENTER YOUR CHOICE:")
        print("1.ENTER MARKS")
        print("2.FILTER FAILED STUDENTS")
        k=int(input())
        if k==1:
            print("enter the exam name")
            print("1.quaterly")
            print("2.halfyearly")
            print("3.annual")
            exam=int(input())
            if exam==1:
                std_id=int(input("enter student id"))
                eng=int(input("enter english mark"))
                tam=int(input("enter tamil marks"))
                mat=int(input("enter maths mark"))
                sci=int(input("enter science mark"))
                social=int(input("enter social marks"))
                curs=mydb.cursor()
                curs.execute("""INSERT INTO std_quaterly_marks VALUES(%s,%s,%s,%s,%s,%s)""",(std_id,eng,tam,mat,sci,social))
                mydb.commit()
                print("\n")
                print("record inserted successfully")
            elif  exam==2:
                std_id=int(input("enter student id"))
                eng=int(input("enter english mark"))
                tam=int(input("enter tamil marks"))
                mat=int(input("enter maths mark"))
                sci=int(input("enter science mark"))
                social=int(input("enter social marks"))
                cursor=mydb.cursor()
                cursor.execute("""INSERT INTO STD_HALFYEARLY_MARKS VALUES(%s,%s,%s,%s,%s,%s)""",(std_id,eng,tam,mat,sci,social))
                mydb.commit()
                print("\n")
                print("record inserted successfully")
            elif exam==3:
                std_id=int(input("enter student id"))
                eng=int(input("enter english mark"))
                tam=int(input("enter tamil marks"))
                mat=int(input("enter maths mark"))
                sci=int(input("enter science mark"))
                social=int(input("enter social marks"))
                cursor=mydb.cursor()
                cursor.execute("""INSERT INTO STD_ANNUAL_MARKS VALUES(%s,%s,%s,%s,%s,%s)""",(std_id,eng,tam,mat,sci,social))
                mydb.commit()
                print("\n")
                print("record inserted successfully")
            
        if k==2:
            print("enter the exam name:")
            print("1.quaterly")
            print("2.halfyearly")
            print("3.annual exam")
            s=int(input())
            if s==1:
                failqu()
            elif s==2:
                failhalf()
            elif s==3:
                failann()
            else: 
                print("invalid option")