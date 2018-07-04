def cellular_automation(string, pattern_number, generations):
    patterns = {}
    pattern_list  = ['...','..x','.x.','.xx','x..','x.x','xx.','xxx']
    n = len(string)
    
    #build my patterns dictionary
    for i in range(7,-1, -1):
        if pattern_number/(2**i) == 1: #8 elements in pattern_list corresp. 1 to 128
            patterns[pattern_list[i]] == 'x'
            pattern_number -= 2**i
        else:
            patterns[pattern_list[i]] == '.'
            
    #make a new string by applying pattern to string generation times
    for j in range(0, generations):
        new_string = ''
        for i in range(0, n):
            pattern = string[i-1] + string[i] + string[(i+1)%n]
            new_string = new_string + patterns[pattern]
        string = new_string
    return new_string

