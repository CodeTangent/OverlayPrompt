import tkinter as tk

'''
Cria a janela sobrescrevendo o que estiver ao fundo e obrigando que ela fique a frente de tudo o que estiver aberto
'''
root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)


def position(window, width, height, x, y):
    window.geometry(f"{width}x{height}+{x}+{y}")
position(window=root, width=800, height=300, x=50, y=700 )

'''
Pra deixar a label visível é necessário definir uma cor para a janela e depois tornar essa cor transparente
'''
root.config(bg="black")
root.wm_attributes("-transparentcolor", "black")
 
'''
Definida a cor da mensagem em uma cor diferente da utilizada, obrigando que ela apareça
'''
label = tk.Label(root, text="SEPARAR\nBADGE do GRSA", 
                 font=("Segoe UI Light", 50, "bold"), 
                 fg="#8BC34A", 
                 bg="#f5f6f7")

label2 = tk.Label(root, text="para fazer o check-in", 
                  font=("Segoe UI Light", 30, "bold"), 
                  fg="#8BC34A", 
                  bg="#f5f6f7")
label.pack()
label2.pack()

label.bind("<Button-1>", 
           lambda e: root.destroy())

label2.bind("<Button-1>", 
           lambda e: root.destroy())
 


root.mainloop()
