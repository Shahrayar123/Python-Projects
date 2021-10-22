from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import matplotlib.pyplot as plt
import requests
import bs4
from sqlite3 import *
def _roll_validate():
	a=b=c=0
	if not st_rno.get():
		showerror("Failure","Roll no should not be empty ")
		a = 1
	elif st_rno.get().isalpha():
		showerror("Failure","Only numbers allowed for rollno")
		b = 1
	elif int(st_rno.get()) < 0:
		showerror("Failue","Roll no should be greater than 0")
		c = 1
	if a == 1 	or b == 1 or c == 1:
		return 1
	else:
		return 0	

def _name_validate():
	a=b=c=0
	if not st_nme.get():
		showerror("Failure","Name should not be empty ")
		a = 1
	elif st_nme.get().isdigit():
		showerror("Failure","Only characters allowed for Name")
		b = 1
	elif len(st_nme.get()) < 2:
		showerror("Failue","Length of name should be greater than 1")
		c = 1
	if a == 1 	or b == 1 or c == 1:
		return 1
	else:
		return 0	


def _marks_validate():
	a=b=c=0
	if not st_mks.get():
		showerror("Failure","Marks should not be empty ")
		a = 1
	elif st_mks.get().isalpha():
		showerror("Failure","Only numbers allowed for marks")
		b = 1
	elif int(st_mks.get()) < 0:
		showerror("Failue","Marks should be greater than 0")
		c = 1
	if a == 1 	or b == 1 or c == 1:
		return 1
	else:
		return 0


def loc():
		wa ="https://ipinfo.io/"
		res = requests.get(wa)
		data = res.json()
		location = data['loc']
		return location
location = loc()

def temp():
	city_name = "Airoli"
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city_name
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"		
	wa = a1 + a2 + a3
	res = requests.get(wa)
	data = res.json()
	t = data['main']
	temperature = t['temp']
	return temperature
temperature = temp()

def f1():
	add_window.deiconify()
	main_window.withdraw()

def f2():
	main_window.deiconify()	
	add_window.withdraw()



