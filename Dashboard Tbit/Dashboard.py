import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Database import produtos_data, Vendas_clientes_data, categorias_mais_vendidas_data  


plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color = ["Blue","orange","red","yellow","green"])

#Cria primeiro gráfico (gráfico de colunas verticais [bar])

'''Gráfico de produtos mais vendidos'''
fig1, ax1 = plt.subplots()

#Uitliza os dados(Produtos) da base de dados como parâmetro de informação do gráfico

ax1.bar(produtos_data.keys(), produtos_data.values())

#Define título principal do gráfico
ax1.set_title("Produtos mais vendidos")
#Define label inferior ao nome dos dados
ax1.set_xlabel("produtos")
#Define label latera a dados númericos
ax1.set_ylabel("Vendas")


#Cria segundo gráfico (gráfico de colunas verticais [barh])
 
'''Gráfico de vendas por parceiros''' 
fig2, ax2 = plt.subplots()
ax2.barh(list(Vendas_clientes_data.keys()), Vendas_clientes_data.values())
ax2.set_title("Vendas por parceiros")

ax2.set_xlabel("Parceiros")
ax2.set_ylabel("Vendas")

#Cria terceiro gráfico (gráfico de pizza [pie])

'''Gráfico de categorias mais vendidas'''
fig3, ax3 = plt.subplots()

ax3.pie(categorias_mais_vendidas_data.values(),labels = categorias_mais_vendidas_data.keys(), autopct='%1.1f%%')
ax3.set_title("Categorias mais vendidas")

#Exibe os gráficos
#plt.show()

#Criando janela TKinter

root = tk.Tk()
root.title("DASHBOARD")
root.state("zoomed")

upper_frame = tk.Frame(root)
upper_frame.pack(fill="both",expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both",expand=True)


canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both",expand=True)


canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both",expand=True)

root.mainloop()








 

