import tkinter

root = tkinter.Tk()

root.title("Tic Tac Toe")

'''make 3x3 tkinter buttons, each has a empty space'''
global nowturn
nowturn=0
buttons = [[0 for x in range(3)] for y in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tkinter.Button(root, text="", width=20, height=10, command=lambda i=i, j=j: button_clicked(i, j))
        buttons[i][j].grid(row=i, column=j)

def button_clicked(i, j):
    
    global nowturn
    print(nowturn)
    if nowturn == 0:
        buttons[i][j].config(text="X")
        buttons[i][j].configure(bg='yellow',state='disabled')
        nowturn = 1
    else:
        buttons[i][j].config(text="O")
        buttons[i][j].configure(bg='blue', state='disabled')
        nowturn = 0
    print(i, j)
root.mainloop()