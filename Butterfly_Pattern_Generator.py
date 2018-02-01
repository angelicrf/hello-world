print("\n\nBeautiful Butterfly Pattern Generator\n")
def draw_shape(w):
    
    h = w-1 if w % 2 == 0 else w
    s = ''
 
    # draw top
    s += draw_top(w, h)
    
    # draw middle
    s += 'A' * w
    # That is slice notation here is the syntax ''[start:stop:step]
    # so by changing step to -1 it reverses the string
      
    # draw bottom
    s += draw_top(w, h)[::-1]
    
    return s
    
def draw_top(w, h):
    s = ''
    for i in range(1, h//2 + 1):
        s += 'A'*i + ' ' * (w - 2*i) + 'A'*i +'\n'
        
    return s
    
query = 'Enter the width of the shape: '
width = int(input(query))
while (width <=0):
    query = 'Enter the width of the shape: '
    width = int(input(query))
print(draw_shape(width))

