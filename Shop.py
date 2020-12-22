from tkinter import *
import sqlite3
from datetime import date
from tkinter import ttk
from sqlite3 import Error
from tkinter import messagebox
db=sqlite3.connect('books.db')
class Shop:
		
		
		def addbook(self):
			
			self.fm=Frame(self.root,bg='#a7ecd9',width=1200,height=800).place(x=0,y=100)
			self.fm1=Frame(self.fm,bg='#fff',width=650,height=710,bd=5,relief='flat').place(x=200,y=150)
			self.clradd()
			self.backbt = Button(self.fm, width=4, bg='#a7ecd9',text="Back",activebackground='#a7ecd9', bd=0, relief='flat',command=self.cur).place(x=20, y=130)
			self.f=Frame(self.fm,bg='brown',width=650,height=100).place(x=200,y=150)
			
			self.ll=Label(self.f,text='ADD BOOKS',fg='#fff',bg='brown',font=('Arial',17,'bold')).place(x=320,y=155)
#labels and entry of add book........			
			
			self.lb2 = Label(self.fm1, text='Title', fg='black', bg='#fff', font=('Arial', 12, 'bold')).place(x=250, y=270)
			
			self.ee1=Entry(self.fm1,width=15,bd=4,relief='groove',textvariable=self.ttl,font=('arial',10,'bold')).place(x=400,y=270)
			
			self.lb3 = Label(self.fm1, text='Author', fg='black', bg='#fff', font=('Arial', 12, 'bold')).place(x=240, y=370)
			
			self.ee2=Entry(self.fm1,width=15,bd=4,relief='groove',textvariable=self.aut,font=('arial',10,'bold')).place(x=400,y=370)
			
			self.lb4= Label(self.fm1, text='Edition', fg='black', bg='#fff', font=('Arial', 12, 'bold')).place(x=240, y=470)
			
			self.ee3=Entry(self.fm1,width=15,bd=4,relief='groove',textvariable=self.edt,font=('arial',10,'bold')).place(x=400,y=470)
			
			self.lb5 = Label(self.fm1, text='Price', fg='black', bg='#fff', font=('Arial', 12, 'bold')).place(x=245, y=570)
			
			self.ee4=Entry(self.fm1,width=15,bd=4,relief='groove',textvariable=self.pri,font=('arial',10,'bold')).place(x=400,y=570)
			
			self.lb=Label(self.fm1,text='Copys',fg='black',bg='#fff',font=('Arial',12,'bold')).place(x=250,y=670)
			
			self.ee5=Entry(self.fm1,width=15,bd=4,relief='groove',textvariable=self.cpy,font=('arial',10,'bold')).place(x=400,y=670)
			
			self.bt=Button(self.fm1,text='Submit',width=10,bg='red',fg='#fff',font=('Arial',10,'bold'),bd=5,
relief='flat',command=self.submit1).place(x=480,y=760)


#insert data in database.....			
		def submit1(self):
			
			if self.ttl.get()=="" or self.aut.get()=="" or self.edt.get()=="" or self.pri.get()=="" or self.cpy.get()=="":
			        messagebox.showerror('Error','PLEASE INSERT ALL DATA..... ')
			        self.clradd()
			else:
				cursor=db.cursor()
				cursor.execute("INSERT INTO bookinfo(title, author,edition, price, copys) values(?,?,?,?,?)",(self.ttl.get(),self.aut.get(),self.edt.get(),self.pri.get(),self.cpy.get()))
				
				db.commit()
				msgbox=messagebox.askquestion('SUCCESSFUL','YOU WANT ADD MORE ?')
				
				if msgbox != 'yes':
					self.cur()
				self.clradd()

		def sellbook(self):
			self.price=0
			self.count=0
			
			
			self.fram=Frame(self.root,bg='#a7ecd9',width=1200,height=800).place(x=0,y=100)
			
			self.fram1=Frame(self.fram,bg='#fff',width=650,height=710,bd=5,relief='flat').place(x=200,y=150)
			
			self.backbt = Button(self.fram, width=4, bg='#a7ecd9',text="Back",activebackground='#a7ecd9', bd=0, relief='flat',command=self.cur).place(x=20, y=130)
			
			self.f1=Frame(self.fram,bg='midnightblue',width=650,height=100).place(x=200,y=150)
			
			self.ll=Label(self.f1,text='SELL BOOKS',fg='#fff',bg='midnightblue',font=('Arial',17,'bold')).place(x=320,y=155)
