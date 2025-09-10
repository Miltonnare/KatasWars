import math

def circle(radius):
    if radius < 0: 
        return ""
    if radius == 0: 
        return "\n"
    
   
    diameter = 2 * radius + 1  
    result = []
    
    for y in range(diameter):
        row = []
        for x in range(diameter):
           
            dx = x - radius  
            dy = y - radius  
            distance = math.sqrt(dx**2 + dy**2)
            
            
            if distance <= radius - 0.5:  
                row.append('#')
            else:
                row.append(' ')
        result.append(''.join(row))
    
    return '\n'.join(result) + '\n'


test_radii = [-255, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30]

for r in test_radii:
    print(f"Radius: {r}")
    output = circle(r)
    lines = output.split('\n')
   
    if r <= 6:
        print(output.rstrip('\n'))  
    else:
        for i in range(min(5, len(lines))):
            print(repr(lines[i]))
        print("...")
    print(f"Dimensions: {len(lines[0])}x{len(lines)-1}")
    print()