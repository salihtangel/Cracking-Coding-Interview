def solution(grid, shots):
    ship_cells = {}
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cell = grid[row][col]
            if cell != ".":
                if cell in ship_cells:
                    ship_cells[cell].append((row, col))
                else:
                    ship_cells[cell] = [(row, col)]

    results = []
    attacked_ships = set()

    for shot in shots:
        row, col = shot
        cell = grid[row][col]
        
        if cell == ".":
            results.append("Missed")
        elif tuple(shot) in attacked_ships:
            results.append("Already attacked")
        else:
            attacked_ships.add(tuple(shot))
            ship = grid[row][col]
            ship_cells[ship].remove(shot)
            
            if len(ship_cells[ship]) == 0:
                results.append(f"Ship {ship} sunk")
            else:
                results.append(f"Attacked ship {ship}")
    
    return results

grid = [
    [".", "A", "B", "B", "B"],
    [".", "A", ".", ".", "C"],
    [".", ".", ".", ".", "."],
    ["D", "D", ".", ".", "."],
    [".", "E", "E", "E", "E"]
]

shots = [
    [0, 0], [0, 1], [0, 2], [1, 1], [0, 1],
    [1, 4], [2, 2], [2, 4], [0, 3], [0, 0], [0, 4]
]

result = solution(grid, shots)
print(result)
