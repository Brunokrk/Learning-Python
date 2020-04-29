import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values, y_values, c='red' , edgecolor='none', s=40) 

#Define o titulo do grafico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000]) #valores minimo e maximo para eixo x e y respectivamente

plt.show()