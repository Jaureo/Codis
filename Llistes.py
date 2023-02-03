#Una llista pot tenir tots aquests elements:
llista_1 = ["string_1", "string_2", "string_3"]
llista_2 = [1, 2, 3]
llista_3 = [True, False]
llista_4 = ["string", 1, True]

#Es poden afegir altres llistes
llista_1.extend(llista_2)
print(llista_1)
llista = ["string_1", "string_2", "string_3"]
#Es pot afegir un element d'una llista a qualsevol index
llista_1.insert(1, "string_2v2")
print(llista_1)

#Es pot afegir altres index al final
llista_1.append("string_4")
print(llista_1)

#Es pot eliminar tots els elements d'una llista
llista_1.clear()
print(llista_1)
llista_1 = ["string_1", "string_2", "string_3"]

#Es pot eliminar un element de qualsevol posició d'una llista
llista_1.remove("string_3")
print(llista_1)
llista_2 = ["string_1", "string_2", "string_3"]

#Es pot eliminar el darrer element d'una llista
llista_1.pop()
print(llista_1)
llista_1 = ["string_1", "string_2", "string_3"]

#Es pot saber la posició d'un element d'una llista
print(llista_1.index("string_1"))

#Es pot saber quants de pics un valor es repeteix a una llista
print(llista_1.count("string_1"))
