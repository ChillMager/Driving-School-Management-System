import pymysql as mysql


def sign_in(coach_number, password):
	""" 登录函数 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="xxq")
	cur = conn.cursor()
	sql = f"select * from `管理员密码表` where `管理员编号` = '{coach_number}' "
	cur.execute(sql)
	list1 = cur.fetchall()
	if password == list1[0][1]:
		return 1
	else:
		return 0


def search_student_information(student_number):
	""" 查找学生信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="xxq")
	cur = conn.cursor()
	sql = f"select * from `学员表` where `学员编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


def search_signin_information(student_number):
	""" 查找签到表信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="xxq")
	cur = conn.cursor()
	sql = f"select * from `签到表` where `学员编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


def search_queue_information(student_number):
	""" 查找队列优先级信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="xxq")
	cur = conn.cursor()
	sql = f"select * from `队列优先级表` where `学员编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


def search_car_information(student_number):
	""" 查找车辆表信息 """
	conn = mysql.connect(host="localhost", user="root", password="123456", db="xxq")
	cur = conn.cursor()
	sql = f"select * from `车辆表` where `车辆编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


def updatesignin(number):
	con = mysql.connect(host="localhost", user="root", password="123456", database="xxq")
	# 创建操作游标

	with con:
		with con.cursor() as cursor:
			sql1 = f"UPDATE `签到表` SET `签到表`.`签到状态` =  '已签到'  WHERE `签到表`.`学员编号` = '{number}'"
			# 执行创建sql语句
			cursor.execute(sql1)
		# 提交数据
		con.commit()


def updatecar(number):
	con = mysql.connect(host="localhost", user="root", password="123456", database="xxq")
	# 创建操作游标

	with con:
		with con.cursor() as cursor:
			sql1 = f"UPDATE `车辆表` SET `车辆表`.`车辆状态` =  '使用'  WHERE `车辆表`.`车辆编号` = '{number}'"
			# 执行创建sql语句
			cursor.execute(sql1)
		# 提交数据
		con.commit()


def updatequeue(number):
	con = mysql.connect(host="localhost", user="root", password="123456", database="xxq")
	# 创建操作游标

	with con:
		with con.cursor() as cursor:
			sql1 = f"UPDATE `队列优先级表` SET `队列优先级表`.`优先级` =  '优先级'  WHERE `队列优先级表`.`学员编号` = '{number}'"
			# 执行创建sql语句
			cursor.execute(sql1)
		# 提交数据
		con.commit()


def updatestudent(number):
	con = mysql.connect(host="localhost", user="root", password="123456", database="xxq")
	# 创建操作游标

	with con:
		with con.cursor() as cursor:
			sql1 = f"UPDATE `学员表` SET `学员表`.`学生状态` =  '已通知'  WHERE `学员表`.`学员编号` = '{number}'"
			# 执行创建sql语句
			cursor.execute(sql1)
		# 提交数据
		con.commit()