#labels and entry of add book........			
			
			
			
			Label(self.fram1, text='Name', fg='black', bg='#fff', font=('Arial', 12, 'bold')).place(x=240, y=350)
			
			Entry(self.fram1,width=15,bd=4,relief='groove',textvariable=self.name,font=('arial',10,'bold')).place(x=400,y=350)
			
			
			Label(self.fram1, text='Contact', fg='black', bg='#fff', font=('Arial', 12, 'bold')).place(x=220, y=470)
		
			Entry(self.fram1,width=15,bd=4,relief='groove',textvariable=self.no,font=('arial',10,'bold')).place(x=400,y=470)
			
			self.no.set(" ")
			self.name.set("")
			
			
			
			self.bt=Button(self.fram1,text='Add Book',width=10,bg='red',fg='#fff',font=('Arial',10,'bold'),bd=5,
relief='flat',command=self.booksell).place(x=480,y=600)

		def booksell(self):
			if self.name.get()=="" or self.no.get()==" ":
				messagebox.showerror('Error','PLESE INSERT ALL DATA..... ')
				self.name.set("")
				self.no.set(" ")
				
			else:
				self.clradd()
				self.new=Frame(self.fram1,bg='gold',height=620,width=650).place(x=185,y=250)
				
				self.lb1 = Label(self.new, text='Title', bg='gold', fg='black', font=('arial', 12, 'bold')).place(x=250,y=300)
				self.p=Entry(self.new,width=12,bd=4,relief='groove',textvariable=self.ttl,font=('arial',10,'bold')).place(x=500,y=300)
				
				self.lb2=Label(self.new,text='Author',bg='gold',fg='black',font=('arial',12,'bold')).place(x=250,y=400)
				Entry(self.new,width=12,bd=4,relief='groove',textvariable=self.aut,font=('arial',10,'bold')).place(x=500,y=400)
				
				
				
				
				
				self.lb4 = Label(self.new, text="Copys", bg='gold', fg='black', font=('arial', 12, 'bold')).place(x=250, y=500)
				Entry(self.new,width=12,bd=4,relief='groove',textvariable=self.cpy,font=('arial',10,'bold')).place(x=500,y=500)
				
			
				
				self.bt=Button(self.new,text='ADD',width=10,bg='coral',fg='#fff',font=('Arial',8,'bold'),bd=5,
relief='flat',command=self.selling).place(x=350,y=600)
			
		def selling(self):
			if self.ttl.get()=="" or self.aut.get()=="" or self.cpy.get()=="":
				messagebox.showerror('Error','PLEASE INSERT ALL DATA..... ')
				self.clradd()
			else:
				cursor=db.cursor()
				que=("SELECT * FROM bookinfo WHERE title=? AND author=?")
				cursor.execute(que,(self.ttl.get(),self.aut.get(),))
				db.commit()
				self.val=cursor.fetchone()
				if self.val!=None:
					
					try:
						self.copys=int(self.cpy.get())
						
#checking stock					
						if self.val[4]>self.copys:
#copy not be zero							
							if self.copys<=0:
								messagebox.showerror('ERROR', 'COPY MUST BE 1')
								self.cpy.set("")
								
							else:
								
								self.price=self.price+self.val[3]*self.copys
							
								qu=("update bookinfo set copys=? where title=?")
								cursor.execute(qu,(self.val[4]-self.copys,self.ttl.get(),))
								db.commit()
								
								cursor.execute("INSERT INTO selling(title, author,price, copy,name,contact) values(?,?,?,?,?,?)",(self.ttl.get(),self.aut.get(),self.val[3],self.copys,self.name.get(),self.no.get()))
				
			
								
								db.commit()
								self.count=self.count+1
								
								
								msgbox=messagebox.askquestion('SUCCESSFUL','YOU WANT ADD MORE ?')
								if msgbox == 'yes':
									self.booksell()
								else:
									self.billing()	
					#billing function	
						else:
							messagebox.showerror('ERROR', 'ONLY ' +str(self.val[4])+' ARE LEFT')
							
					except Exception as e:
						messagebox.showerror('ERROR', e)
						self.cpy.set("")
					
    
				else:
					messagebox.showerror('ERROR', 'BOOK NOT FOUND')
					self.clradd()
					
				
	       				
