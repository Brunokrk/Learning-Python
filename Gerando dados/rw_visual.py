import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Apresentação
plt.title("Random Walks Generator", fontsize=24)
plt.xlabel("X Value", fontsize=14)
plt.ylabel("Y Value", fontsize=14)

while True:
    #Apresentação
    plt.title("Random Walks Generator", fontsize=24)
    plt.xlabel("X Value", fontsize=14)
    plt.ylabel("Y Value", fontsize=14)
    
    #Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()  
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    keep_running = input("Make another walk? (s/n)")
    if keep_running == 'n':
        break