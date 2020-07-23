from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import random
import os
import sqlite3
import unittest
import library

#close unclosed data.png at the end of the program

class TestLibrary(unittest.TestCase):

    @classmethod 
    def setUpClass(cls):
        a='1'
        b='test'
        c='test'
        d='test'
        e=1
        f='test'
        conn=sqlite3.connect('test_cases.db')
        conn.execute('''create table if not exists test_book_info
        (ID VARCHAR PRIMARY KEY NOT NULL,
        TITLE VARTEXT NOT NULL,
        AUTHOR VARTEXT NOT NULL,
        GENRE VARTEXT NOT NULL,
        COPIES VARINT NOT NULL,
        LOCATION VARCHAR NOT NULL);''')
        conn.commit()
        conn.execute('''create table if not exists test_book_issued
        (BOOK_ID VARCHAR NOT NULL,
        STUDENT_ID VARCHAR NOT NULL,
        ISSUE_DATE DATE NOT NULL,
        RETURN_DATE DATE NOT NULL,
        PRIMARY KEY (BOOK_ID,STUDENT_ID));''')
        conn.commit()
        conn.execute('''create table if not exists test_login
        (username VARCHAR NOT NULL,
        password VARCHAR NOT NULL);''')
        conn.commit()
        conn.execute("insert into test_book_info \
        values (?,?,?,?,?,?)",(a.capitalize(),b.capitalize(),c.capitalize(),d.capitalize(),e,f.capitalize(),));
        conn.commit()
        conn.close()

    @classmethod 
    def tearDownClass(cls):
        os.remove("test_cases.db")

    def test_Database(self):
        conn=sqlite3.connect('test_cases.db')
        self.assertIsNotNone(conn) 

    def test_login(self):
        USERNAME='admin'
        PASSWORD='password'
        conn=sqlite3.connect('test_cases.db')
        c=conn.execute("SELECT * FROM `test_login` WHERE `username` = ? AND `password` = ?", (USERNAME, PASSWORD)) 
        d=c.fetchall() 
        self.assertEqual(len(d),0)   

    def test_canvases(self):
        root=Tk()
        w = 50
        h = 50
        image2='data.png'
        with open(image2, 'rb') as image_fd:   
            photo=Image.open(image_fd)
            canvas = Canvas(root, width='%d'%w, height='%d'%h)
            canvas.image=photo
            result = canvas
            self.assertIsInstance(result,Canvas)

    def test_book(self):
        root=Tk()
        image2='data.png'
        with open(image2, 'rb') as image_fd:   
            photo=Image.open(image_fd)
            canvas = Canvas(root, width='50', height='50')
            canvas.image=photo
            result = canvas.destroy()
            self.assertIsNone(result)     

    def test_addbook(self):
        root=Tk()
        a = Canvas(root, width='50', height='50')
        a.aid='test'
        a.aauthor='test'
        a.aname='test'
        a.acopies=1
        a.agenre='test'
        a.aloc='test'
        result=Frame(a,height=500,width=650,bg='black') 
        self.assertIsNotNone(a)  
        self.assertIsNotNone(result)

    def test_rm(self):
        root=Tk()
        canvas = Canvas(root, width='50', height='50')
        self.f1=Frame(canvas,height=500,width=650,bg='black')
        result = library.menu.rm(self)
        self.assertIsNone(result)    

    def test_mainmenu(self):
        root=Tk()
        result_root = root.destroy()
        result_menu=library.menu
        self.assertIsNone(result_root)  
        self.assertIsNotNone(result_menu)

    def test_adddata(self):
        a='2'
        b='test'
        c='test'
        d='test'
        e=2
        f='test'
        conn=sqlite3.connect('test_cases.db')
        conn.execute("insert into test_book_info \
        values (?,?,?,?,?,?)",(a.capitalize(),b.capitalize(),c.capitalize(),d.capitalize(),e,f.capitalize(),));
        conn.commit()
        r = conn.execute("select count(?) from test_book_info where TITLE = ?",(b.capitalize(),b.capitalize(),))
        for i in r.fetchall():
                self.assertEqual(i[0],2)
        conn.close()
        
    def test_search(self):
        root=Tk()
        canvas = Canvas(root, width='50', height='50')
        result=Frame(canvas,height=500,width=650,bg='black')  
        self.assertIsNotNone(result)      

    def test_create_tree(self):
        root=Tk()
        test_list = ['test','test']
        canvas = Canvas(root, width='50', height='50')
        f1=Frame(canvas,height=500,width=650,bg='black')  
        result = library.menu.create_tree(self,f1,test_list)
        self.assertIsNotNone(result)

    def test_serch1(self):
        k='test'
        not_k='not_present' 
        conn=sqlite3.connect('test_cases.db')
        c=conn.execute("select * from test_book_info where ID=? OR TITLE=? OR AUTHOR=? OR GENRE=?",(k.capitalize(),k.capitalize(),k.capitalize(),k.capitalize(),))
        a=c.fetchall()  
        self.assertEqual(len(a),2)  
        c=conn.execute("select * from test_book_info where ID=? OR TITLE=? OR AUTHOR=? OR GENRE=?",(not_k.capitalize(),not_k.capitalize(),not_k.capitalize(),not_k.capitalize(),))
        a=c.fetchall()  
        self.assertEqual(len(a),0)

    def test_delete2(self):
        id='2'
        conn=sqlite3.connect('test_cases.db')
        c=conn.execute("DELETE FROM test_book_info where ID=?",(id.capitalize(),));
        a=c.fetchall()  
        self.assertEqual(len(a),0)  
        c=conn.execute("select * from test_book_info where ID=?",(id.capitalize(),))
        a=c.fetchall()  
        self.assertEqual(len(a),0)

    def test_copiesadd(self):
        id='1'
        copies=2
        conn=sqlite3.connect('test_cases.db')
        conn.execute("update test_book_info set COPIES=COPIES+? where ID=?",(copies,id,))
        conn.commit()
        r=conn.execute("select COPIES from test_book_info where ID=?",(id,))
        for i in r.fetchall():
                self.assertEqual(i[0],3)
        conn.close()

    def test_copiesdelete(self):
        id='1'
        copies=1
        conn=sqlite3.connect('test_cases.db')
        conn.execute("update test_book_info set COPIES=COPIES-? where ID=?",(copies,id,))
        conn.commit()
        r=conn.execute("select COPIES from test_book_info where ID=?",(id,))
        for i in r.fetchall():
                self.assertEqual(i[0],2)
        conn.close()

    def test_all(self):
        conn=sqlite3.connect('test_cases.db')
        c=conn.execute("select * from test_book_info")
        g=c.fetchall()
        self.assertEqual(len(g),2)  
        conn.close()    

    def test_issuedbook(self):
        bookid='1'
        studentid='1'
        conn=sqlite3.connect('test_cases.db')
        conn.execute("insert into test_book_issued \
        values (?,?,date('now'),date('now','+7 day'))",(bookid.capitalize(),studentid.capitalize(),));
        conn.commit()
        c=conn.execute("select * from test_book_issued")
        g=c.fetchall()
        self.assertEqual(len(g),1)  
        r=conn.execute("update test_book_info set COPIES=COPIES-1 where ID=?",(bookid.capitalize(),))
        conn.commit()
        r=conn.execute("select COPIES from test_book_info where ID=?",(bookid.capitalize(),))
        for i in r.fetchall():
                self.assertEqual(i[0],1)
        conn.close()
        
    def test_returnbook(self):
        bookid='1'
        studentid='1'
        conn=sqlite3.connect('test_cases.db')
        c=conn.execute("select * from test_book_issued where BOOK_ID=? and STUDENT_ID=?",(bookid.capitalize(),studentid.capitalize(),))
        d=c.fetchall()
        self.assertEqual(len(d),1)  
        conn.execute("DELETE FROM test_book_issued where BOOK_ID=? and STUDENT_ID=?",(bookid.capitalize(),studentid.capitalize(),)); 
        c=conn.execute("select * from test_book_issued where BOOK_ID=? and STUDENT_ID=?",(bookid.capitalize(),studentid.capitalize(),))
        d=c.fetchall()
        self.assertEqual(len(d),0)   
        conn.execute("update test_book_info set COPIES=COPIES+1 where ID=?",(bookid.capitalize(),))    
        conn.commit()
        r=conn.execute("select COPIES from test_book_info where ID=?",(bookid.capitalize(),))
        for i in r.fetchall():
                self.assertEqual(i[0],2)
        conn.close()

    def test_searchact(self):
        bookid='1'
        studentid='1'
        conn=sqlite3.connect('test_cases.db')
        c=conn.execute("select * from test_book_issued where BOOK_ID=? or STUDENT_ID=?",(bookid.capitalize(),studentid.capitalize(),))
        d=c.fetchall() 
        self.assertEqual(len(d),0)

    def test_searchall(self):
        conn=sqlite3.connect('test_cases.db')
        c=conn.execute("select * from test_book_issued")
        d=c.fetchall() 
        self.assertEqual(len(d),0)         
    
if __name__ == '__main__':
    unittest.main()