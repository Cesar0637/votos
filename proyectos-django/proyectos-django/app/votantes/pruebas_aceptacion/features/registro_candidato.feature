Característica: Registro de candidato
    Como administrador del sistema de votacion
    Quiero registrar un candidato
    Para Que sea votado.

    Escenario: Registrar al candidato margarito
    Dado que ingreso a la url "http://localhost:8000/listaC/"
    Y presiono el boton de Nuevo candidato
    Y escribo el nombre "margarito" y su apeido paterno "ruiz" y su apeido materno "salas"
    Y selecciono su partido "naranja"
    Cuando presiono el boton de Guardar
    Entonces puedo ver el candidato margarito en la lista de candidatos.

