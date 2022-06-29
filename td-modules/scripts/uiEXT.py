class uiEXT:
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		self.op_ui = op('ui')
		self.op_size = op('buttons/size')
		self.op_buttons = op('buttons')
		self.op_parameters = op('parameters')
		self.op_files = op('buttons/template')
		self.op_update = op('buttons/count1')
		self.op_folder = op('buttons/folder/folder_dat')
		self.op_drop = op('buttons/drop_text')
		return


	# get active value
	def Get_active(self):
		return self.ownerComp.par.Active


	# get osc address to send	
	def Get_osc_address(self):
		return self.ownerComp.par.Ipaddresstosend


	# get osc port value
	def Get_osc_port(self):
		return self.ownerComp.par.Oscport

	
	# get local address value
	def Get_local_address(self):
		return self.ownerComp.par.Localip


	# get osc path value
	def Get_osc_path(self):
		return self.ownerComp.par.Oscpath


	# get folder path
	def Get_folder_path(self):
		return self.ownerComp.par.Folder


	# auto fit size buttons height
	def Auto_fit_height(self):
		self.op_size.par.value1 = self.op_buttons.par.h / (math.ceil((self.op_files.numRows - 1) / self.op_buttons.par.alignmax)) - self.op_buttons.par.spacing


	# auto fit size buttons width
	def Auto_fit_width(self):
		if ((self.op_files.numRows - 1) > self.ownerComp.par.Buttonsperrow):
			self.op_size.par.value0 = self.op_buttons.par.w / self.ownerComp.par.Buttonsperrow - self.op_buttons.par.spacing
		else:
			self.op_size.par.value0 = self.op_buttons.par.w / (self.op_files.numRows - 1)- self.op_buttons.par.spacing


	# disconnect connection from op
	def Comp_disconnect_connectors(self, op):
		op.inputCOMPConnectors[0].disconnect()


	# connect op to target
	def Comp_connect_connector(self, op, target):
		op.inputCOMPConnectors[0].connect(target)


	# get width of op
	def Get_width_comp(self, op):
		return op.par.w


	# set width of op
	def Set_width_comp(self, op, w):
		op.par.w = w


	# set heigth of op
	def Set_heigth_comp(self, op, h):
		op.par.h = h


	# get text color 
	def Get_text_color(self):
		text_color = (self.ownerComp.par.Textcolorr * 255) * 256 * 256 + (self.ownerComp.par.Textcolorg * 255) * 256 + (self.ownerComp.par.Textcolorb * 255)
		return text_color


	# get bg color
	def Get_bg_color(self):
		bg_color = (self.ownerComp.par.Backgroundcolorr * 255) * 256 * 256 + (self.ownerComp.par.Backgroundcolorg * 255) * 256 + (self.ownerComp.par.Backgroundcolorb * 255)
		return bg_color


	# get text align
	def Get_text_align(self):
		return self.ownerComp.par.Textalignment


	# get text size
	def Get_size_text(self):
		return self.ownerComp.par.Textsize


	#get video bank
	def Get_video_bank(self):
		return self.ownerComp.par.Videobank


	def Get_subfolders_state(self):
		return self.ownerComp.par.Includesubfolders


	def Set_folder_path(self, in_path):
		self.ownerComp.par.Folder = in_path


	def Update_folder(self):
		self.op_folder.par.refreshpulse.pulse()
		if not self.Get_folder_path():
			self.op_drop.par.fontalpha = 1
		else:
			self.op_drop.par.fontalpha = 0


	def Update_thumbnails(self):
		self.op_update.par.reset.pulse()


	# unpin buttons window
	def Open_window(self):
		op_window = op('buttons/buttons_window')
		self.Comp_disconnect_connectors(self.op_buttons)
		self.Set_width_comp(self.op_ui, self.op_parameters.par.w)
		self.Set_width_comp(self.op_buttons, 1920)
		self.Set_heigth_comp(self.op_buttons, 1080)
		op_window.par.winopen.pulse()

	