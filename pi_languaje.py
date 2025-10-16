from enum import Enum

CONSONANTES = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "ll", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "z")
VOCALES_ABIERTAS = ("a", "e", "o")
VOCALES_CERRADAS = ("i", "u")
SEMIVOCALES = ("y",)
PARES_CONSONANTES = ("bl", "cl", "fl", "gl", "kl", "pl", "tl", "br", "cr", "dr", "fr", "gr", "kr", "pr", "tr", "ch", "ll", "rr")

class ES_PI(Enum):
    NO_HAY_PI = 0
    SOLO_P = 1
    HAY_PI = 2

def es_vocal(caracter):
    return caracter in VOCALES_ABIERTAS or caracter in VOCALES_CERRADAS

def es_diptongo(grupo):
    if grupo[0] in VOCALES_ABIERTAS and grupo[1] in VOCALES_CERRADAS:
        return True
    elif grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_ABIERTAS:
        return True
    elif grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_CERRADAS:
        return True

def es_triptongo(grupo):
    return grupo[0] in VOCALES_CERRADAS and grupo[1] in VOCALES_ABIERTAS and grupo[2] in VOCALES_CERRADAS

def es_grupo_vocalico_ok(grupo, caracter):
    # Asumimos que tanto grupo como caracter solo pueden estar formados por vocales y que caracter siempre va informado (con una vocal)
    if grupo == "": 
        return True
    
    if es_diptongo(grupo + caracter):
        return True
    if es_triptongo(grupo + caracter):
        return True
    
    return False


def obtener_grupos_vocalicos(palabra):
    grupos_vocalicos = []
    grupo = ""
    for caracter in palabra:
        if es_vocal(caracter):
            if es_grupo_vocalico_ok(grupo, caracter):
                grupo += caracter
            else:
                grupos_vocalicos.append(grupo)
                grupo = caracter
        elif grupo:
            grupos_vocalicos.append(grupo)
            grupo = ""

    if grupo:
        grupos_vocalicos.append(grupo)

    
    return grupos_vocalicos

def es_grupo_consonantico(anterior, caracter):
    if anterior + caracter in PARES_CONSONANTES:
        return anterior + caracter
    else:
        return caracter

def add_grupo_consonantes_delante(grupos_vocalicos, palabra):
    ix_grupo_vocalico = 0
    grupos_protosilabas = grupos_vocalicos[:] #para no modificar el original, buena practica
    consonante_anterior = ""

    for caracter in palabra:
        if ix_grupo_vocalico >= len(grupos_protosilabas):
            break
        if caracter in grupos_protosilabas[ix_grupo_vocalico]:
            grupos_protosilabas[ix_grupo_vocalico] = consonante_anterior + grupos_protosilabas[ix_grupo_vocalico]
            ix_grupo_vocalico += 1
            consonante_anterior = ""
        else:
            consonante_anterior = es_grupo_consonantico(consonante_anterior, caracter)

    return grupos_protosilabas
    

def completar(grupos_protosilabicos, palabra):
    ix_grupo = 0
    ix_dentro_grupo = 0

    for caracter in palabra:
        if ix_dentro_grupo < len(grupos_protosilabicos[ix_grupo]) and \
           caracter == grupos_protosilabicos[ix_grupo][ix_dentro_grupo]:
            ix_dentro_grupo +=1
            continue
        else:
            if ix_grupo < len(grupos_protosilabicos)-1  and \
               caracter == grupos_protosilabicos[ix_grupo + 1][0]:
                ix_grupo += 1
                ix_dentro_grupo = 1
            else:
                grupos_protosilabicos[ix_grupo] += caracter



def silabear(palabra):
    grupos_vocalicos = obtener_grupos_vocalicos(palabra)
    grupos_protosilabicos = add_grupo_consonantes_delante(grupos_vocalicos, palabra)
    completar(grupos_protosilabicos, palabra)
    return grupos_protosilabicos

def normal_a_pi(palabra):
    if palabra == "":
        return ""
    silabas = silabear(palabra)
    resultado = ""
    for silaba in silabas:
        resultado += "pi" + silaba
    return resultado

def pi_a_normal(palabra):
    silabeada = silabear(palabra)
    resultado = []
    for i, silaba in enumerate(silabeada):
        if i % 2 != 0:
            resultado.append(silaba)

    return "".join(resultado)

def pi_a_normal(palabra):
    resultado = ""
    pi_en_construccion = ES_PI.NO_HAY_PI
    for caracter in palabra:
        if caracter == "p" and not pi_en_construccion == ES_PI.NO_HAY_PI:
            pi_en_construccion = ES_PI.SOLO_P
            continue
        if caracter == "i" and pi_en_construccion == ES_PI.SOLO_P:
            pi_en_construccion = ES_PI.HAY_PI
            continue
        pi_en_construccion = ES_PI.NO_HAY_PI
        resultado += caracter
    return resultado



if __name__ == "__main__":
    print(completar(["tra", "po", "te"], "transportes"))