import pymysql as mysql


def sign_in(coach_number, password):
	""" 登录函数 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="xxq")
	cur = conn.cursor()
	sql = f"select * from `教练密码表` where `教练编号` = '{coach_number}' "
	cur.execute(sql)
	list1 = cur.fetchall()
	if password == list1[0][1]:
		return 1
	else:
		return 0


def Attendance(coach_number):
	""" 出勤函数 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="xxq")
	cur = conn.cursor()
	sql = f"UPDATE `教练表` set `状态` = '在岗' where `教练编号` = '{coach_number}' "
	cur.execute(sql)
	conn.commit()


def search_student_information(student_number):
	""" 查找学生信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="xxq")
	cur = conn.cursor()
	sql = f"select * from `学员表` where `学员编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


def print_coach_information(coach_number):
	""" 显示教练信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="xxq")
	cur = conn.cursor()
	sql = f"select `教练姓名`,`电话号码`,`车辆编号`,`状态` from `教练表` where `教练编号` = '{coach_number}' "
	cur.execute(sql)
	return cur.fetchall()


def change_car(coach_number, car_number):
	""" 调车 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="xxq")
	cur = conn.cursor()
	sql1 = f"select `教练姓名`,`教练编号`from `教练表` where `车辆编号` = '{car_number}'"
	cur.execute(sql1)
	last_all = cur.fetchall()[0]
	sql2 = f"select `教练姓名`,`车辆编号` from `教练表` where `教练编号` = '{coach_number}'"
	cur.execute(sql2)
	now_all = cur.fetchall()[0]
	sql3 = f"update `教练表` set `车辆编号` = '{car_number}' where `教练编号` = '{coach_number}'"
	cur.execute(sql3)
	sql4 = f"update `教练表` set `车辆编号` = '{now_all[1]}' where `教练编号` = '{last_all[1]}'"
	cur.execute(sql4)
	sql5 = f"update `车辆表` set `教练姓名` = '{now_all[0]}' where `车辆编号` = '{car_number}'"
	cur.execute(sql5)
	sql6 = f"update `车辆表` set `教练姓名` = '{last_all[0]}' where `车辆编号` = '{now_all[1]}'"
	cur.execute(sql6)
	conn.commit()