#billing........

		def billing(self):
			#self.count=3
			v=self.count
			
			self.bil=Frame(self.root,bg='#fff',width=1200,height=800).place(x=0,y=100)
			
			cursor=db.cursor()
			cursor.execute("SELECT * FROM  selling ORDER BY id DESC LIMIT '"+str(v)+"'" )
		
			db.commit()
			self.rows=cursor.fetchall()
			
			if len(self.rows)!=0:
					self.val=self.rows[0]
					Label(self.bil, text="No.", bg='#fff', fg='black', font=('Arial', 12, 'bold')).place(x=50, y=100)
					
					Label(self.bil, text=self.val[0]-v, bg='#fff', fg='black', font=('Arial', 12, 'bold')).place(x=140, y=100)
					
					Label(self.bil, text="Date ", bg='#fff', fg='black', font=('Arial', 12, 'bold')).place(x=830, y=100)
					
					today=date.today()
					t1=today.strftime("%d/%m/%Y")
				
					Label(self.bil, text=t1, bg='#fff', fg='black', font=('Arial', 12, 'bold')).place(x=940, y=100)
					
					Label(self.bil, text="Customer Information", bg='#fff', fg='black', font=('Arial', 15, 'bold')).place(x=300, y=180)
#for table.....					
					p=0
					for i in range(118):
						
						Label(self.bil, text="___", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=0+p, y=150)
						Label(self.bil, text="___", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=0+p, y=340)
						
						
						Label(self.bil, text="---", bg='#fff', fg='black', font=('Arial', 3, 'bold')).place(x=0+p, y=250)
						
						Label(self.bil, text="___", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=0+p, y=400)
						
						Label(self.bil, text="___", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=0+p, y=800)
						Label(self.bil, text="___", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=650+p, y=850)
						
						Label(self.bil, text="___", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=0+p, y=900)
					
						
						p=p+10
						
# Labels......

												
					Label(self.bil, text="Name:-", bg='#fff', fg='black', font=('Arial', 10, 'bold')).place(x=50, y=280)
					
					
					Label(self.bil, text=self.val[5], bg='#fff', fg='black', font=('Arial', 10, 'bold')).place(x=200, y=280)
					
					Label(self.bil, text="Mob:-", bg='#fff', fg='black', font=('Arial', 10, 'bold')).place(x=750, y=280)
					
					Label(self.bil, text=self.val[6], bg='#fff', fg='black', font=('Arial', 10, 'bold')).place(x=880, y=280)

										
				
#headings.......					
					Label(self.bil, text="Id", bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=20, y=370)
					
					Label(self.bil, text="Title", bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=120, y=370)
					Label(self.bil, text="Author", bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=320, y=370)
					
					Label(self.bil, text="Price", bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=520, y=370)
					
					Label(self.bil, text="Qty.", bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=720, y=370)
					
					Label(self.bil, text="Amount", bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=920, y=370)
					self.NO=0
					a=0
					add=0
					
											
					while self.count!=0:
																							
																							self.count=self.count-1
																							
																							self.NO=self.NO+1
																							self.row=self.rows[self.count]
																							
																							for i in range(0,6):
																								
																								self.val=self.row[int(i)]
																								if i==0:
																									Label(self.bil, text=self.NO, bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=20, y=430+a)
																								elif i==1:
																									Label(self.bil, text=self.val, bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=120, y=430+a)
																									
																								elif i==2:
																									Label(self.bil, text=self.val, bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=320, y=430+a)
																								elif i==3:
																									Label(self.bil, text=self.val, bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=520, y=430+a)
																									pri=self.val
																								elif i==4:
																									Label(self.bil, text=self.val, bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=720, y=430+a)
																									cpy=self.val
																								else:
																									add=add+(pri*cpy)
																									Label(self.bil, text=pri*cpy, bg='#fff', fg='black', font=('Arial',8, 'bold')).place(x=920, y=430+a)
																									Label(self.bil, text="Total", bg='#fff', fg='black', font=('Arial',20, 'bold')).place(x=800, y=850)
																									Label(self.bil, text=add, bg='#fff', fg='black', font=('Arial',20, 'bold')).place(x=920, y=850)
																									a=a+50
																								Button(self.bil, width=4, bg='#a7ecd9',text="print",activebackground='#a7ecd9', bd=0, relief='flat',command=self.login).place(x=520, y=850)
																								
																				
																										
																												

