from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100,default='')
    imagem = models.CharField(max_length=255,default='https://cdn.myanimelist.net/images/characters/11/497292.jpg')
    anime = models.CharField(max_length=255,default='???')
    desc = models.TextField(default='')
    titulo = models.CharField(max_length=255,default='Featured')
    info = models.TextField(default='Esse é um personagem ainda não tem uma descrição legal, mete um edit ai comparsa.')
    wallpaper = models.TextField(default='https://e1.pxfuel.com/desktop-wallpaper/208/877/desktop-wallpaper-shounen-manga-panel-anime-all-manga.jpg')
    powermove1= models.CharField(max_length=255,default='Respirar')
    powermove2= models.CharField(max_length=255,default='Gritar')
    powermove3= models.CharField(max_length=255,default='Fugir')
    powermovedesc1=models.TextField(default='Eu não sei o que ele vai fazer com tanto O², mais ele é capaz de fazer isso...')
    powermovedesc2=models.TextField(default='Isso ou pode assustar ou pode transformar a pessoa em um novo astro do POP...')
    powermovedesc3=models.TextField(default='Habilidade Suprema caso o personagem saiba que tem uma promoção no mercado...')
    powerimg1=models.TextField(default='https://i.gifer.com/3tW3.gif')
    powerimg2=models.TextField(default='https://media.tenor.com/ZTU55HQaVWIAAAAd/one-punch-man-opm.gif')
    powerimg3=models.TextField(default='https://i.pinimg.com/originals/88/13/63/8813632e9591a260e59a195bd5b6c7d3.gif')

    def __str__(self):
        return self.nome +" "+ self.sobrenome 