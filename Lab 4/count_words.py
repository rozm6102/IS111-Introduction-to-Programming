def count_a(text): 
    
    text_list = text.split()
    
    a = 0 
    
    for word in text_list: 
        if word == "a": 
            a += 1 
        else: 
            a += 0
    
    return a


def count_an(text): 
    
    text_list = text.split()
    
    an = 0 
    
    for word in text_list: 
        if word == "an": 
            an += 1 
        else: 
            an += 0

    return an