#vartical	
					
											
					p=0
					for i in range(55):
							Label(self.bil, text="|", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=0, y=340+p)
							
							Label(self.bil, text="|", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=850, y=350+p)
							
							p=p+10
					
					p=0
					for i in range(45):
							Label(self.bil, text="|", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=50, y=350+p)
							
							Label(self.bil, text="|", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=1150, y=350+p)
							
							Label(self.bil, text="|", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=250, y=350+p)
							
							Label(self.bil, text="|", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=450, y=350+p)
							
							Label(self.bil, text="|", bg='#fff', fg='black', font=('Arial', 5, 'bold')).place(x=650, y=350+p)
							
							
							p=p+10
						
						
					  
			
#edit books...........			
		def edit(self):
			self.ffm=Frame(self.root,bg='#a7ecd9',width=1200,height=800).place(x=0,y=100)
			
			self.backbt = Button(self.ffm, width=4, bg='#a7ecd9',text="Back",activebackground='#a7ecd9', bd=0, relief='flat',command=self.login).place(x=20, y=130)
			
			self.fm1 = Frame(self.ffm, bg='#fff', width=700, height=500, bd=5, relief='flat').place(x=200, y=150)
			self.ed = Frame(self.fm1, bg='silver', bd=0, relief='flat', width=700, height=100).place(x=200,y=150)
			
			self.lab = Label(self.ed, text='EDIT BOOKS DETAILS', bg='silver', fg='#fff', font=('Arial', 14, 'bold')).place(x=300, y=170)
			
			self.label3=Label(self.fm1,text='Book Name',bg='#fff',fg='black',font=('arial',10,'bold')).place(x=230,y=300)
			
			self.entry=Entry(self.fm1,width=15,bd=4,relief='groove',textvariable=self.E3,font=('arial',10,'bold')).place(x=450,y=300)
			
			
			
			self.button7 = Button(self.fm1, text='Search', bg='tomato', fg='#fff', width=10, height=0,font=('Arial', 10, 'bold'),command=self.editsearch).place(x=400,y=410)

		
				
