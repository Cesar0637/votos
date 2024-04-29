Característica: Registro de partido
    Como usuario del sistema de votacion
    Quiero registrar un un partido
    Para Que sea votado.

    Escenario: Registrar al partido azul
    Dado que ingreso a la url "http://localhost:8000/listaP/"
    Y presiono el boton Nuevo partido
    Y escribo el nombre del partido "azul" y su descripcion "partidoAzul"
    Cuando presiono el boton Guardar
    Entonces puedo ver el partido Azul en la lista de partidos.

