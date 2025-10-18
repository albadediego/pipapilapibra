import pytest
from pilengua_app.app.logic.pi_language import pi_a_normal, normal_a_pi, tokenizar, procesar_tokens, reconstruir_frase, frase_a_pi, pi_a_frase

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
    ("version 2.0 lista", ["version", " ", "2.0", " ", "lista"]),
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
    (["hola", ",", " ", "mundo", "!"], ["pihopila", ",", " ", "pimunpido", "!"]),
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
    (["pihola", ",", " ", "pimundo", "!"], ["hola", ",", " ", "mundo", "!"]),
    (["piadios", " ", "piamigo"], ["adios", " ", "amigo"]),
])
def test_procesar_tokens_inverso(tokens, expected):
    assert procesar_tokens(tokens, pi_a_normal) == expected


# ===============================================
# CASOS BÁSICOS
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    (["hola"], "hola"),
    (["pihola"], "pihola"),
])
def test_reconstruir_frase_basicos(tokens, expected):
    assert reconstruir_frase(tokens) == expected


# ===============================================
# PALABRAS SEPARADAS POR ESPACIOS
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    (["hola", " ", "mundo"], "hola mundo"),
    (["pihola", " ", "pimundo"], "pihola pimundo"),
    (["hola", " ", "amigo", " ", "bueno"], "hola amigo bueno"),
])
def test_reconstruir_frase_con_espacios(tokens, expected):
    assert reconstruir_frase(tokens) == expected


# ===============================================
# PUNTUACIÓN BÁSICA
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    (["hola", ",", " ", "mundo", "!"], "hola, mundo!"),
    (["adios", ".", " ", "hasta", " ", "luego"], "adios. hasta luego"),
])
def test_reconstruir_frase_con_puntuacion(tokens, expected):
    assert reconstruir_frase(tokens) == expected


# ===============================================
# TOKENS CON DÍGITOS (NO PALABRAS)
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    (["h", "o", "l", "a", " ", "123"], "hola 123"),
    (["nivel", " ", "42"], "nivel 42"),
    (["pi", "nomb", "re", " ", "2025"], "pinombre 2025"),
])
def test_reconstruir_frase_con_digitos(tokens, expected):
    assert reconstruir_frase(tokens) == expected


# ===============================================
# CASOS MIXTOS Y CON SIMBOLOS
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    (["@", "usuario", ":", " ", "hola"], "@usuario: hola"),
    (["(", "piamigo", ")", " ", "pi!", " ", "123"], "(piamigo) pi! 123"),
])
def test_reconstruir_frase_casos_mixtos(tokens, expected):
    assert reconstruir_frase(tokens) == expected


# ===============================================
# LISTA VACÍA O SIN ELEMENTOS
# ===============================================
@pytest.mark.parametrize("tokens, expected", [
    ([], ""),
    ([""], ""),
])
def test_reconstruir_frase_vacia(tokens, expected):
    assert reconstruir_frase(tokens) == expected


# from mi_modulo import frase_a_pi, pi_a_frase


# ==========================================================
# TESTS PARA frase_a_pi
# ==========================================================
class TestFraseAPi:

    # -------------------------------
    # Casos básicos
    # -------------------------------
    @pytest.mark.parametrize("frase, expected", [
        ("hola", "pihopila"),
        ("mundo", "pimunpido"),
        ("nombre", "pinompibre"),
    ])
    def test_basicos(self, frase, expected):
        assert frase_a_pi(frase) == expected

    # -------------------------------
    # Frases con espacios
    # -------------------------------
    @pytest.mark.parametrize("frase, expected", [
        ("hola mundo", "pihopila pimunpido"),
        ("nombre propio", "pinompibre pipropipio"),
    ])
    def test_con_espacios(self, frase, expected):
        assert frase_a_pi(frase) == expected

    # -------------------------------
    # Puntuación básica
    # -------------------------------
    @pytest.mark.parametrize("frase, expected", [
        ("hola, mundo!", "pihopila, pimunpido!"),
        ("nombre propio.", "pinompibre pipropipio."),
    ])
    def test_con_puntuacion(self, frase, expected):
        assert frase_a_pi(frase) == expected

    # -------------------------------
    # Dígitos y símbolos
    # -------------------------------
    @pytest.mark.parametrize("frase, expected", [
        ("hola 123", "pihopila 123"),
        ("mundo!", "pimunpido!"),
        ("#hola", "#pihopila"),
    ])
    def test_con_digitos_y_simbolos(self, frase, expected):
        assert frase_a_pi(frase) == expected

    # -------------------------------
    # Casos vacíos y extremos
    # -------------------------------
    @pytest.mark.parametrize("frase, expected", [
        ("", ""),
        (" ", " "),
        ("!", "!"),
    ])
    def test_vacios_y_extremos(self, frase, expected):
        assert frase_a_pi(frase) == expected


# ==========================================================
# TESTS PARA pi_a_frase
# ==========================================================
class TestPiAFrase:

    # -------------------------------
    # Casos básicos
    # -------------------------------
    @pytest.mark.parametrize("frase, expected", [
        ("pihopila", "hola"),
        ("pimunpido", "mundo"),
        ("pinompibre", "nombre"),
    ])
    def test_basicos(self, frase, expected):
        assert pi_a_frase(frase) == expected

    # -------------------------------
    # Frases con espacios
    # -------------------------------
    @pytest.mark.parametrize("frase, expected", [
        ("pihopila pimunpido", "hola mundo"),
        ("pinompibre pipropipio", "nombre propio"),
    ])
    def test_con_espacios(self, frase, expected):
        assert pi_a_frase(frase) == expected

    # -------------------------------
    # Puntuación básica
    # -------------------------------
    @pytest.mark.parametrize("frase, expected", [
        ("pihopila, pimunpido!", "hola, mundo!"),
        ("pinompibre pipropipio.", "nombre propio."),
    ])
    def test_con_puntuacion(self, frase, expected):
        assert pi_a_frase(frase) == expected

    # -------------------------------
    # Dígitos y símbolos
    # -------------------------------
    @pytest.mark.parametrize("frase, expected", [
        ("pihopila 123", "hola 123"),
        ("pimunpido!", "mundo!"),
        ("#pihopila", "#hola"),
    ])
    def test_con_digitos_y_simbolos(self, frase, expected):
        assert pi_a_frase(frase) == expected

    # -------------------------------
    # Casos vacíos y extremos
    # -------------------------------
    @pytest.mark.parametrize("frase, expected", [
        ("", ""),
        (" ", " "),
        ("!", "!"),
    ])
    def test_vacios_y_extremos(self, frase, expected):
        assert pi_a_frase(frase) == expected