#search of books..........					
		def editsearch(self):
		                   cursor=db.cursor()
		                   cursor.execute("SELECT * FROM bookinfo WHERE title='"+self.E3.get()+"'" )
		                   db.commit()
		                   self.val=cursor.fetchone()
		                   if self.val!=None:
		                   	self.fr1 = Frame(self.root, bg='#fff', width=700, height=780, bd=5, relief='flat').place(x=200, y=150)
		                   	self.f=Frame(self.root,bg='darkorange',width=700,height=100).place(x=200,y=150)
		                   	self.ll=Label(self.root,text='EDIT BOOKS',fg='#fff',bg='darkorange',font=('Arial',17,'bold')).place(x=340,y=155)
		                   	
		                   	self.lb2 = Label(self.fm1, text='Title', fg='black', bg='#fff', font=('Arial', 12, 'bold')).place(x=250, y=270)
		                   	
		                   	self.ee1=Entry(self.fm1,width=15,bd=4,textvariable=self.En1,relief='groove',font=('arial',10,'bold')).place(x=400,y=270)
		                   	
		                   	self.lb3 = Label(self.fm1, text='Author', fg='black', bg='#fff', font=('Arial', 12, 'bold')).place(x=240, y=370)
		                   	
		                   	self.ee2=Entry(self.fm1,width=15,bd=4,textvariable=self.En2,relief='groove',font=('arial',10,'bold')).place(x=400,y=370)
		                   	
		                   	self.lb4= Label(self.fm1, text='Edition', fg='black', bg='#fff', font=('Arial', 12, 'bold')).place(x=240, y=470)
		                   	
		                   	self.ee3=Entry(self.fm1,width=15,bd=4,textvariable=self.En3,relief='groove',font=('arial',10,'bold')).place(x=400,y=470)
		                   	
		                   	
		                   	self.lb5 = Label(self.fm1, text='Price', fg='black', bg='#fff', font=('Arial', 12, 'bold')).place(x=245, y=570)
		                   	
		                   	self.ee4=Entry(self.fm1,width=15,bd=4,textvariable=self.En4,relief='groove',font=('arial',10,'bold')).place(x=400,y=570)
		                   	
		                   	self.lb=Label(self.fm1,text='Copys',fg='black',bg='#fff',font=('Arial',12,'bold')).place(x=250,y=670)
		                   	
		                   	self.ee5=Entry(self.fm1,width=15,bd=4,textvariable=self.En5,relief='groove',font=('arial',10,'bold')).place(x=400,y=670)
		                   	
		                   	self.En1.set(self.val[0])
		                   	
		                   	self.En2.set(self.val[1])
		                   	
		                   	self.En3.set(self.val[2])
		                   	
		                   	self.En4.set(self.val[3])
		                   	
		                   	self.En5.set(self.val[4])
		                   	
		                   	self.bt=Button(self.fm1,text='Submit',width=10,bg='red',fg='#fff',font=('Arial',10,'bold'),bd=5,
relief='flat',command=self.editbook).place(x=480,y=760)



		                   else:
		                   	messagebox.showerror('Error', 'PLEASE! CORRECT BOOK Name')
		                   	self.E3.set("")
		                  #self.clear()
		def editbook(self):
			self.datas= self.En1.get()
			cursor= db.cursor()
			que=("UPDATE bookinfo SET title=?,author=?,edition=?,price=?,copys=? WHERE title=?")
			data=(self.En1.get(),self.En2.get(),self.En3.get(),self.En4.get(),self.En5.get(),self.datas)
			cursor.execute(que,data)
			db.commit()
			messagebox.showinfo('Book Shop','YOUR DATA IS UPDATED!')
			self.edit()
			self.E3.set("")           
#back to home page......
		def cur(self):
			self.login()
			


