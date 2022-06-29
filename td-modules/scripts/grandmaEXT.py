import xml.etree.ElementTree as ET

class grandmaEXT:
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.blank = op('XML_blank').text
		self.names = op('names')
		self.tree = ET.ElementTree(ET.fromstring(self.blank))
		# self.Save_xml()
		# self.export = op('XML_export')

	def Make_xml(self):
		self.tree = ET.ElementTree(ET.fromstring(self.blank))	
		xmlroot = self.tree.getroot()
		i = 0
		for row in self.names.col('name'):
			if row != 'name':
				macro = xmlroot.find('Macro')
				macroline = ET.SubElement(macro, 'Macroline')
				text = ET.SubElement(macroline, 'text')
				text.text = f'Attribute "VIDEO BANK" At {op.Ui.Get_video_bank()}'
				macroline = ET.SubElement(macro, 'Macroline')
				text = ET.SubElement(macroline, 'text')
				text.text = f'Attribute "VIDEO SLOT" At {i}'
				macroline = ET.SubElement(macro, 'Macroline')
				text = ET.SubElement(macroline, 'text')
				text.text = f'Store Preset 11.{i + 1} /g /o'
				macroline = ET.SubElement(macro, 'Macroline')
				text = ET.SubElement(macroline, 'text')
				text.text = f'Label Preset 11.{i + 1} "{row}"'
				i += 1
		# ET.dump(xmlroot)
		return

	def Save_xml(self):
		self.Make_xml()
		path = ui.chooseFile(load=False, fileTypes=['xml'], title='Save macro')
		if (path):
			self.tree.write(path)
		return