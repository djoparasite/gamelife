from pprint import pprint

class MyInteraction:
    def __init__(self, args):
        self.args = args

    def leftInteraction(self, event):
        pprint(event)
        x = event.x - (event.x % self.args.get('cell'))
        y = event.y - (event.y % self.args.get('cell'))
        self.args.get('canvas').create_rectangle(x, y, x+self.args.get('cell'), y+self.args.get('cell'), fill='blue')
        self.args.get('dict_case')[x,y] = 1

    def rightInteraction(self, event):
        pprint(event)
        x = event.x -(event.x%self.args.get('cell'))
        y = event.y -(event.y%self.args.get('cell'))
        self.args.get('canvas').create_rectangle(x, y, x+self.args.get('cell'), y+self.args.get('cell'), fill='white')
        self.args.get('dict_case')[x,y] = 0