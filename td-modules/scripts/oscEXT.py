class oscEXT:
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.osc = op('osc_out')

	def set_osc_parameters(self):
		self.osc.par.active = op.Ui.Get_active()
		self.osc.par.address = op.Ui.Get_osc_address()
		self.osc.par.port = op.Ui.Get_osc_port()
		self.osc.par.localaddress = op.Ui.Get_local_address()
		return
		
	def Set_active(self, val):
		self.osc.par.active = val


	def Set_send_ip(self, val):
		self.osc.par.address = val


	def Set_port(self, val):
		self.osc.par.port = val


	def Set_localaddress(self, val):
		self.osc.par.localaddress = val


	def Send_osc(self, path, command):
		# self.set_osc_parameters()
		self.osc.sendOSC(path, command)
		print(f'osc command was send {path} {command[0]}')
		return