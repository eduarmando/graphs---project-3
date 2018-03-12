import networkx as nx
import matplotlib.pyplot as plt
import sys
import Salesman1 as sm
import numpy as np
import re
import time
import SimulatedAnnealing as sa
import random

def procesar1():
    G = nx.Graph()
    G.add_edge('Colotlan','Tala',weight=168.18)
    G.add_edge('Colotlan','Ameca',weight=192.14)
    G.add_edge('Colotlan','Puerto Vallarta',weight=260.04)
    G.add_edge('Puerto Vallarta','Ameca',weight=123.17)
    G.add_edge('Puerto Vallarta','Autlan de Navarro',weight=132.84)
    G.add_edge('Autlan de Navarro','Ameca',weight=92.61)
    G.add_edge('Autlan de Navarro','Tecolotlan',weight=58.46)
    G.add_edge('Autlan de Navarro','Tapalpa',weight=66.36)
    G.add_edge('Ameca','Tecolotlan',weight=38.57)
    G.add_edge('Ameca','Tala',weight=37.68)
    G.add_edge('Tecolotlan','Tapalpa',weight=40.88)
    G.add_edge('Tala','Guadalajara',weight=36.97)
    G.add_edge('Tapalpa','Guadalajara',weight=90.14)
    G.add_edge('Tapalpa','Ciudad Guzman',weight=40.81)
    G.add_edge('Guadalajara','Ajijic',weight=41.09)
    G.add_edge('Ajijic','Ciudad Guzman',weight=69.57)
    G.add_edge('Guadalajara','Zapotlanejo',weight=29.72)
    G.add_edge('Zapotlanejo','Ajijic',weight=41.13)
    G.add_edge('Ajijic','Ocotlan',weight=52.22)
    G.add_edge('Zapotlanejo','Tepatitlan',weight=37.83)
    G.add_edge('Tepatitlan','Ocotlan',weight=52.05)
    G.add_edge('Ocotlan','La Barca',weight=23.59)
    G.add_edge('La Barca','Degollado',weight=46.65)
    G.add_edge('Degollado','Arandas',weight=36.32)
    G.add_edge('Tepatitlan','Arandas',weight=45.06)
    G.add_edge('Arandas','Jalostotitlan',weight=52.96)
    G.add_edge('Tepatitlan','Jalostotitlan',weight=50.42)
    G.add_edge('Jalostotitlan','San Juan de los Lagos',weight=16.56)
    G.add_edge('San Juan de los Lagos','Lagos de Moreno',weight=43.70)
    G.add_edge('Lagos de Moreno','Encarnacion de Diaz',weight=36.93)
    G.add_edge('Encarnacion de Diaz','San Juan de los Lagos',weight=32.43)

    ################    dibujar el grafo
    elarge=[(u,v) for (u,v,d) in G.edges(data=True)]
    pos = {'Colotlan': [22.11, -103.26], 'Tala': [20.54,-103.7],
                  'Ameca': [20.54,-104.04], 'Puerto Vallarta': [20.65,-105.22],
                  'Autlan de Navarro': [19.77,-104.36], 'Tecolotlan': [20.20,-104.04],
                  'Tapalpa': [19.94,-103.76], 'Guadalajara': [20.65,-103.35],
                  'Ciudad Guzman': [19.70,-103.46], 'Ajijic': [20.29,-103.26],
                  'Zapotlanejo': [20.61,-103.06], 'Ocotlan': [20.34,-102.76],
                  'Tepatitlan': [20.80,-102.76], 'La Barca': [20.29,-102.54],
                  'Degollado': [20.44,-102.13], 'Arandas': [20.70,-102.34],
                  'Jalostotitlan': [21.16,-102.46], 'San Juan de los Lagos': [21.24,-102.33],
                  'Lagos de Moreno': [21.26,-101.92], 'Encarnacion de Diaz': [21.52,-102.24]
                  }
    datos = []
    for key, value in pos.items():
        datos.append(value)
    #drawing nodes
    nx.draw_networkx_nodes(G,pos,node_size=100,node_color='b')
    #drawing edges
    nx.draw_networkx_edges(G,pos,edgelist=elarge,width=2,alpha=0.5,edge_color='r')

    #drawing labels
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

    print(G.nodes())
    ####Origen-Destino
    origen = (input("Ingresa origen:")).title()
    if not (G.has_node(origen)):
        print("Origen no encontrado")
        sys.exit()
    destino = (input("Ingresa destino:")).title()
    if not (G.has_node(destino)):
        print("Origen no encontrado")
        sys.exit()

    ####rutas
    print("Ruta mas corta:")
    start_time = time.time()
    print(nx.shortest_path(G, origen, destino, weight='weight'))#ruta mas corta
    print("--- SPA: %s seconds ---" % (time.time() - start_time))
    print("Distancia: ",nx.shortest_path_length(G, origen, destino, weight='weight'))#distancia mas corta
    plt.axis('off')
    plt.show()

    print("Minimum Spanning tree:")
    start_time = time.time()
    T=nx.minimum_spanning_tree(G)
    print("--- MST: %s seconds ---" % (time.time() - start_time))
    print(sorted(T.edges(data=True),"/n"))
    plt.figure()
    elarge=[(u,v) for (u,v,d) in T.edges(data=True)]
    nx.draw_networkx_nodes(G,pos,node_size=100,node_color='b')
    nx.draw_networkx_edges(G,pos,edgelist=elarge,width=2,alpha=0.5,edge_color='r')
    plt.axis('off')
    plt.show()

    nombres=("Colotlan","Encarnacion de Diaz","Lagos de Moreno","San Juan de los Lagos","Jalostotitlan","Tepatitlan","Arandas","Zapotlanejo","Degollado","La Barca","Ocotlan","Ajijic","Guadalajara","Tala","Ameca","Tecolotlan","Tapalpa","Ciudad Guzman","Puerto Vallarta","Autlan de Navarro")
    datos = [[22.11,-103.26],[21.52,-102.24],[21.26,-101.92],[21.24,-102.33],[21.16,-102.46],[20.80,-102.76],[20.70,-102.34],[20.61,-103.06],[20.44,-102.13],[20.29,-102.54],[20.34,-102.76],[20.29,-103.26],[20.65,-103.35],[20.54,-103.7],[20.54,-104.04],[20.20,-104.04],[19.94,-103.76],[19.70,-103.46],[20.65,-105.22],[19.77,-104.36]]
    points = datos
    print(nombres)
    origen = (input("TSP - Ingresa ciudad:")).title()
    if origen.title()  not in nombres:
        print("Ciudad no encontrada")
        sys.exit()
    ind = nombres.index(origen)
    start_time = time.time()
    resultado = sm.optimized_travelling_salesman(points, points[ind])
    print("--- TSPc: %s seconds ---" % (time.time() - start_time))
    print(resultado)
    show = list()
    datos = [[22.11,-103.26],[21.52,-102.24],[21.26,-101.92],[21.24,-102.33],[21.16,-102.46],[20.80,-102.76],[20.70,-102.34],[20.61,-103.06],[20.44,-102.13],[20.29,-102.54],[20.34,-102.76],[20.29,-103.26],[20.65,-103.35],[20.54,-103.7],[20.54,-104.04],[20.20,-104.04],[19.94,-103.76],[19.70,-103.46],[20.65,-105.22],[19.77,-104.36]]
    for i in resultado:
        ind = datos.index(i)
        show.append(nombres[ind])
    print("Ruta: ", show)
    print("Distancia: ",sm.total_distance(resultado)*111.325)
    output = np.vstack(resultado)
    x = output[:,0]
    y = output[:,1]
    plt.figure()
    plt.plot(x, y, '-o')
    plt.plot(x[0], y[0], 'og')
    plt.axis('off')
    plt.show()

    start_time = time.time()
    init_state = list(pos.keys())
    random.shuffle(init_state)

    # create a distance matrix
    distance_matrix = {}
    for ka, va in pos.items():
        distance_matrix[ka] = {}
        for kb, vb in pos.items():
            if kb == ka:
                distance_matrix[ka][kb] = 0.0
            else:
                distance_matrix[ka][kb] = sa.distance(va, vb)

    tsp = sa.TravellingSalesmanProblem(init_state, distance_matrix)
    tsp.steps = 100
    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"
    state, e = tsp.anneal()

    while state[0] != origen:
        state = state[1:] + state[:1]  # rotate NYC to start
    print("--- TSPa: %s seconds ---" % (time.time() - start_time))
    print("%f Km" % (e*1.60934)) #mile to km
    x = []
    y = []
    for i in state:
        dx, dy = pos[i]
        x.append(dx)
        y.append(dy)
    plt.figure()
    plt.plot(x, y, '-o')
    plt.plot(x[0], y[0], 'og')
    plt.axis('off')
    plt.show()

