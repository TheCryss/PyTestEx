import pytest
from calc import *


#Prueba unitaria
@pytest.mark.skip(reason="Porque si")
def test_add():
    assert add(2,2) == 4 

#Prueba en serie

@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [
        (2,1,3),
        (3,-2,1),
        (add(3,1),4,9), #falla a proposito
        (10,2,12)
        ]
)
#con el comando $ pytest -v podemos ver el estado de ejecucion de las pruebas
def test_add_multi(input_a,input_b,expected):
    assert add(input_a,input_b) == expected


#Si lo ejecutamos con $ pytest -v -k "substraction" filtramos todos los test cuyo nombre contenga substraction
#Tambien podemos aplicar or y and $ pytest -v -k "substraction or multi" || $ pytest -v -k "add and multi"
def test_substraction():
    assert substraction(2,2) == 0  

#Tambien se pueden filtrar mediante decoradores
#$ pytest -v -m number

@pytest.mark.number
@pytest.mark.parametrize(
        "input_a,input_b,expected",
        [
            (2,0,1),
            (2,1,2),
            (2,2,4),
            (2,3,8)
        ]
)
def test_power_multi(input_a,input_b,expected):
    assert power(input_a,input_b) == expected

@pytest.mark.number
def test_substraction_mark():
    assert substraction(2,2) == 0  

#Con el parametro -x cuando ocurra un error los test faltantes seran detenidos
#$ pytest -v -x

#Con el parametro --tb=no no se muestra el stack trace del error
#$ pytest -v --tb=no

#Mediante el parametro --maxfail=2 paramos la ejecucion del los test cuando 2 fallan
#$ pytest -v --maxfail=2

def test_scott_data():
    db = StudentDB ()
    db.connect('data.json')
    scott_data = db.get_data('Scott')
    assert scott_data['id']==1
    assert scott_data['name']=='Scott'
    assert scott_data['result']=='pass'

def test_mark_data():
    db =StudentDB()
    db.connect('data.json')
    scott_data = db.get_data('Mark')
    assert scott_data['id']==2
    assert scott_data['name']=='Mark'
    assert scott_data['result']=='fail'
