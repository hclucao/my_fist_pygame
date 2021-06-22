import os

class Diretorio:
	def __init__(self) -> None:
		"""module with way of files
		just that
		"""
		self.diretorioMestre = os.path.dirname(__file__) #definindo os diretorio para que essa script rode em qualquer pc
		self.diretorioIMG = os.path.join(self.diretorioMestre, 'img') # aqui vamos comecar pelo diretorio principal e dps entrar na pasta img
		self.diretorioSound = os.path.join(self.diretorioMestre, 'sound')

	def perso(self) -> str:
		return os.path.join(self.diretorioIMG, 'perso1.png')

	def soundjump(self) -> str:
		return os.path.join(self.diretorioSound, 'swm_jump.wav')