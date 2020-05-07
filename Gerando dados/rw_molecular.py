import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
  

    #Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()

    #Define o tamanho da tela de plotagem
    plt.figure(dpi=128, figsize=(15,8))
    plt.title("Movimento de um Grão de pólem \n na superfície de uma gota d'água", fontsize=24)

    point_numbers = list(range(rw.num_points))  
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    #Enfatizando primeiro e ultimo ponto
    plt.scatter(0, 0, c='green', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=50)

    #Removendo os eixos
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    break