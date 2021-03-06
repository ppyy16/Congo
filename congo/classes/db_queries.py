import MySQLdb
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import random
from classes import *

def get_connection():
	return MySQLdb.connect(host='54.157.229.227',user= 'root',password='databaes',port=3306, database = 'congo')

def list_merch():
	db = get_connection() #MYSQLdb.connect(host='54.157.229.227', user='root', password='databaes', port=3306, database='congo')
	cur = db.cursor()
	sql = "select * from MERCHANDISE LIMIT 5"
	cur.execute(sql)
	merch = []
	for row in cur.fetchall():
		merch.append(Merch(row[1], row[2], row[3], row[4], row[5]))
	db.close()
	return merch
	# Load the html for merch
	template = 'homepage.html'
	return render(request, template, {"merch": merch})

'''
	{% for landloard in data%}
	{{landloard.office_addr}}
	{%endfor%}
'''


def create_merch(request, name, price, desc, rating, url):
	db = get_connection() #MYSQLdb.connect(host='54.157.229.227', user='root', password='databaes', port=3306, database='congo')
	cur = db.cursor()
	rand_id = random.randint(1000,60000)
	sql = "insert into merchandise values("+rand_id+", '"+name+"', "+price+", '"+desc+ "', "+rating + ", '"+ url + ")"
	cur.execute(sql)
	db.commit()
	db.close()
	return redirect('home')

def edit_merch(request, m_id, name, price, desc, rating, url):
	db = get_connection()
	cur = db.cursor()
	sql = "update merchandise set m_name='"+name+"', m_price="+price+", m_desc='"+desc+ "', m_rating= "+rating + ", merchandise_image='"+ url + "' where merchandise_id=" + m_id
	cur.execute(sql)
	db.commit()
	db.close()
	return redirect('home')

def delete_merch(request, merch_id):
	db = get_connection()
	cur = db.cursor()
	sql = "delete from merchandise where merchandise_id=" + merch_id
	cur.execute(sql)
	db.commit()
	db.close()
	return redirect('home')


class Merch:
	def __init__(self, name, price, desc, num_avail, img):
		self.name = name
		self.price=price
		self.image=img
		self.num_avail = num_avail
		self.desc = desc


class Merchant:
	def __init__(self, m_id, name, rating):
		self.name = name
		self.m_id = m_id
		self.rating = rating

class Creditcard:
	def __init__(self, cc_number, cc_name, cc_expDate, cc_secCode):
		self.cc_number = cc_number
		self.cc_name = cc_name
		self.cc_expDate = cc_expDate
		self.cc_secCode = cc_secCode

class Customer:
	def __init__(self, name, dob, addr, cc_number):
		self.name = name
		self.dob = dob
		self.addr = addr
		self.cc_number = cc_number

class Orders:
	def __init__(self, name, dob, addr, cc_number):
		self.name = name
		self.dob = dob
		self.addr = addr
		self.cc_number = cc_number

class Reviews:
	def __init__(self, id, data, ts, rating, merch_id):
		self.id = id
		self.data = data
		self.ts = ts
		self.rating = rating
		self.merch_id = merch_id

class Sells:
	def __init__(self, id, merch_id, m):
		self.id = id
		self.merch_id = merch_id
		self.m = m
