"""docstring module"""
#อยากลองใช้ :) OOP
class Grid:
    """Grid class"""
    def __init__(self,row,col,value=0):
        """initialize the grid"""
        self.row = row
        self.col = col
        self.grid = [[value for _ in range(col)] for _ in range(row)]
    def get(self,row,col):
        """get value"""
        return self.grid[row][col]
    def set(self,row,col,value):
        """set value"""
        self.grid[row][col] = value
    def __str__(self):
        """print format for visualize"""
        return "\n".join([" ".join([f"{item:>4}" for item in row])+\
                          " | "+str(i) for i,row in enumerate(self.grid)])
    def get_safeplace(self):
        """get amount of safe place (0%)"""
        count = 0
        for i in self.grid:
            for j in i:
                if not j:
                    count += 1
        return count


def init_infected(city : Grid,amount : int):
    """initialize data infect percentage"""
    radius = 2
    for _ in range(amount):
        row,col = map(int,input().split(" "))
        city.set(row,col,100)
        for i in range(-radius,radius+1):
            for j in range(-radius,radius+1):
                new_r = max(0,i+row)
                new_c = max(0,j+col)
                try:
                    rad = max(abs(i), abs(j))
                    city.set(new_r,new_c,max(
                        city.get(new_r,new_c),
                        60 if rad == 1 else 20 if rad == 2 else 0
                    ))
                except IndexError:
                    continue


def main():
    """main function"""
    row,col = map(int,input().split(" "))
    pos_rabbit = list(map(int,input().split(" ")))
    infected_amount = int(input())
    city = Grid(row,col)
    init_infected(city,infected_amount)
    print(city.get_safeplace())
    print(str(city.get(pos_rabbit[0],pos_rabbit[1]))+"%")
main()