#delete button code........			
		def delete(self):
			self.fra1=Frame(self.root,bg='#a7ecd9',width=1200,height=800).place(x=0,y=100)
			
			self.fra2 = Frame(self.fra1, bg='#fff', width=700, height=500, bd=5, relief='flat').place(x=200, y=150)
			
			self.backbt = Button(self.fra1, width=4, bg='#a7ecd9',text="Back",activebackground='#a7ecd9', bd=0, relief='flat',command=self.cur).place(x=20, y=130)
			
			self.fr3 = Frame(self.fra2, bg='gold', bd=0, relief='flat', width=700, height=100).place(x=200,y=150)
			
			self.lab = Label(self.fr3, text='DELETE BOOKS', bg='gold', fg='#fff', font=('Arial', 14, 'bold')).place(x=370, y=170)
			
			self.label3=Label(self.fra2,text='Book Name',bg='#fff',fg='black',font=('arial',10,'bold')).place(x=230,y=300)
			
			self.entry=Entry(self.fra2,width=15,bd=4,relief='groove',textvariable=self.E4,font=('arial',10,'bold')).place(x=450,y=300)
			
			
			
			self.button7 = Button(self.fra2, text='Delete', bg='teal', fg='#fff', width=10, height=0,font=('Arial', 10, 'bold'),command=self.deletebook).place(x=400,y=410)

		def deletebook(self):
			                  	self.a=self.E4.get()
			                  	cursor=db.cursor()
			                  	cursor.execute("SELECT * FROM bookinfo WHERE title='"+self.a+"'")
			                  	db.commit()
			                  	self.da=cursor.fetchone()
			                  	que=("DELETE FROM bookinfo WHERE title=?")
			                  	cursor.execute(que,(self.a,))
			                  	
			                  	db.commit()
			                  	self.E4.set("")
			                  	if self.da!=None:
			                  		msgbox=messagebox.askquestion('SUCCESSFUL','YOU WANT DELETE MORE ?')
			                  		if msgbox == 'yes':
			                  			pass
			                  		else:
			                  			self.cur()
			                  	else:
			                  		messagebox.showerror('Library System','YOUR 	DATA IS NOT FOUND !')	

         
		
		def search(self):
			self.fa1=Frame(self.root,bg='#a7ecd9',width=1200,height=800).place(x=0,y=100)
			
			self.fa2 = Frame(self.fa1, bg='#fff', width=700, height=500, bd=5, relief='flat').place(x=200, y=150)
			
			self.backbt = Button(self.fa1, width=4, bg='#a7ecd9',text="Back",activebackground='#a7ecd9', bd=0, relief='flat',command=self.cur).place(x=20, y=130)
			
			self.fa3 = Frame(self.fa2, bg='coral', bd=0, relief='flat', width=700, height=100).place(x=200,y=150)
			
			self.lab = Label(self.fa3, text='SEARCH BOOKS', bg='coral', fg='#fff', font=('Arial', 14, 'bold')).place(x=370, y=170)
			
			self.label3=Label(self.fa2,text='Book Name',bg='#fff',fg='black',font=('arial',10,'bold')).place(x=230,y=300)
			
			self.entry=Entry(self.fa2,width=15,bd=4,relief='groove',textvariable=self.E5,font=('arial',10,'bold')).place(x=450,y=300)
			
			
			
			self.button7 = Button(self.fa2, text='Search', bg='indigo', fg='#fff', width=10, height=0,font=('Arial', 10, 'bold'),command=self.searchbook).place(x=400,y=410)
		def exit(self):
					self.top.destroy()
					self.E5.set("")	
		def searchbook(self):
			self.emp=self.E5.get()
			self.a=self.aut.get()
			cursor=db.cursor()
			cursor.execute("SELECT * FROM bookinfo WHERE title='"+self.emp+"'")
			db.commit()
			self.srval=cursor.fetchone()
			if self.srval!=None:
				self.top=Tk()
				self.top.title("BOOK SHOP")
				self.top.geometry("665x550+195+250")
				self.top.resizable(0, 0)
				self.top.configure(bg='skyblue')
				
				#self.frm=Frame(self.top,bg='#0f624c',width=300,height=35).place(x=0,y=0)
				
				#self.mnlb=Label(self.frm,bg='#0f624c',fg='#fff',text="Avaliable",font=('arial',11,'bold')).place(x=120,y=5)
				
				self.lb1 = Label(self.top, text='Title', bg='skyblue', fg='blue', font=('arial', 12, 'bold')).place(x=100,y=80)
				
				self.lb2=Label(self.top,text=self.srval[0],bg='skyblue',fg='blue',font=('arial',12,'bold')).place(x=400,y=80)
				
				self.lb3 = Label(self.top, text='Author', bg='skyblue', fg='blue', font=('arial', 12, 'bold')).place(x=100, y=160)
				self.lb4 = Label(self.top, text=self.srval[1], bg='skyblue', fg='blue', font=('arial', 12, 'bold')).place(x=400, y=160)
				
				self.lb5 = Label(self.top, text='Edition', bg='skyblue', fg='blue', font=('arial', 12, 'bold')).place(x=100, y=240)
				
				self.lb6 = Label(self.top, text=self.srval[2], bg='skyblue', fg='blue', font=('arial', 12, 'bold')).place(x=400, y=240)
				
				Label(self.top, text='Price', bg='skyblue', fg='blue', font=('arial', 12, 'bold')).place(x=100, y=320)
				
				Label(self.top, text=self.srval[3], bg='skyblue', fg='blue', font=('arial', 12, 'bold')).place(x=400, y=320)
				
				Label(self.top, text='Copys', bg='skyblue', fg='blue', font=('arial', 12, 'bold')).place(x=100, y=400)
				
				Label(self.top, text=self.srval[4], bg='skyblue', fg='blue', font=('arial', 12, 'bold')).place(x=400, y=400)
				
				Button(self.top, text='Ok', bg='black', fg='#fff', width=10, height=0,font=('Arial', 10, 'bold'),command=self.exit).place(x=250,y=510)
				self.E5.set("")
				
			else:
				messagebox.showwarning('Library System','YOUR DATA IS NOT AVAILABLE !')
				self.E5.set("")

			
				
		def clradd(self):
			self.ttl.set("")
			self.aut.set("")
			self.edt.set("")
			self.pri.set("")
			self.cpy.set("")
						
