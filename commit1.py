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


inventario = [ 

    'Espada de hierro', 

    'Pocion de vida', 

    'Escudo de madera', 

    'Llave dorada' 

] 

 

print('=== INVENTARIO ===') 

# Con indice 

for i, item in enumerate(inventario, 1): 

    print(f'{i}. {item}') 

 

# Buscar item especifico 

buscar = 'Pocion de vida' 

if buscar in inventario: 

    print(f'[OK] {buscar} encontrada') 
else: 

    print(f'[X] {buscar} no disponible') 

# Simulacion de combate RPG 

vida_hero = 80 

vida_enemigo = 60 

ronda = 1 

 

while vida_hero > 0 and vida_enemigo > 0: 

    # Heroe ataca 

    dano_heroe = 15 

    vida_enemigo -= dano_heroe 

 

    # Enemigo contraataca 

    dano_enemigo = 10 

    vida_hero -= dano_enemigo 

 

    print(f'Ronda {ronda}: Hero={vida_hero}' 

          f' | Enemigo={vida_enemigo}') 

    ronda += 1 

 

resultado = 'VICTORIA!' if vida_hero > 0 else 'DERROTA' 

print(resultado) 

# Python: mismo ejercicio 

xp = 0 

nivel = 1 

xp_necesario = 100 

batallas = [20, 35, 15, 40, 30] 

for xp_ganado in batallas: 

    xp += xp_ganado 

    if xp >= xp_necesario: 

        nivel += 1 

        xp -= xp_necesario 

        print(f'Nivel {nivel}')


        # Funciones RPG 

 

def calcular_dano(ataque: int, defensa: int) -> int: 

    '''Retorna el dano real (minimo 1)''' 

    dano = ataque - defensa 

    return dano if dano > 0 else 1 

 

def aplicar_curacion( 

    vida: float, cur: float, max_vida: float) -> float: 

    '''Cura sin pasar el maximo''' 

    nueva = vida + cur 

    return min(nueva, max_vida) 

 

def mostrar_estado( 

    nombre: str, vida: float, nivel: int): 

    '''Imprime el estado del personaje''' 

    print(f'{nombre} [Nv{nivel}] HP: {vida:.0f}') 

 

# Prueba 

d = calcular_dano(20, 8) 

print(f'Dano: {d}') 

v = aplicar_curacion(40, 80, 100) 

mostrar_estado('Frodo', v, 3)


"""
Parametros: xp_actual (int), xp_necesario (int), nivel_actual (int) 
Logica: si xp_actual >= xp_necesario, incrementa nivel en 1, 
        reinicia xp a 0, imprime mensaje de nivel alcanzado. 
        Retorna el nuevo nivel. 
"""


def subirNivel(  xp_actual , xp_necesario , nivel_actual ):
    if(xp_actual >= xp_necesario):
        nivel_actual += 1
        xp_actual = 0
        print(f"nuevo nivel alcanzado {nivel_actual}")
    else:
        print(f"xp insuficiente {nivel_actual}")
    return nivel_actual

""" Prueba con: xp=110, xpNecesario=100, nivel=3 -> debe retornar 4 
            xp=80, xpNecesario=100, nivel=3 -> debe retornar 3 (no sube)  """

print( "xp=110, xpNecesario=100, nivel=3, retorno: " + str(subirNivel(110,100,3)) )
print( "xp=80, xpNecesario=100, nivel=3, retorno: " + str(subirNivel(80,100,3)) )