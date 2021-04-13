grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

grid_rows = len(grid)
grid_row = 0

#At first i tried this, but it didn't work:
#for i in range(grid_rows):
#    #print(len(grid[grid_row])) (returns 6 6 6 6 6 6 6)
#    for i in range(len(grid[grid_row])):
#        print(grid[i][grid_row], end='')
#    grid_row += 1
#    print()

#Than i tried this and it DID work:

for i in range(len(grid[grid_row])):
    #print(len(grid[grid_row])) 6 6 6 6 6 6 6
    for i in range(grid_rows):
        print(grid[i][grid_row], end='')
    grid_row += 1
    print()