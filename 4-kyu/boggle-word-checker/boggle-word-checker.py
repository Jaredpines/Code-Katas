def find_word(board, word):
    if not word:
        return True
    if not board or not board[0]:
        return False
        
    rows = len(board)
    cols = len(board[0])
    
    board_chars = {char for row in board for char in row}
    if not all(char in board_chars for char in word):
        return False
​
    def dfs(r, c, index, visited):
        if index == len(word):
            return True
            
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            (r, c) in visited or 
            board[r][c] != word[index]):
            return False
            
        visited.add((r, c))
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        for dr, dc in directions:
            if dfs(r + dr, c + dc, index + 1, visited):
                return True
                
        visited.remove((r, c))
        return False
​
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if dfs(r, c, 0, set()):
                    return True
                    
    return False