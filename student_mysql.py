# 导入模块
import pymysql


def sign_in(student_number, password):
	""" 登录函数 """
	sql = f"select * from `学员密码表` where `学员编号` = '{student_number}'"
	cur.execute(sql)
	list1 = cur.fetchall()
	if password == list1[0][1]:
		return 1
	else:
		return 0


def Register_information():
	# 编写插入数据的sql
	sql = 'insert into student(id_num,name,year,sex) values(%s,%s,%s,%s)'

	try:
		# 执行sql
		id = input('请输入学员身份证号：')
		name = input('请输入学员姓名：')
		year = input('请输入学员年龄：')
		sex = input('请输入学员性别：')
		cur.execute(sql, (id, name, year, sex))
		# 提交事务
		con.commit()
		print('登记成功')
	except Exception as e:
		print(e)
		con.rollback()
		print('信息登记失败')
	finally:
		# 关闭连接
		cur.close()
		con.close()


def Search_Coach(coach_number):
	# 编写查询的sql
	sql = f"select * from `教练表` where `教练编号` = '{coach_number}' "
	cur.execute(sql)
	return cur.fetchall()


def Appointment_Coach(student_number, coach_number):
	# 编写更新数据的sql
	sql = f"UPDATE `预约表` set `教练编号` = '{coach_number}' where `学员编号` = '{student_number}' "
	cur.execute(sql)
	con.commit()


def log_in(student_number):
	# 编写更新数据的sql
	sql = f"UPDATE `签到表` set `签到状态` = 1 where `学员编号` = '{student_number}' "
	cur.execute(sql)
	con.commit()


def Search_Course(program_number):
	# 编写查询的sql
	sql = f"select * from `练习进度表` where `练习项目编号` = '{program_number}' "
	cur.execute(sql)
	return cur.fetchall()


def Search_Test(student_number):
	# 编写查询的sql
	sql = f"select * from `培训表` where `学员编号` = '{student_number}' "
	cur.execute(sql)
	return cur.fetchall()


# 创建数据库本地链接
con = pymysql.connect(host="localhost", user="root", password="123456", database="xxq")
# 创建操作游标对象

cur = con.cursor()
