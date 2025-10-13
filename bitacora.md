# Interfaz
La logica con python en el servidor

    entrada: ____hola
    >>traducir<<
    salida: ____pihopila

    entrada: ____pihopila
    >>traducir<<
    salida: ____hola

# Fases de desarrollo
1. Crear dos funciones
    - def normal_a_pi(palabra: str) -> str
    - def pi_a_normal(palabra: str) -> str

2. Estructura del proyecto
/proyecto_pi/
    app.py
    /templates/
    /static/
    /tests/
    /pi_lenguaje.py

3. Crear los tests
    normal_a_pi("hola") -> "pihopila"
    normal_a_pi("") -> ""
    | cotarte   | co-tar-te               |
    | caucho    | cau-cho                 |
    | inacción  | in-ac-ción              |
    | fluye     | flu-ye    

4. Me he dado cuenta de que silabear va antes
- Crear funcion
    def silabear(palabra) -> [str]