# Variables del personaje RPG 

nombre = 'Aragorn' 
nivel = 1
vida = 100.0 
vida_maxima = 100.0 
esta_vivo = True 
clase = 'Guerrero' 
puntos_ataque = 15 
puntos_defensa = 10 

aragorn = [nombre, nivel, vida, vida_maxima, esta_vivo, clase, puntos_ataque, puntos_defensa]
 

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

# refactorizando el personaje

gandalf = {
    'nombre': 'Gandalf',
    'nivel': 6,
    'vida': 50,
    'mana': 120,
    'ataque': 15
}


dano = float(ataque) * 1.5  # cast 

msg = 'Dano: ' + str(dano)  # explicito 



# f-strings (muy utiles) 

vida = 87.5 

print(f'Vida: {vida:.1f}%') 
print(f'Mana: {mana:.1f}%')
print(f'Nombre: {nombre}')
print(f'Nivel: {nivel:.1f}')

vida = 25.0 

vida_max = 100.0 

 

pct = (vida / vida_max) * 100 

 

if pct <= 0: 

    estado = 'MUERTO' 

elif pct <= 25: 

    estado = 'CRITICO' 

elif pct <= 50: 

    estado = 'HERIDO' 

elif pct <= 75: 

    estado = 'ESTABLE' 

else: 

    estado = 'SALUDABLE' 

 

print(f'Vida: {vida:.0f}/{vida_max:.0f} ({pct:.0f}%)') 

print(f'Estado: {estado}') 

clase = 'Mago' 

nivel_habilidad = 3 

 

# match (Python 3.10+) 

match clase: 

    case 'Guerrero': tipo_ataque = 'Espada' 

    case 'Mago':     tipo_ataque = 'Hechizo' 

    case 'Arquero':  tipo_ataque = 'Flecha' 

    case _:          tipo_ataque = 'Puno' 

 

# Condicion compuesta 

puede_usar_magia = ( 

    clase == 'Mago' and nivel_habilidad >= 3 

) 

 

if puede_usar_magia: 

    print('Bola de fuego!') 

else: 

    print(f'{tipo_ataque} basico')


def estado_personaje(nombre, nivel, vida, mana):
    vivo ='vivo' if  vida > 0 else 'muerto'
    return f'{nombre} (Nv.{nivel}) - Vida: {vida:.1f}%, Mana: {mana:.1f}% - Vivo:{vivo}'



""" 
    #vida_enemigo = 40, ataque = 35, 

bonificacion = 10 (si el jugador tiene nivel >= 5, sino 0), 
nivel_jugador = 6: 
 1. Calcule el dano total = ataque + bonificacion 
  2. Calcule vida_restante = vida_enemigo - dano_total 
  3. Si vida_restante <= 0: imprima 'Enemigo derrotado! +50 XP' 
     Si vida_restante <= 20: imprima 'Enemigo en estado critico' 
     Si no: imprima 'Enemigo resiste. Vida restante: [valor]'  """

print('Nivel gandalf: ' +  str( gandalf['nivel'])     )

#commit 2 
enemigo = {'vida': 40, 'ataque': 35, 'bonificacion':10 if gandalf['nivel'] >= 5 else 0}
while (enemigo['vida'] >= 0):
    enemigo['vida'] = enemigo['vida'] - gandalf['ataque']
    if(enemigo['vida']<=0):
        print(f'Enemigo derrotado! +50 XP. Vida restante: {enemigo["vida"]}')
    elif (enemigo['vida']<=20):
        print(f'Enemigo en estado critico. Vida restante: {enemigo["vida"]}')
    else:
        print(f'Enemigo resiste. Vida restante: {enemigo["vida"]}')

