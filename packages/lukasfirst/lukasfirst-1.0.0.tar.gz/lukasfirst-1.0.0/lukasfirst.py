
#lista = ['Kamil', 'Ziomek', 'Bartek', 'Anna', 'Paulina', 'Gosia', ['Pies', 'Kot', 'Kogut', ['Tulipan', 'Roza', 'Mak']]]

'''for x in lista:
    if isinstance(x, list):
        for nested_x in x:
            if isinstance(nested_x, list):
                for nested_nested_x in nested_x:
                    if isinstance(nested_nested_x, list):
                        print(nested_nested_x)
                    else:
                        print(nested_nested_x)
            else:
                print(nested_x)
    else:
        print(x)'''

def lista_funkcja(lista):
#function below is doing exactly the same as a code above
    for each_item in lista:
        if isinstance(each_item, list):
            lista_funkcja(each_item)
        else:
            print(each_item)

#print(lista_funkcja(lista))
#lista2=['Polska', 'Niemcy', 'Niderlandy',['Kenya', 'Senegal', 'Egipt', ['Japonia', 'Tajlandia', 'Chiny']]]

#print(lista_funkcja(lista2))
