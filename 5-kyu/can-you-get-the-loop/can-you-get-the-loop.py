def loop_size(node):
    tracker = node.next
    tracker2 = node.next.next
    
    while tracker != tracker2:
        tracker = tracker.next
        tracker2 = tracker2.next.next
        
    loop = 1
    tracker2 = tracker2.next
    while tracker != tracker2:
        tracker2 = tracker2.next
        loop +=1
    
        
    return loop