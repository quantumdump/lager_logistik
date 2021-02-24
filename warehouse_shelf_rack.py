import sqlite3

conn=sqlite3.connect('warehouse.db')

c = conn.cursor()

class WarehouseShelfRack():
	"""WarehouseShelfRack class
	Lagerregal class
	"""
	def __init__(self, id, canvas):
		super(General, self).__init__()
		self.id = id
		self.canvas = canvas
		c.execute("SELECT * FROM shelf_racks WHERE id="+self.id)
		the_rack = c.fetchone()
		print(the_rack)
		conn.commit()
		conn.close()
		self.x1meters =''
		self.y1meters =''
		self.x2meters =''
		self.y2meters =''
		

		