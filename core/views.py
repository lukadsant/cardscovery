from django.shortcuts import render,redirect
from .models import Pessoa
from googletrans import Translator

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all().order_by('-id')

    return render(request,'newindex.html',{'pessoas':pessoas})




def charlist(request,id):
    pessoa =  Pessoa.objects.get(id=id)

    return render(request,'newcharlist.html',{'pessoa':pessoa})


def addchar(request):
    return render(request,'addchar.html')



def salvar(request):

    import requests

    url = 'https://graphql.anilist.co'

    query = '''
    query ($name: String) {
    Character(search: $name) {
        id
        name {
        full
        }
        image {
        medium
        }
        description
        media(sort: [POPULARITY_DESC], type: ANIME) {
        nodes {
            title {
            romaji
            }
        }
        }
    }
    }
    '''

    variables = {
        'name': request.POST.get("nome")+" "+request.POST.get("sobrenome")
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()

    if 'errors' in data:
        print(data['errors'])
        img='https://cdn.myanimelist.net/images/characters/11/497292.jpg'
        anime_name='???'
        vdesc='sem comentários para esse personagem...'

    else:
        character = data['data']['Character']
        try:
            anime_name = character['media']['nodes'][0]['title']['romaji']
        except:
            anime_name='???'
        print(f"Name: {character['name']['full']}")
        print(f"ID: {character['id']}")
        print(f"Image: {character['image']['medium']}")
        print(f"Description: {character['description']}")
        print(f"Anime: {anime_name}")
        img=character['image']['medium']
        vdesc=character['description']
        print(vdesc)
        translator = Translator()
        try:
            vtdesc=translator.translate(vdesc, dest='pt').text
        except:
            try:
                vtdesc=vdesc
            except:
                vtdesc='sem comentários pra esse personagem...'

    vnome = request.POST.get("nome")
    vsobrenome = request.POST.get("sobrenome")
    Pessoa.objects.create(nome=vnome.title(),sobrenome=vsobrenome.title(),imagem=img,anime=anime_name,desc=vtdesc)
    pessoas = Pessoa.objects.all()


    return redirect(home)


def editar(request,id):
    pessoa =  Pessoa.objects.get(id=id)

    return render(request,'newupdate.html',{'pessoa':pessoa})



def update(request,id):
    vnome = request.POST.get("nome")
    vsobrenome = request.POST.get("sobrenome")
    vanime = request.POST.get("anime")
    vtitulo = request.POST.get("titulo")
    vbio = request.POST.get("bio")
    vdesc = request.POST.get("descricao")
    vlinkimg = request.POST.get("imagem")
    vwallpaper = request.POST.get("wallpaper")
    vpowermove1 = request.POST.get("powermove1")
    vpowermovedesc1 = request.POST.get("powermovedesc1")
    vpowerimg1 = request.POST.get("powerimg1")
    vpowermove2 = request.POST.get("powermove2")
    vpowermovedesc2 = request.POST.get("powermovedesc2")
    vpowerimg2 = request.POST.get("powerimg2")
    vpowermove3 = request.POST.get("powermove3")
    vpowermovedesc3 = request.POST.get("powermovedesc3")
    vpowerimg3 = request.POST.get("powerimg3")

    pessoa =  Pessoa.objects.get(id=id)

    pessoa.nome=vnome
    pessoa.sobrenome=vsobrenome
    pessoa.anime=vanime
    pessoa.desc=vdesc
    pessoa.imagem=vlinkimg
    pessoa.titulo=vtitulo
    pessoa.info=vbio
    pessoa.wallpaper=vwallpaper
    pessoa.powermove1=vpowermove1
    pessoa.powerimg1=vpowerimg1
    pessoa.powermovedesc1=vpowermovedesc1
    pessoa.powermove2=vpowermove2
    pessoa.powerimg2=vpowerimg2
    pessoa.powermovedesc2=vpowermovedesc2
    pessoa.powermove3=vpowermove3
    pessoa.powerimg3=vpowerimg3
    pessoa.powermovedesc3=vpowermovedesc3

    pessoa.save()
    return redirect(home)




def delete(request,id):
    pessoa =  Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)




