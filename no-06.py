class Maze:
    wall = "#"
    player = "x"
    space = " "
    mark = "."
    coorx = 0
    coory = 0

    def __init__(self, name):
        self.name = name
        self.file_read()
    
    def file_read(self):
        with open(self.name, "r") as f:
            self.maze_map = f.read().splitlines()
        for i in range(len(self.maze_map)):
            tmp = []
            for j in self.maze_map[i]:
                tmp.append(j)
            self.maze_map[i] = tmp
    
    def maze_settings(self):
        self.wall = input("Masukan character untuk wall = ")
        self.player = input("Masukan character untuk player = ")
        self.space = input("Masukan character untuk space = ")
        self.mark = input("Masukan character untuk mark = ")

    def maze_out(self):
        for i in range(len(self.maze_map)):
            for j in self.maze_map[i]:
                if j == " ":
                    print (self.space, end=self.space)
                elif j == "*":
                    print (self.wall, end=self.wall)
                elif j == "x":
                    print (self.player, end=" ")
                elif j == ".":
                    print (self.mark, end=" ")
                else:
                    print (j, end=" ")
            print ()
    
    def solve(self, y, x):
        mmap = self.maze_map
        if y > len(mmap) or x > len(mmap[0]):
            return False
        elif mmap[y][x] in ("T"):
            return True
        elif mmap[y][x] in ("*", "x", "."):
            return False
        else:
            mmap[y][x] = "x"
            found = self.solve(y - 1, x)
            if not found:
                found = self.solve(y + 1, x)
                if not found:
                    found = self.solve(y, x + 1)
                    if not found:
                        found = self.solve(y, x - 1)
                        if not found:
                            mmap[y][x] = "."
        return found

    def maze_solve(self):
        mmap = self.maze_map
        coorx = self.coorx
        coory = self.coory
        found = False

        for y in range(len(mmap)):
            for x in range(len(mmap[y])):
                if mmap[y][x] == "P":
                    coorx = x
                    coory = y
                    found = True
                    break
                if found:
                    break
        
        a = self.solve(coory, coorx)



maze = Maze("maze_map")
maze.maze_out()
maze.maze_solve()
maze.maze_out()
