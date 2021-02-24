import ctypes
import subprocess
import os
print(os.name)

				
class General():
	"""General information about the company
	General Informazion über der Firma"""
	canvas_width = 500
	canvas_height = 500
	@staticmethod
	#Get screen resolution in linux
	def get_screen_resolution_linux():
			output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
			resolution = output.split()[0].split(b'x')
			return {'width': resolution[0].decode('utf-8'), 'height': resolution[1].decode('utf-8')}
	@staticmethod
	#Get screen resolution in Windows
	def get_screen_resolution_windows():
			#Get screen size
			user32 = ctypes.windll.user32
			screensize = {'width': user32.GetSystemMetrics(0), 'height': user32.GetSystemMetrics(1)}
			return screensize
	@staticmethod
	#Convert meters to pixels
	def meters_to_pixels(meters_to_convert, total_meters_width, new_canvas_width):
			meters_per_pixel=total_meters_width/new_canvas_width
			return round(meters_per_pixel*new_canvas_width) 
		
	def __init__(self, company_name, company_foundation_year, company_logo_path):
		super(General, self).__init__()
		
		self.company_name = company_name
		self.company_foundation_year = company_foundation_year
		self.company_logo_path = company_logo_path
	@classmethod
	#Set canvas size. Returns list of canvas_width and canvas_height in pixels
	def set_canvas_size(cls, storage_area_width_meters, storage_area_height_meters):
			scr_res = False
			if os.name=="nt":
					#Get resolution in windows
					scr_res = cls.get_screen_resolution_windows()
			elif os.name=="posix":
					#Get resolution in Linux
					scr_res = cls.get_screen_resolution_linux()
			#If screen resolution is available
			if scr_res:
					coef = int(scr_res['height'])/int(scr_res['width'])
					width_pixels=cls.meters_to_pixels(storage_area_width_meters, int(scr_res['width']), 1000)
					print(width_pixels)
					new_canvas_width = coef*width_pixels
					height_pixels=cls.meters_to_pixels(storage_area_height_meters, int(scr_res['height']), int(scr_res['height']))
					new_canvas_height = coef*height_pixels
					return [round(new_canvas_width), round(new_canvas_height)]
			return False
					
					
			
		# cls.canvas_width = canvas_width
		# print(cls.canvas_width)
		# cls.canvas_height = canvas_height
		# print(cls.canvas_height)
		# 
new_company = General("SEP logistik AG", "1980","logo.png")
print(General.set_canvas_size(32, 29))
		
		