#back to login page........			
		def logout(self):
		
			self.root.destroy()
			code=Tk()
			obj=Shop(code)
			code.mainloop()				
	   
		def showbook(self) :
			self.fc = Frame(self.root, bg='#a7ecd9', width=900, height=390).place(x=0, y=110)
			
			self.popframe=Frame(self.fc,width=900,height=30,bg='#0f624c').place(x=0,y=0)
			
			self.lbn=Label(self.popframe,bg='#0f624c',text='BOOKS INFORMATION',fg='#fff',font=('arial',10,'bold')).place(x=380,y=5)
			
			self.backbt = Button(self.popframe,width=10, text="back",bg='#0f624c',activebackground='#0f624c',bd=0, relief='flat', command=self.cur).place(x=0, y=0)
			
			self.table_frame=Frame(self.fc,bg='#fff',bd=1,relief='flat').place(x=0,y=30,width=900,height=360)
			
			self.scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
			
			self.scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
			
			self.book_table=ttk.Treeview(self.table_frame,columns=("Title","Author","Edition","Price","Copys"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
			self.scroll_x.pack(side=BOTTOM,fill=X)
			self.scroll_y.pack(side=RIGHT, fill=Y)
			self.scroll_x.config(command=self.book_table.xview)
			self.scroll_y.config(command=self.book_table.yview)
			
			self.book_table.heading("Title", text="Title")
			self.book_table.heading("Author", text="Author")
			self.book_table.heading("Edition", text="Edition")
			self.book_table.heading("Price", text="Price")
			self.book_table.heading("Copys",text="Copys")
			self.book_table['show']='headings'
			
			self.book_table.column("Title", width=200)
			self.book_table.column("Author", width=200)
			self.book_table.column("Edition", width=120)
			self.book_table.column("Price", width=110)
			self.book_table.column("Copys",width=200)
			self.book_table.pack(fill=BOTH,expand=1)
			
			
			cursor=db.cursor()
			cursor.execute("SELECT * FROM bookinfo")
			self.rows=cursor.fetchall()
			if len(self.rows)!=0:
				for self.row in self.rows:
					self.book_table.insert('',END,values=self.row)
					db.commit()

			
		      
#home page afte login......
		def login(self):
			if self.E1.get()=="1" :#and self.E1.get()=="1234":							
			
				self.fm2=Frame(self.root,bg='cyan',height=100,width=1200).place(x=0,y=0)
				
				
				
			
				self.lb3=Label(self.fm2,text='BOOK STORE',fg='grey',bg='cyan',font=('Arial',20,'bold')).place(x=275,y=0)
				
				self.fm3=Frame(self.root,bg='grey',height=800,width=1200).place(x=0,y=100)
		
			#self.canvas = Canvas(self.fm2, bg='white', width=1200, height=800).place(x=5, y=110)
			#self.photo9=PhotoImage(file="/storage/emulated/0/Project Python/dipak/Library management System GUI/Library management System GUI/images (17).png")
			#self.canvas.create_image(0,0,image=self.photo9,anchor=NW)

#Button.........			
				self.bt1=Button(self.fm3,text='  Add Books',fg='#fff',bg='#ff0076',font=('Arial',10,'bold'),width=10,height=0,bd=7,relief='flat',command=self.addbook,cursor='hand2').place(x=50,y=200)
			
				self.bt2=Button(self.fm3,text=' Sell Books',fg='#fff',bg='#ff0076',font=('Arial',10,'bold'),width=10,height=0,bd=7,relief='flat',command=self.sellbook,cursor='hand2').place(x=500,y=200)
			
				self.bt3=Button(self.fm3,text=' Edit Books',fg='#fff',bg='#ff0076',font=('Arial',10,'bold'),width=10,height=0,bd=7,relief='flat',command=self.edit,cursor='hand2').place(x=50,y=400)
			
				self.bt4=Button(self.fm3,text=' Delete Books',fg='#fff',bg='#ff0076',font=('Arial',10,'bold'),width=10,height=0,bd=7,relief='flat',command=self.delete,cursor='hand2').place(x=500,y=400)
			
				self.bt5=Button(self.fm3,text=' Show Books',fg='#fff',bg='#ff0076',font=('Arial',10,'bold'),width=10,height=0,bd=7,relief='flat',command=self.showbook,cursor='hand2').place(x=50,y=600)
			
				self.bt6=Button(self.fm3,text=' Search Books',fg='#fff',bg='#ff0076',font=('Arial',10,'bold'),width=10,height=0,bd=7,relief='flat',command=self.search,cursor='hand2').place(x=500,y=600)
			
				self.bt8 = Button(self.fm3, text='  log Out', fg='#fff', bg='#ff0076', font=('Arial', 10, 'bold'),width=10,height=0, bd=7, relief='flat',cursor='hand2',command=self.logout).place(x=250, y=280)
#			
			
			
			
			
			

			else:
				messagebox.showerror('Error', 'Your ID or Password is not Valid')
				self.clear()

#clear method			
		def clear(self):
	         self.E1.set("")
	         self.E2.set("")
	    
	#login page .......         
		def __init__(self,root):
			self.root=root
			self.root.geometry("1350x700+0+0")
			self.E1=StringVar()
			self.E2=StringVar()
			self.E3=StringVar()
			self.E4=StringVar()
			self.E5=StringVar()
			self.En1=StringVar()
			self.En2=StringVar()
			self.En3=StringVar()
			self.En4=IntVar()
			self.En5=IntVar()
			self.se1=StringVar()
			self.name=StringVar()
			self.no=StringVar()
			self.ttl=StringVar()
			self.aut=StringVar()
			self.edt=StringVar()
			self.pri=StringVar()
			self.cpy=StringVar()
			
			self.fm=Frame(root,height=800,width=1200,bg='white').place(x=0,y=0)
			self.fm2=Frame(self.fm,height=600,width=600,bg='grey').place(x=260,y=10)
			
			self.title=Label(self.fm2,text='           Login          ',fg='cyan',bg="grey",font=('Arial',20,'bold')).place(x=260,y=50)
			
			self.uname=Label(self.fm2,text=' User ID ',fg='white',bg="grey",font=('Arial',12,'bold')).place(x=280,y=250)
			
			self.e1=Entry(self.fm2,width=12,font=('arial',10,'bold'),textvariable=self.E1,bd=5,relief='groove').place(x=520,y=248)
			
			self.password=Label(self.fm2,text='Password',bg="grey",fg="white",font=('Arial',12,'bold')).place(x=280,y=350)
			
			self.e2=Entry(self.fm2,show='*',width=12,font=('arial',10,'bold'),textvariable=self.E2,bd=5,relief='groove').place(x=520,y=350)
			
			self.btn1=Button(self.fm2,text='  Login ',fg='white',bg='grey',width=5,font=('Arial',10,'bold'),activebackground='white',activeforeground='black',command=self.login,bd=3,relief='flat',cursor='hand2').place(x=320,y=480)
			
			self.btn2=Button(self.fm2,text=' Clear ',fg='white',bg='grey',width=5,font=('Arial',10,'bold'),activebackground='white',activeforeground='black',command=self.clear,bd=3,relief='flat',cursor='hand2').place(x=620,y=480)
			
		
		
root=Tk()
obj=Shop(root)
root.mainloop()		