import os

class paperParser():

	def __init__(self):
		return None

	def open_file(self, fileName):
		if os.path.exists(fileName):
			with open(fileName,'r') as file:
				try:
					self.paperString = file.read()
				except:
					print("Cannot read file")

	# select document main body: from \bgin{document} to \end{document}
	def select_main_document(self):
		temp = self.paperString.split("begin{document}")
		self.paperString = temp[1]
		temp = self.paperString.split("\end{document} ")
		self.paperString = temp[0]
		#print(self.paperString)

	# eliminate all comments (block comment and line comment)
	def eliminate_comment(self):
		### eliminate block comment: /* */
		paperList = self.paperString.split("/*")
		print(len(paperList))
		for i in range(1,len(paperList)):
			tempString = paperList[i]
			tempList = tempString.split("*/")
			try:
				paperList[i] = tempList[1]
			except:
				print("Error: there is no */ after a /*")
		#sth = "".join(paperList)
		#print(sth)

		### separate by \n + remove duplicates
		paper_list = [temp.split("\n") for temp in paperList]
		self.paperSet = set()
		for i in paper_list:
			[self.paperSet.add(j.strip()) for j in i]
		self.paperSet.remove("")
		#print(len(self.paperSet))

		### eliminate line comment: %
		tempSet = set()
		for paragraph in self.paperSet:
			if (paragraph.startswith("%")):
				tempSet.add(paragraph)
		self.paperSet.difference_update(tempSet)
		#print(len(self.paperSet))


	def parse_paper(self, fileName):
		self.open_file(fileName)
		self.select_main_document()
		self.eliminate_comment()

		# parse all paragraph into sentences
		finalSet = set()
		for i in self.paperSet:
			for j in i.split("."):
				finalSet.add(j)
		print(len(finalSet))
		return finalSet
