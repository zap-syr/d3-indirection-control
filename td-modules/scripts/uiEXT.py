class uiEXT:
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		self.opUi = op('ui')
		self.opSize = op('buttons/size')
		self.opButtons = op('buttons')
		self.opParameters = op('parameters')
		self.opFiles = op('buttons/template')
		self.opUpdate = op('buttons/count1')
		self.opFolder = op('buttons/folder/folder_dat')
		self.opDrop = op('buttons/drop_text')
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
		self.opFolder.par.refreshpulse.pulse()
		if not self.Get_folder_path():
			self.opDrop.par.fontalpha = 1
		else:
			self.opDrop.par.fontalpha = 0


	# auto fit size buttons height
	def Auto_fit_height(self):
		self.opSize.par.value1 = self.opButtons.par.h / (math.ceil((self.opFiles.numRows - 1) / self.opButtons.par.alignmax)) - self.opButtons.par.spacing


	# auto fit size buttons width
	def Auto_fit_width(self):
		if ((self.opFiles.numRows - 1) > self.ownerComp.par.Buttonsperrow):
			self.opSize.par.value0 = self.opButtons.par.w / self.ownerComp.par.Buttonsperrow - self.opButtons.par.spacing
		else:
			self.opSize.par.value0 = self.opButtons.par.w / (self.opFiles.numRows - 1)- self.opButtons.par.spacing


	# disconnect connection from op
	def Comp_disconnect_connectors(self, op):
		op.inputCOMPConnectors[0].disconnect()


	# connect op to target
	def Comp_connect_connector(self, op, target):
		op.inputCOMPConnectors[0].connect(target)


	# update buttons thnumbnails
	def Update_thumbnails(self):
		self.opUpdate.par.reset.pulse()


	# unpin buttons window
	def Open_window(self):
		opWindow = op('buttons/buttons_window')
		self.Comp_disconnect_connectors(self.opButtons)
		self.Set_width_comp(self.opUi, self.opParameters.par.w)
		self.Set_width_comp(self.opButtons, 1920)
		self.Set_heigth_comp(self.opButtons, 1080)
		opWindow.par.winopen.pulse()

	