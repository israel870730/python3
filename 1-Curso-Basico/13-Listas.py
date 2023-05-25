**Suma **(+) Concatena dos o más listas:
a=[1,2]
b=[3,4]
a + b --> [1,2,3,4]
**Multiplicación **(*) Repite la misma lista:
a=[1,2]
a * 2 —> [1,2,1,2]
Añadir elemento al final de la lista:
a=[1]
a.append(2)=[1,2]
Eliminar elemento al final de la lista:
a=[1,2]
b=a.pop()
a=[1]
**Eliminar elemento **dado un indice:
a=[1,2]
b=a.pop(1)
a=[2]
Ordenar lista de menor a mayor, esto modifica la lista inicial
a=[3,8,1]
a.sort() —> [1,3,8]
Ordenar lista de menor a mayor, esto NO modifica la lista inicial
a=[3,8,1]
a.sorted() —> [1,3,8]
Eliminar elementos de lista Elimina el elemento de la lista dado su indice
a=[1,2,3]
del a[0] —> a[2,3]
Eliminar elementos de lista Elimina el elemento de la lista dado su valor
a=[0, 2, 4, 6, 8]
a.remove(6)
a=[0, 2, 4, 8]
**Range **creacion de listas en un rango determinado
a=(list(range(0,10,2))) -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a=[0,2,4,6,8]
Tamaño lista len Devuelve el valor del tamaño de la lista:
a=[0,2,4,6,8]
len(a)=5