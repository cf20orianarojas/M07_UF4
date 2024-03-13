from django.shortcuts import render

alumnes = [
        {'id':'1','nom':'Angelo', 'cognom1':'Montenegro', 'cognom2':'Zavala', 'correu':'2023_angelo.montenegro@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'2','nom':'Adria', 'cognom1':'Garcia', 'cognom2':'Perez', 'correu':'2023_adria.garcia@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'3','nom':'Alexander', 'cognom1':'Andreev', 'cognom2':'Apukhtina', 'correu':'2023_alexander.andreev@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'4','nom':'Angel', 'cognom1':'Ivanov', 'cognom2':'Spasov', 'correu':'2023_angel.ivanov@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7'},
        {'id':'5','nom':'Anxo', 'cognom1':'Aragundi', 'cognom2':'Mesias', 'correu':'2023_anxo.aragundi@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'6','nom':'Carlos Andres', 'cognom1':'Zambrano', 'cognom2':'Aray', 'correu':'2023_carlos.zambrano@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'7','nom':'Dinar', 'cognom1':'Khazimullin', 'cognom2':'', 'correu':'2023_dinar.khazimullin@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'8','nom':'Eric', 'cognom1':'Sanchez', 'cognom2':'Vazquez', 'correu':'2023_eric.sanchez@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'9','nom':'Facundo Calixto', 'cognom1':'Barrios', 'cognom2': '', 'correu':'2023_facundo.barrios@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'10','nom':'Gemma', 'cognom1':'Garrigosa', 'cognom2':'Frances', 'correu':'2023_gemma.garrigosa@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'11','nom':'Joana Jiayun', 'cognom1':'Lin', 'cognom2':'Chen', 'correu':'2023_joana.lin@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'12','nom':'Joel', 'cognom1':'Ghanem', 'cognom2':'Gomez', 'correu':'2023_joel.ghanem@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'13','nom':'Junhong', 'cognom1':'Zhu', 'cognom2':'Zhang', 'correu':'2023_junhong.zhu@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'14','nom':'Jianjing', 'cognom1':'Niu', 'cognom2':'', 'correu':'2023_jianjing.niu@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M7, M8, M9'},
        {'id':'15','nom':'Jesus', 'cognom1':'Pujada', 'cognom2':'Montoya', 'correu':'2023_jesus.pujada@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'16','nom':'Neus', 'cognom1':'Bravo', 'cognom2':'Areas', 'correu':'2023_neus.bravo@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'17','nom':'Oriana Saray', 'cognom1':'Rojas', 'cognom2':'Guedez', 'correu':'2023_oriana.rojas@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'18','nom':'Oscar ', 'cognom1':'Perez', 'cognom2': 'Mengual', 'correu':'2023_oscar.perez@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'},
        {'id':'19','nom':'Veronica', 'cognom1':'Cartagena', 'cognom2':'Jaldin', 'correu':'2023_veronica.cartagena@iticbcn.cat', 'curs':'DAW2A', 'moduls':'M6, M7, M8, M13, M9'}
]

teachers = [
    {'id': '1', 'nom': 'Juan Manuel', 'cognom1': 'Sánchez', 'cognom2': 'Bel', 'correu': 'juanmanuel.sanchez@iticbcn.cat',
     'curs': 'DAW2A', 'tutor': 'Si', 'moduls': 'M6'},
    {'id': '2', 'nom': 'Roger', 'cognom1': 'Sobrino', 'cognom2': 'Gil', 'correu': 'roger.sobrino@iticbcn.cat',
     'curs': 'DAW2A', 'tutor': '', 'moduls': 'M7'},
    {'id': '3', 'nom': 'Xavi', 'cognom1': 'Quesada', 'cognom2': 'Puertas', 'correu': 'xavi.quesada@iticbcn.cat',
     'curs': 'DAW2A', 'tutor': '', 'moduls': 'M8/M13'},
    {'id': '4', 'nom': 'Josep Oriol', 'cognom1': 'Roca', 'cognom2': 'Fabra', 'correu': 'joseporiol.roca@iticbcn.cat',
     'curs': 'DAW2A', 'tutor': '', 'moduls': 'M9'}
]

# index
def index(request):
    return render(request, 'index_centre.html')

# Funció que retornà el template students.html i les dades dels alumnes
def students(request):
    return render(request, 'students.html', { 'students':alumnes })

# Funció que retornà el template teachers.html les dades dels professors
def teachers(request):
    return render(request, 'teachers.html', { 'teachers': teachers })

def info(request, pk):
    infoObj = none
    for i in infoObj