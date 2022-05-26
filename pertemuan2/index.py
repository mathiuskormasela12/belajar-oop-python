# Inheritance

class OrangTua :
	
	# Membuat private property
	__iniPrivateProperty = 'Ini Private Property'

	def __init__(self, nama, usia) :
		self.nama = nama;
		self.usia = usia

	def show(self) :
		print('Hello Dari Parent Class')
	

	def tampilkanPrivateProperty(self) :
		return self.__iniPrivateProperty


class Anak(OrangTua) :
	def __init__(self, nama, usia, tinggiBadan) :
		# memanggit contructor function parent class (Cara Pertama)
		# OrangTua.__init__(self, nama, usia)

		# memanggit contructor function parent class (Cara Kedua)
		super().__init__(nama, usia)
		self.tinggiBadan = tinggiBadan

	def show(self) :
		# Overide Method dari parent class
		super().show()
		print('Hello Dari Child Class')


test = Anak('Mathius', 20, 167)
test.show()
print(test.tampilkanPrivateProperty())