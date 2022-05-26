class Mahasiswa :
	@staticmethod
	def show() :
		print('Ini Static Method')
	
	@classmethod
	def show2(cls) :
		# memanggil static method dari class method
		cls.show()
		print('Ini Class Method')



Mahasiswa.show()
Mahasiswa.show2()