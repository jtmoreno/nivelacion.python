# Variables del personaje RPG 

nombre = 'Aragorn' 

nivel = 1

vida = 100.0 

vida_maxima = 100.0 

esta_vivo = True 

clase = 'Guerrero' 

puntos_ataque = 15 

puntos_defensa = 10 

 

# Verificar tipos 

print(type(nombre))   # <class 'str'> 

print(type(nivel))    # <class 'int'> 

print(type(vida))     # <class 'float'> 

print(type(esta_vivo)) # <class 'bool'> 

 

print(f'{nombre} (Nv.{nivel}) - Vida: {vida}') 
# Conversiones de tipo 

ataque = 15 
mana = 120
nombre = 'Gandalf'
vida = 5
nivel=4

dano = float(ataque) * 1.5  # cast 

msg = 'Dano: ' + str(dano)  # explicito 



# f-strings (muy utiles) 

vida = 87.5 

print(f'Vida: {vida:.1f}%') 
print(f'Mana: {mana:.1f}%')
print(f'Nombre: {nombre}')
print(f'Nivel: {nivel:.1f}')
