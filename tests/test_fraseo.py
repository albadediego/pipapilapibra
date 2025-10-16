import pytest
from pi_languaje import tokenizar, pi_a_normal, normal_a_pi, procesar_tokens

# ---------------------------
# Casos básicos: palabras y espacios
# ---------------------------
@pytest.mark.parametrize("frase, esperado", [
    ("hola mundo", ["hola", " ", "mundo"]),
    ("hola  mundo", ["hola", "  ", "mundo"]),  # Doble espacio
])
def test_tokenizar_basico(frase, esperado):
    assert tokenizar(frase) == esperado


# ---------------------------
# Puntuación básica
# ---------------------------
@pytest.mark.parametrize("frase, esperado", [
    ("hola, mundo", ["hola", ",", " ", "mundo"]),
    ("hola, mundo!", ["hola", ",", " ", "mundo", "!"]),
    ("¿como estas?", ["¿", "como", " ", "estas", "?"]),
    ("¡buenos dias!", ["¡", "buenos", " ", "dias", "!"]),
])
def test_tokenizar_puntuacion_basica(frase, esperado):
    assert tokenizar(frase) == esperado


# ---------------------------
# Mezcla de puntuación intermedia
# ---------------------------
@pytest.mark.parametrize("frase, esperado", [
    ("hola... mundo", ["hola", "...", " ", "mundo"]),
    ("hola-mundo", ["hola", "-", "mundo"]),
    ("uno, dos y tres.", ["uno", ",", " ", "dos", " ", "y", " ", "tres", "."]),
])
def test_tokenizar_puntuacion_intermedia(frase, esperado):
    assert tokenizar(frase) == esperado


# ---------------------------
# Casos con números y símbolos
# ---------------------------
@pytest.mark.parametrize("frase, esperado", [
    ("version 2.0 lista", ["version", " ", "2", ".", "0", " ", "lista"]),
    ("#hola mundo", ["#", "hola", " ", "mundo"]),
    ("correo@example.com", ["correo", "@", "example", ".", "com"]),
])
def test_tokenizar_simbolos_y_numeros(frase, esperado):
    assert tokenizar(frase) == esperado


# ---------------------------
# Casos límite
# ---------------------------
@pytest.mark.parametrize("frase, esperado", [
    ("", []),
    (" ", [" "]),
    ("...", ["..."]),
    ("pi", ["pi"]),
])
def test_tokenizar_casos_limite(frase, esperado):
    assert tokenizar(frase) == esperado


import pytest

# Suponemos que las funciones están importadas desde tu módulo principal:
# from mi_modulo import procesar_tokens, normal_a_pi, pi_a_normal

# ===============================================
# CASOS BÁSICOS
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    (["hola"], ["pihopila"]),
    (["mundo"], ["pimunpido"]),
])
def test_procesar_tokens_basicos(tokens, expected):
    assert procesar_tokens(tokens, normal_a_pi) == expected


# ===============================================
# PALABRAS CON PUNTUACIÓN O ESPACIOS
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    (["hola", ",", " ", "mundo", "!"], ["piholpia", ",", " ", "pimunpido", "!"]),
    (["adios", " ", "amigo"], ["piapidios", " ", "piapimipigo"]),
])
def test_procesar_tokens_con_puntuacion_y_espacios(tokens, expected):
    assert procesar_tokens(tokens, normal_a_pi) == expected


# ===============================================
# NÚMEROS Y COMBINACIONES ALFANUMÉRICAS
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    (["123"], ["123"]),
    (["abc123"], ["abc123"]),
    (["ver2"], ["ver2"]),
])
def test_procesar_tokens_con_numeros(tokens, expected):
    assert procesar_tokens(tokens, normal_a_pi) == expected


# ===============================================
# TOKENS NO PROCESABLES
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    (["!", "?", ",", "."], ["!", "?", ",", "."]),
    ([" ", "\t", "\n"], [" ", "\t", "\n"]),
])
def test_procesar_tokens_no_procesables(tokens, expected):
    assert procesar_tokens(tokens, normal_a_pi) == expected


# ===============================================
# MODO INVERSO (pi_a_normal)
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    (["pihopila", ",", " ", "pimunpido", "!"], ["hola", ",", " ", "mundo", "!"]),
    (["piapidios", " ", "piapimipigo"], ["adios", " ", "amigo"]),
])
def test_procesar_tokens_inverso(tokens, expected):
    assert procesar_tokens(tokens, pi_a_normal) == expected