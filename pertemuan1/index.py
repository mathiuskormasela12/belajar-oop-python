
# Belajar Membuat Class dan Menginstansiasinya

class Mahasiswa :
	# Membuat Property
	nama = ''
	usia = 0

	# Constructor method seperti di Javascript dan Typescript
	def __init__(self, nama, usia) :
		self.nama = nama
		self.usia = usia

	# Membuat Method
	def jikoshokai(self) :
		print('Hi I am ' + self.nama + ' and I am ' + str(self.usia) + ' years old.')

	# Getter
	# Nama method setter and getter harus sama
	@property
	def setAndGetNama(self) :
		return self.nama
	
	# Setter
	@setAndGetNama.setter 
	def setAndGetNama(self, nama) :
		self.nama = nama


mathius = Mahasiswa('Mathius', 21)
print(mathius.nama)
mathius.jikoshokai()
print('Dari Getter', mathius.setAndGetNama)
mathius.setAndGetNama = 'Arin'
print(mathius.setAndGetNama)