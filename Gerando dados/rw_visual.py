import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    #Apresentação
    plt.title("Random Walks Generator", fontsize=24)

    #Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()

    #Define o tamanho da tela de plotagem
    plt.figure(dpi=128, figsize=(10,6))


    point_numbers = list(range(rw.num_points))  
    plt.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

    #Enfatizando primeiro e ultimo ponto
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    #Removendo os eixos
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (s/n)")
    if keep_running == 'n':
        break