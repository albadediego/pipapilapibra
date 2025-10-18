import pytest
from pilengua_app.app.logic.pi_language import normal_a_pi, pi_a_normal

def test_normal_a_pi_basicos():
    assert normal_a_pi("hola") == "pihopila"
    assert normal_a_pi("") == ""

def test_normal_a_pi_palabras_silabeadas():
    # cotarte = co-tar-te → pi intercalado
    assert normal_a_pi("cotarte") == "picopitarpite"
    
    # caucho = cau-cho
    assert normal_a_pi("caucho") == "picaupicho"
    
    # inacción = in-ac-ción
    # assert normal_a_pi("inacción") == "piinpiacpición"
    
    # fluye = flu-ye
    assert normal_a_pi("fluye") == "piflupiye"

    #assert normal_a_pi("pino") == "pipipino"
    assert normal_a_pi("repican") == "pirepipipican"


@pytest.mark.parametrize(
    "pi_texto,esperado",
    [
        ("pihopila", "hola"),
        ("picopitarpite", "cotarte"),
        ("picaupicho", "caucho"),
        ("piinpiacpición", "inacción"),
        ("piflupiye", "fluye"),
        ("pipipipiopilo", "pipiolo"),
        ("pirepipipipi", "repipi")
    ],
)
def test_pi_a_normal_reversion(pi_texto, esperado):
    assert pi_a_normal(pi_texto) == esperado