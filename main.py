from tkinter import *
from grid import MyGrid
from interaction import MyInteraction
from engine import MyEngine
   
#App
dict_status = {}
dict_case = {}

fenetre = Tk()
args = dict({'height':500, 'width': 500, 'cell': 20, 'dict_status': dict_status, 'dict_case': dict_case,'flag': 0, 'speed': 50, 'fenetre':fenetre })

canvas = Canvas(fenetre, width=args.get('width'), height=args.get('height'), bg='white')
args['canvas'] = canvas
engine = MyEngine(args)
engine.init()

interactionService = MyInteraction(args)
canvas.bind("<Button-1>", interactionService.leftInteraction)
canvas.bind("<Button-2>", interactionService.rightInteraction)
canvas.pack(side =TOP, padx =5, pady =5)
champ_label = Label(fenetre, text="Salut les Zér0s !")

b1 = Button(fenetre, text="Play dude", command=engine.play)
text1 = Label(fenetre, text="Sorry ! cuz you'll have to click on 'Play dude' again and again ! that script isn't done")
#b2 = Button(fenetre, text="Reset", command=engine.stop)
b1.pack()
text1.pack()
#b2.pack()

grid = MyGrid(args)

fenetre.mainloop()