def f3():
	view_window.deiconify()
	main_window.withdraw()
	view_st_data.delete(1.0, END)
	info = ''
	con = None
	try:
		con = connect("datab.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + "Rno: " + str(d[0]) + "   Name:	" + str(d[1]) + "   Marks:  " + str(d[2]) + "\n"
		view_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("Failure ",e)
	finally:
		if con is not None:
				con.close()
	
def f4():
	main_window.deiconify()	
	view_window.withdraw()

def f5():
	update_window.deiconify()
	main_window.withdraw()

def f6():
	main_window.deiconify()	
	view_window.withdraw()

def f7():
	delete_window.deiconify()
	main_window.withdraw()

def f8():
	main_window.deiconify()	
	delete_window.withdraw()

def f9():
	try:
		con = None
		con = connect('datab.db')
		nme = _name_validate()
		roll = _roll_validate()
		marks = _marks_validate()
		if roll == 0: 
			if nme == 0: 
				if marks == 0:
					rno = int(add_ent_rno.get())
					name = add_ent_name.get()
					marks = int(add_ent_marks.get())
					cursor = con.cursor()
					sql_ = "insert into student values('%d','%s','%d')"
					cursor.execute(sql_ % (rno, name, marks))
					con.commit()
					showinfo('Success','record added')
					add_ent_rno.delete(0,END)
					add_ent_name.delete(0,END)
					add_ent_marks.delete(0,END)
	except Exception as e:
		showerror('Failure',e)
		con.rollback()	
	finally:
		if con is not None:
			con.close()


def f10():
		wa = "https://www.brainyquote.com/quote_of_the_day"
		res = requests.get(wa)
		data = bs4.BeautifulSoup(res.text, 'html.parser')
		info = data.find('img', {'class' : 'p-qotd'})
		msg = info['alt']
		return msg
message = f10()
msg = message.strip()

def f11():
	try:
		con = connect('datab.db')
		cursor = con.cursor()
		nme = _name_validate()
		rll = _roll_validate()
		mks = _marks_validate()
		if rll == 0:
			if nme == 0:
				if mks == 0:
					rno = int(update_ent_rno.get())
					name = update_ent_name.get()
					marks = int(update_ent_marks.get())
					sql_ = "select rno from student"
					cursor.execute(sql_)
					data = cursor.fetchall()
					for d in data:
						if(d[0]==rno):
							cursor = con.cursor()
							cursor.execute("update student set name=(?),marks=(?) where rno=(?)",(name,marks,rno))
							con.commit()
							showinfo('Success','record updated')
							break
					if(d[0]!=rno):
						showerror('Failure','record does not exist')
					update_ent_rno.delete(0,END)
					update_ent_rno.delete(0,END)
					update_ent_rno.delete(0,END)
	except Exception as e:
		showerror('Failure',e)
	finally:
		if con is not None:
			con.close()

def f12():
	con = None
	try: 
		con = connect("datab.db")
		cursor = con.cursor()
		rollno = _roll_validate()
		if rollno == 0:
			rno = int(delete_ent_rno.get())
			sql = "select rno from student"
			cursor.execute(sql)
			data = cursor.fetchall()
			for d in data:
				if(d[0]==rno):
					cursor = con.cursor()
					sql_="delete from student where rno=?"
					cursor.execute(sql_,(rno,))
					con.commit()
					showinfo("Success","Record deleted")
					break
			if(d[0]!=rno):
					showerror("Failure","Invalid roll no")
			if(d[0]==""):
					showerror("Failure","No data")
	except Exception as e:
		showerror("Delete issue",e)
		delete_ent_rno.delete(0,END)
	finally:
		if con is not None:
			con.close()

def f13():	
	try:
		con = connect("datab.db")
		cursor = con.cursor()
		sql = "select name,marks from student order by marks desc"
		cursor.execute(sql)
		data = cursor.fetchall()
		cnames=[x[0] for x in data]
		cmarks=[x[1] for x in data]
		plt.bar(cnames,cmarks,color=('r','g','b','y'))
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.show()
	except Exception as e:
		print("select issue",e)
	finally:
		if con is not None:
			con.close()

# Main window
main_window = Tk()
main_window.geometry("600x600+400+100")
main_window.title("S.M.S")
f = ("Calibri", 20, "bold")
btn_Add = Button(main_window, text="Add", font=f, width=10, command = f1)
btn_View = Button(main_window, text="View", font=f, width=10, command = f3)
btn_Update = Button(main_window, text="Update", font=f, width=10,command = f5)
btn_Delete = Button(main_window, text="Delete", font=f, width=10,command = f7)
btn_Charts = Button(main_window, text="Charts", font=f, width=10,command= f13)
lbl_Location = Label(main_window, text = "Location: ",font=f)
lbl_Location_value = Label(main_window, text =location,font=f)
lbl_Temperature = Label(main_window, text="Temperature: ",font=f)
lbl_Temperature_value = Label(main_window, text=temperature,font=f)
lbl_qotd = Label(main_window, text = "QOTD: ",font =f)
lbl_qotd_txt = Message(main_window, text=msg,font=f, width= 480 )
btn_Add.pack(pady=10)
btn_View.pack(pady=10)
btn_Update.pack(pady=10)
btn_Delete.pack(pady=10)
btn_Charts.pack(pady=10)
lbl_Location.place(x = 5, y=500, anchor ='sw')
lbl_Temperature.place(x = 350, y=500, anchor ='sw')
lbl_Location_value.place(x = 111, y=500, anchor ='sw')
lbl_Temperature_value.place(x =510 , y=500, anchor='sw')
lbl_qotd.place(x=5,y=540, anchor='sw')
lbl_qotd_txt.place(x=81,y=578, anchor='sw')


# Add window
st_rno = StringVar()
st_nme = StringVar()
st_mks = StringVar()
add_window = Toplevel(main_window)
add_window.title("Add St.")
add_window.geometry("600x600+400+100")
add_lbl_rno = Label(add_window, text="Enter roll no", font=f)
add_ent_rno = Entry(add_window, bd=5, font=f,textvariable=st_rno)
add_lbl_name = Label(add_window, text="Enter name", font=f)
add_ent_name = Entry(add_window, bd=5, font=f,textvariable=st_nme)
add_lbl_marks = Label(add_window, text="Enter marks", font=f)
add_ent_marks = Entry(add_window, bd=5, font=f,textvariable=st_mks)
add_btn_save = Button(add_window, text="Save",width=10,font = f,command=f9)
add_btn_back = Button(add_window, text="Back",width=10,font = f,command=f2)
add_lbl_rno.pack(pady=10)
add_ent_rno.pack(pady=10)
add_lbl_name.pack(pady=10)
add_ent_name.pack(pady=10)
add_lbl_marks.pack(pady=10)
add_ent_marks.pack(pady=10)
add_btn_save.pack(pady=10)
add_btn_back.pack(pady=10)
add_window.withdraw()


# View window
view_window = Toplevel(main_window)
view_window.title("View St.")
view_window.geometry("600x600+400+100")
view_st_data = ScrolledText(view_window, width = 30 , height =10 ,font = f)
view_btn_back = Button(view_window, text="Back",width=10,font = f,command = f4)
view_st_data.pack(pady=10)
view_btn_back.pack(pady=10)
view_window.withdraw()


# Update window
update_window = Toplevel(main_window)
update_window.title("Update St.")
update_window.geometry("600x600+400+100")
update_lbl_rno = Label(update_window, text="Enter roll no", font=f)
update_ent_rno = Entry(update_window, bd=5, font=f, textvariable=st_rno)
update_lbl_name = Label(update_window, text="Enter name", font=f)
update_ent_name = Entry(update_window, bd=5, font=f, textvariable=st_nme)
update_lbl_marks = Label(update_window, text="Enter marks", font=f)
update_ent_marks = Entry(update_window, bd=5, font=f, textvariable=st_mks)
update_btn_save = Button(update_window, text="Save",width=10,font = f,command=f11)
update_btn_back = Button(update_window, text="Back",width=10,font = f,command=f6)
update_lbl_rno.pack(pady=10)
update_ent_rno.pack(pady=10)
update_lbl_name.pack(pady=10)
update_ent_name.pack(pady=10)
update_lbl_marks.pack(pady=10)
update_ent_marks.pack(pady=10)
update_btn_save.pack(pady=10)
update_btn_back.pack(pady=10)
update_window.withdraw()


# Delete window
delete_window = Toplevel(main_window)
delete_window.title("Delete St.")
delete_window.geometry("600x600+400+100")
delete_lbl_rno = Label(delete_window, text = "Enter roll no ",font = f)
delete_ent_rno = Entry(delete_window, bd = 5 , font = f,textvariable=st_rno)
delete_btn_delete = Button(delete_window, text="Delete",width=10,font = f, command = f12 )
delete_btn_back = Button(delete_window, text="Back",width=10,font = f,command = f8)
delete_lbl_rno.pack(pady=10)
delete_ent_rno.pack(pady=10)
delete_btn_delete.pack(pady=10)
delete_btn_back.pack(pady=10)
delete_window.withdraw()






main_window.mainloop()