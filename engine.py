from grid import MyGrid

class MyEngine:
    def __init__(self, args):
        self.args = args
        self.init()

    def playSafe(self):
        global flag
        if flag == 0:
            flag =1
            self.play()
    def play(self):
        #global flag, vitesse
        v=0
        while v != self.args.get('width') / self.args.get('cell'):
            w=0
            while w!= self.args.get('height')/self.args.get('cell'):
                x = v * self.args.get('cell')
                y = w * self.args.get('cell')
                dc = self.args.get('dict_case')
                ds = self.args.get('dict_status')
                
                # corners
                if x == 0 and y == 0: #left top
                    compt_viv = 0
                    if dc[x, y+ self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y+self.args.get('cell')]==1:
                        compt_viv+=1
                    ds[x, y]=compt_viv
                elif x==0 and y==int(self.args.get('height')-self.args.get('cell')): #left bot
                    compt_viv=0
                    if dc[x, y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y]==1:
                        compt_viv+=1
                    ds[x, y]=compt_viv
                elif x==int(self.args.get('width')-self.args.get('cell')) and y==0: #top right
                    compt_viv=0
                    if dc[x-self.args.get('cell'), y]==1:
                        compt_viv+=1
                    if dc[x-self.args.get('cell'), y+self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x, y+self.args.get('cell')]==1:
                        compt_viv+=1
                    ds[x, y]=compt_viv
                elif x==int(self.args.get('width')-self.args.get('cell')) and y==int(self.args.get('height')-self.args.get('cell')): #bot right
                    compt_viv=0
                    if dc[x-self.args.get('cell'), y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x-self.args.get('cell'), y]==1:
                        compt_viv+=1
                    if dc[x, y-self.args.get('cell')]==1:
                        compt_viv+=1
                    ds[x, y]=compt_viv
                    
                # border without corners   
                elif x==0 and 0<y<int(self.args.get('height')-self.args.get('cell')): # border left
                    compt_viv=0
                    if dc[x, y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x, y+self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y+self.args.get('cell')]==1:
                        compt_viv+=1
                    ds[x, y]=compt_viv
                elif x==int(self.args.get('width')-self.args.get('cell')) and 0<y<int(self.args.get('height')-self.args.get('cell')): # border right
                    compt_viv=0
                    if dc[x-self.args.get('cell'), y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x-self.args.get('cell'), y]==1:
                        compt_viv+=1
                    if dc[x-self.args.get('cell'), y+self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x, y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x, y+self.args.get('cell')]==1:
                        compt_viv+=1
                    ds[x, y]=compt_viv
                elif 0<x<int(self.args.get('width')-self.args.get('cell')) and y==0: # border top
                    compt_viv=0
                    if dc[x-self.args.get('cell'), y]==1:
                        compt_viv+=1
                    if dc[x-self.args.get('cell'), y+self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x, y+self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y+self.args.get('cell')]==1:
                        compt_viv+=1
                    ds[x, y]=compt_viv
                elif 0<x<int(self.args.get('width')-self.args.get('cell')) and y==int(self.args.get('height')-self.args.get('cell')): # border bot
                    compt_viv=0
                    if dc[x-self.args.get('cell'), y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x-self.args.get('cell'), y]==1:
                        compt_viv+=1
                    if dc[x, y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y]==1:
                        compt_viv+=1
                    ds[x, y]=compt_viv

                #cell no border
                else:
                    compt_viv=0
                    if dc[x-self.args.get('cell'), y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x-self.args.get('cell'), y]==1:
                        compt_viv+=1
                    if dc[x-self.args.get('cell'), y+self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x, y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x, y+self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y-self.args.get('cell')]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y]==1:
                        compt_viv+=1
                    if dc[x+self.args.get('cell'), y+self.args.get('cell')]==1:
                        compt_viv+=1
                    ds[x, y]=compt_viv
                    
                w+=1
            v+=1
        self.reset()
        if self.args.get('flag') > 0: 
            self.args.get('fenetre').after(self.args.get('speed'),self.play)

    def stop(self):
        global flag    
        flag = 0

    def reset(self):
        canvas = self.args.get('canvas')
        canvas.delete("all")
        grid = MyGrid(self.args)
        t = 0
        while t!= self.args.get('width') / self.args.get('cell'):
            u=0
            while u!= self.args.get('height')/self.args.get('cell'):
                x = t * self.args.get('cell')
                y = u * self.args.get('cell')
                dc = self.args.get('dict_case')
                ds = self.args.get('dict_status')
                if ds[x,y]==3:
                    dc[x,y] = 1
                    canvas.create_rectangle(x, y, x+self.args.get('cell'), y+self.args.get('cell'), fill='blue')
                elif ds[x,y]==2:
                    if dc[x,y]==1:
                        canvas.create_rectangle(x, y, x+self.args.get('cell'), y+self.args.get('cell'), fill='blue')
                    else:
                        canvas.create_rectangle(x, y, x+self.args.get('cell'), y+self.args.get('cell'), fill='white')
                elif ds[x,y]<2 or ds[x,y]>3:
                    dc[x,y]=0
                    canvas.create_rectangle(x, y, x+self.args.get('cell'), y+self.args.get('cell'), fill='white')
                u+=1
            t+=1
        

    def init(self):
        i = 0
        while i!= self.args.get('width')/self.args.get('cell'):
            j = 0
            while j!= self.args.get('height')/self.args.get('cell'):
                x = i * self.args.get('cell')
                y = j * self.args.get('cell')
                self.args.get('dict_case')[x,y] = 0
                j += 1
            i += 1