def procesar2(archivo):
    datos = []
    ciudades = {}
    with open(archivo) as fp:
        for line in fp:
            if re.match('^[1-9]+', line) is not None:
                renglon = (line.strip()).split(' ')
                datos.append([int(renglon[1]), int(renglon[2])])
                ciudades[int(renglon[0])] = (int(renglon[1]), int(renglon[2]))

    start_time = time.time()
    resultado = sm.optimized_travelling_salesman(datos)
    print("--- TSPc: %s seconds ---" % (time.time() - start_time))

    output = np.vstack(resultado)
    x = output[:,0]
    y = output[:,1]
    plt.figure()
    plt.plot(x, y, '-o')
    plt.plot(x[0], y[0], 'og')
    plt.axis('off')
    plt.show()

    start_time = time.time()
    init_state = list(ciudades.keys())
    random.shuffle(init_state)

    # create a distance matrix
    distance_matrix = {}
    for ka, va in ciudades.items():
        distance_matrix[ka] = {}
        for kb, vb in ciudades.items():
            if kb == ka:
                distance_matrix[ka][kb] = 0.0
            else:
                distance_matrix[ka][kb] = sa.distance(va, vb)

    tsp = sa.TravellingSalesmanProblem(init_state, distance_matrix)
    tsp.steps = 100
    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"
    state, e = tsp.anneal()

    while state[0] != 1:
        state = state[1:] + state[:1]  # rotate NYC to start
    print("--- TSPa: %s seconds ---" % (time.time() - start_time))
    print("%f Km" % (e*1.60934)) #mile to km
    x = []
    y = []
    for i in state:
        dx, dy = ciudades[i]
        x.append(dx)
        y.append(dy)
    plt.figure()
    plt.plot(x, y, '-o')
    plt.plot(x[0], y[0], 'og')
    plt.axis('off')
    plt.show()

def print_menu():
    print('1. 20 Ciudades')
    print('2. 100 Ciudades')
    print('3. 150 Ciudades')
    print('4. 200 Ciudades')
    print('5. Salir')
    print()

menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Ingresa un numero (1-5): "))
    if menu_choice == 1:
        procesar1()
    elif menu_choice == 2:
        procesar2('kroA100.txt')
    elif menu_choice == 3:
        procesar2('kroA150.txt')
    elif menu_choice == 4:
        procesar2('kroA200.txt')
    elif menu_choice != 5:
        print_menu()

#referencia
#https://networkx.github.io/documentation/networkx-1.9/examples/drawing/weighted_graph.html
#https://github.com/networkx/networkx/
#https://networkx.github.io/documentation/networkx-1.9/examples/drawing/weighted_graph.html


#obtener ruta mas rapida
#obtener MST (la ruta mas eficiente pasando por todos los nodos)

#instalar
#pip install networkx[all]