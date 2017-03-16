def PellNum(start, stop, step):
    """ (int,int,int) -> list of integers
    
    Input: This function is passed start (>= 0), stop (>start), and step (>= 1) values that define a sequence of numbers.
    Output: This function returns a list of the corresponding Pell Numbers.
    
    >>>PellNum(0,6,1)
    [0, 1, 2, 5, 12, 29]
    >>>PellNum(2,6,2)
    [2, 12]
    """
    
    Pell = []
        
    
    count = (1)
    
    Pell.append(0)
    Pell.append(1)
        
    if start == 0:
        stop -= 1
        while count < stop:
            x = Pell[-1]
            y = Pell[-2]
            z = 2*(x) + y
            Pell.append(z)
            count += 1
    
    elif start == 1:
        while count < stop:
            x = Pell[-1]
            y = Pell[-2]
            z = 2*(x) + y
            Pell.append(z)
            count += 1
            
    else:
        while len(Pell) < start:
            x = Pell[-1]
            y = Pell[-2]
            z = 2*(x) + y
            Pell.append(z)
        while count < stop:
            x = Pell[-1]
            y = Pell[-2]
            z = 2*(x) + y
            Pell.append(z) 
            count += 1
            
    Pell = Pell [-stop:]
    elPell = []
    
    if step == 1:
        Pell = Pell
    else:
       for i in Pell[::step]:
           elPell.append(i)
           Pell = elPell
           
    return Pell
           
        
    