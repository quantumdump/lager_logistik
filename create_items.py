import sqlite3

conn=sqlite3.connect('warehouse.db')

c = conn.cursor()

# c.execute("""CREATE TABLE items (
# 	item_name text,
# 	item_slot_id integer,
# 	item_weight integer,
# 	item_dimensions text
# 	)""")
# c.execute("""CREATE TABLE slots (
# 	slot_free integer,
# 	shelf_rack_id integer
# 	)""")
# c.execute("""CREATE TABLE shelf_racks (
# 	the_rows integer,
# 	slots_per_rows integer,
# 	slot_dimensions text,
# 	shelf_x1_meters integer,
# 	shelf_y1_meters integer,
# 	shelf_x2_meters integer,
# 	shelf_y2_meters integer
# 	)""")
# c.execute("INSERT INTO shelf_racks VALUES(5, 8, '', 5, 39, 10, 29)")
# c.execute("INSERT INTO shelf_racks VALUES(5, 8, '', 12,39,17,29)")
# c.execute("INSERT INTO shelf_racks VALUES(5, 5, '', 19, 39, 24, 17)")
# c.execute("INSERT INTO shelf_racks VALUES(5, 10, '', 5, 27, 17, 17)")
c.execute("INSERT INTO shelf_racks VALUES(6, 12, '', 5,15,24,15)")
c.execute("SELECT * FROM shelf_racks")
all_racks = c.fetchall()
print(all_racks)
conn.commit()
conn.close()