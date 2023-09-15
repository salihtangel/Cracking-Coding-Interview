grid = [[".", "A", "B", "B", "B"],
        [".", "A", ".", ".", "C"],
        [".", ".", ".", ".", "."],
        ["D", "D", ".", ".", "."],
        [".", "E", "E", "E", "E"]]
        


shots = [[0, 0], [0, 1], [0, 2], [1, 1], [0, 1], 
         [1, 4], [2, 2], [2, 4], [0, 3], [0, 0], [0,4]]
         

record = []


def solution(grid,shots):
    i = 0 
    counta = 0
    countb = 0
    countc = 0
    for i in range (len(shots)):
        print(grid[shots[i][0]] [shots[i][1]])

        if grid[shots[i][0]] [shots[i][1]] == ".":  
            record.append("Missed")
        if grid[shots[i][0]] [shots[i][1]] == "A":
            if counta > 1:
                record.append("Ship A sunk")
            else:
                record.append("Attacked ship A")
                counta = counta + 1  
        if grid[shots[i][0]] [shots[i][1]] == "B" :
            record.append("Attacked ship B")
        if grid[shots[i][0]] [shots[i][1]]  == "C":
            record.append("Attacked ship C")
        if grid[shots[i][0]] [shots[i][1]]  == "D":
            record.append("Attacked ship D")
        if grid[shots[i][0]] [shots[i][1]]  == "E":
            record.append("Attacked ship E")



        

    print(record)        
    
solution(grid,shots)