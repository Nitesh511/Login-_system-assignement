import unittest
import frontend.Login_Page
import backend.database
import backend.database2
import model.user
import model.supplier

class Test_connection(unittest.TestCase):
    def setUp(self):
          self.db=backend.database.DBConnect()
          self.obj = model.user.User("Nitesh", "Karki", "9841", "9840349079", "male")



    def test_get_password(self):
        self.assertEqual("9841",self.obj.get_username())


    def test_get_last(self):
        self.assertEqual("Karki",self.obj.get_username())


    def test_get_email(self):
        self.assertEqual("nitesh.karki31",self.obj.get_gender())


    def test_linear_search(self):
        list=["1","2","3","4","5"]
        item="4"
        obj=frontend.user.student.linear_search(list,item)
        self.assertEqual("4",obj)

    def test_merge_sort(self):
        list2 = ['vivek', 'manoj', 'kushwaha', 'poudel']
        obj1 = front_tend.showdetais.student.mergesort(list2)
        self.assertEqual(obj1, obj1)

    def test_update_data(self):
        name= str(input("Enter the category name: "))
        email=str(input("Enter the category email: "))
        don=str(input("Enter the category dob: "))
        address=str(input("Enter the category addess: "))
        contact=str(input("Enter the category contact: "))
        gender=str(input("Enter the category gender: "))
        roll=str(input("Enter the category roll: "))

        values = name, email,don,address,contact,gender,roll
        query = "update tbl_work set Name=%s,Email=%s,Contact=%s,DOB=%s,Address=%s,Gender=%s where Roll_No=%s"
        d = self.db.update(query, values)
        if d:
            print('succese')
        else:
            return False

        self.assertEqual(True, d)

    def test_delete(self):
        roll = int(input("Enter the Roll no: "))
        values = roll,
        query = "delete from tbl_work where Roll_No=%s"
        b = self.db.delete(query, values)
        if b:
            print('Success')
        else:
            return False
        self.assertEqual(True, b)

    def test_forget_password(self):
        query="update tbl_she set Password=%s where Email=%s"
        username=str(input("Enter your email:"))
        password= str(input("Enter your password:"))
        values=username,password
        d= self.db.update(query,values)
        if d:
            print('succese')
        else:
            return False

        self.assertEqual(True, d)

    def test_add(self):
        '''
        it test the add method of database
        '''
        query = "insert into tbl_std1(Roll_no,Name,Email,Contact,DOB,Address,Gender) values(%s,%s,%s,%s,%s,%s,%s)"
        roll= str(input('enter the  Id:'))
        name = str(input("Enter the  name: "))
        email = str(input("Enter the  email: "))
        dob = str(input("Enter the  dob: "))
        contact = str(input("Enter the  contact: "))
        address = str(input("Enter the  address: "))
        gender = str(input("Enter the  gender: "))
        values =(roll,name,email,dob,contact,address,gender)
        a=self.db.insert(query,values)
        self.assertIsNot(False,a)



    def tearDown(self):
        del self.db
        del self.obj