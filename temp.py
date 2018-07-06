def find_path_to_friend(network, user_A, user_B):
    node = [user_A]
    recursive(network, user_A, user_B, node)
    if node[-1] == user_B:
        return node
    else:
        return None

def recursive(network, user_A, user_B, node):
    if not network:
        return
    elif user_A+'Connection' not in network or user_B+'Connection' not in network:
        return
    
    if user_B in network[user_A+'Connection']:
        node.append(user_B)
        return #1
    for name in network[user_A+'Connection']: #2
        if name not in node:
            #node.remove(node[-1])
        #else:
            node.append(name)
            recursive(network, name, user_B, node)
            if node[-1] != user_B: #when recursive() ends, can either be 2 run out or return from 1
                node.remove(node[-1]) #if return from 1, do not remove any node record



network = {'AConnection':['B'],'BConnection':['A','C','D'],'CConnection':['A'],'DConnection':['E'],'EConnection':['D']}
print(find_path_to_friend(network, 'A', 'E'))
