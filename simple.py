def escalada(grafo, inicio, nodos_finales):
    nodo_actual = inicio
    camino_actual = [nodo_actual]
    peso_actual = 0
    
    while True:
        # Obtener los vecinos del nodo actual
        vecinos = list(grafo.neighbors(nodo_actual))
        
        # Evaluar las opciones basadas en el peso de los bordes
        opciones = []
        for vecino in vecinos:
            if vecino not in camino_actual:  # Evitar ciclos
                peso_borde = grafo[nodo_actual][vecino].get('weight', 1)
                opciones.append((vecino, peso_borde))
        
        if not opciones:
            # No hay vecinos disponibles, detenerse
            break
        
        # Elegir el vecino con el mayor peso de borde
        siguiente_vecino, siguiente_peso = max(opciones, key=lambda x: x[1])
        
        # Si el siguiente nodo es uno de los finales, detenerse
        if siguiente_vecino in nodos_finales:
            camino_actual.append(siguiente_vecino)
            peso_actual += siguiente_peso
            break
        
        # Si el borde tiene peso infinito, detenerse
        if siguiente_peso == float('inf'):
            break
        
        # Actualizar el estado actual
        camino_actual.append(siguiente_vecino)
        peso_actual += siguiente_peso
        nodo_actual = siguiente_vecino

    return camino_actual, peso_actual