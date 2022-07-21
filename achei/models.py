from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Lugar(models.Model):
	nome = models.CharField(max_length=300)
	descricao = models.TextField()
	autor = models.ForeignKey(get_user_model(), on_delete = models.CASCADE,)

	def __str__(self):
		return self.nome

class Comodo(models.Model):
	lugar = models.ForeignKey(Lugar, on_delete = models.CASCADE,)
	nome = models.CharField(max_length=300)
	descricao = models.TextField()
	autor = models.ForeignKey(get_user_model(), on_delete = models.CASCADE,)
	

	def __str__(self):
		return self.nome

class Compartimento(models.Model):
	comodo = models.ForeignKey(Comodo, on_delete = models.CASCADE,)
	nome = models.CharField(max_length=300)
	descricao = models.TextField()
	autor = models.ForeignKey(get_user_model(), on_delete = models.CASCADE,)
	

	def __str__(self):
		return self.nome

class Objeto(models.Model):
	compartimento = models.ForeignKey(Compartimento, on_delete = models.CASCADE,)
	nome = models.CharField(max_length=300)
	descricao = models.TextField()
	autor = models.ForeignKey(get_user_model(), on_delete = models.CASCADE,)

	def __str__(self):
		return self.nome

class HistoricoTransferencias(models.Model):
	#TENTAR FAZER PELO METODO NORMAL, FOREIGNKEY
	objeto = models.ForeignKey(Objeto, on_delete = models.CASCADE,)
	compartimentoDe = models.ForeignKey(Compartimento, on_delete = models.CASCADE, related_name='compartimentoDe')
	compartimentoPara = models.ForeignKey(Compartimento, on_delete = models.CASCADE, related_name='compartimentoPara')

	#def atribuir(self, o, cd, cp):
		#new_historico = HistoricoTransferencias()
	#	self.objeto = o
	#	self.compartimentoDe = cd
	#	self.compartimentoPara = cp
	#objeto = models.ForeignKey(Objeto, on_delete = models.CASCADE,)
	#compartimentoDe = models.ForeignKey(Compartimento, on_delete = models.CASCADE, related_name='compartimentoDe')
	#compartimentoPara = models.ForeignKey(Compartimento, on_delete = models.CASCADE, related_name='compartimentoPara')

	def __str__(self):
		return f'Objeto {self.objeto.pk} foi de {self.compartimentoDe.pk}  para {self.compartimentoPara.pk}'