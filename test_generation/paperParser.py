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
		# block comment: /* */
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
		self.paper_list = [temp.split("\n") for temp in paperList]
		print(len(self.paper_list))




	def parse_paper(self, fileName):
		self.open_file(fileName)
		self.select_main_document()
		self.eliminate_comment()

		


if __name__ == '__main__':
	pp = paperParser();
	pp.parse_paper("../data/example_paper.tex")





