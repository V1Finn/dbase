from django.db import models

class dbase(models.Model):
	id_id = models.CharField(max_length=3, primary_key=True, verbose_name='Код')
	text = models.TextField(max_length=1000, verbose_name='Текст')
	data = models.DateTimeField(auto_now=True, verbose_name='Дата, время')

	def __str__(self):
		return '{} / {}'.format(self.id_id, self.data)

	class Meta:
		verbose_name="Таблица"
		verbose_name_plural='Таблицы'
		

