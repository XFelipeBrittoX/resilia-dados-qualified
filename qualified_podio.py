def podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3,nome_corredor1,nome_corredor2,nome_corredor3):
    if tempo_chegada1 < tempo_chegada2 and tempo_chegada2 < tempo_chegada3:
        return f'1 - {nome_corredor1} - {tempo_chegada1} minutos\n2 - {nome_corredor2} - {tempo_chegada2} minutos\n3 - {nome_corredor3} - {tempo_chegada3} minutos\n'
    elif tempo_chegada1 < tempo_chegada3 and tempo_chegada3 < tempo_chegada2:
        return f'1 - {nome_corredor1} - {tempo_chegada1} minutos\n2 - {nome_corredor3} - {tempo_chegada3} minutos\n3 - {nome_corredor2} - {tempo_chegada2} minutos\n'
    elif tempo_chegada2 < tempo_chegada3 and tempo_chegada3 < tempo_chegada1:
        return f'1 - {nome_corredor2} - {tempo_chegada2} minutos\n2 - {nome_corredor3} - {tempo_chegada3} minutos\n3 - {nome_corredor1} - {tempo_chegada1} minutos\n'
    elif tempo_chegada2 < tempo_chegada1 and tempo_chegada1 < tempo_chegada3:
        return f'1 - {nome_corredor2} - {tempo_chegada2} minutos\n2 - {nome_corredor1} - {tempo_chegada1} minutos\n3 - {nome_corredor3} - {tempo_chegada3} minutos\n'
    elif tempo_chegada3 < tempo_chegada2 and tempo_chegada2 < tempo_chegada1:
        return f'1 - {nome_corredor3} - {tempo_chegada3} minutos\n2 - {nome_corredor2} - {tempo_chegada2} minutos\n3 - {nome_corredor1} - {tempo_chegada1} minutos\n'
    elif tempo_chegada3 < tempo_chegada1 and tempo_chegada1 < tempo_chegada2:
        return f'1 - {nome_corredor3} - {tempo_chegada3} minutos\n2 - {nome_corredor1} - {tempo_chegada1} minutos\n3 - {nome_corredor2} - {tempo_chegada2} minutos\n'