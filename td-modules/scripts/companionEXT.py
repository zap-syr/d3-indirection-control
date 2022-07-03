import random as rnd

class companionEXT:
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.buttonStyle = {'"style"' : '"png"',
							 '"text"' : '',
							 '"size"' : '',
							 '"alignment"' : '',
							 '"pngalignment"' : '',
							 '"color"' : '',
							 '"bgcolor"' : '',
							 '"latch"' : 'false',
							 '"relative_delay"' : 'false'
		}

		self.buttonAction = {'"id"' : '',
							  '"label"' : '"X3NQabG0z:send_string"',
							  '"instance"' : '"X3NQabG0z"',
							  '"action"' : '"send_string"',
							  '"options"' : {'"path"' : '',
							 			'"string"' : ''}
		}
		

	# add commas to text
	def add_commas(self, text):
		text = f'\"{text}\"'
		return text


	# generate random ID
	def Get_id(self):
		rnd_id = ''
		for i in range(9):
			x = rnd.randint(0,2)
			if x == 0:
				rnd_id += chr(rnd.randint(65,90))
			elif x == 1:
				rnd_id += chr(rnd.randint(97, 122))
			else:
				rnd_id += chr(rnd.randint(48, 57))

		rnd_id = self.add_commas(rnd_id)
		return rnd_id


	# get buttons style dictionary
	def Get_button_style(self):
		return self.buttonStyle

	
	# get buttons action dictionary
	def Get_buttons_action(self):
		return self.buttonAction


	# save config to file
	def Save_config(self):
		path = ui.chooseFile(load=False, fileTypes=['companionconfig'], title='Save config')
		if (path):
			op('export').save(path)
		return

		