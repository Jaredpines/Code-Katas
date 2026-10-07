from collections import deque
​
def tree_by_levels(node):
    if not node:
        return []
    
    result = []
    queue = deque([node])
    
    while queue:
        currentNode = queue.popleft()
        
        result.append(currentNode.value)
        
        if currentNode.left:
            queue.append(currentNode.left)
            
        if currentNode.right:
            queue.append(currentNode.right)
            
    return result