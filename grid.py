class MyGrid:

    def __init__(self, args):
        self.args = args
        self.createGrid()

    def createGrid(self):
        self.vertical()
        self.horizontal()

    def vertical(self):
        x0 = 0
        while x0 != self.args.get('height'):
            self.args.get('canvas').create_line(x0, 0, x0, self.args.get('height'), width=1, fill='black')
            x0 += self.args.get('cell')
                    
    def horizontal(self):
        y0 = 0
        while y0 != self.args.get('height'):
            self.args.get('canvas').create_line(0, y0, self.args.get('width'), y0, width=1, fill='black')
            y0  += self.args.get('cell')