x = "variable_1"
y = "VARIABLE_2"
#imprimeix literalment variable_1
print(x)

#imprimeix literalment x
print("x")

#imprimeix literalment "x"
print("\"x\"")

#imprimeix literalment x y
print("x " + "y")

#imprimeix x VARIABLE_2
print("x " + y)

#imprimeix literalment x i y i no facis intro
print("x",end="y") 
print("")

#imprimeix x, fes intro i imprimeix y
#imprimeix variable_1 fes intro i imprimeix VARIABLE_2
print("x\ny")

#imprimeix VARIABLE_1
print(x.upper())

#imprimeix variable_2
print(y.lower())

#imprimeix si variable_1 esta escrit en majúscules / dir si VARIABLE_2 esta escrit en minuscules
print(x.isupper())
print(y.islower())

#imprimeix la quantitat de símbols que te variable_1
print(len(x))

#imprimeix el primer símbol de variable_1
print(x[0])

#imprimeix la posició del símbol v en variable_1
print(x.index("v"))

#imprimeix x_1
print(x.replace("variable","x"))
