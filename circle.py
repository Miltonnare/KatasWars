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
            
          
            if distance <= radius:
                row.append('#')
            else:
                row.append(' ')
        result.append(''.join(row))
    
    return '\n'.join(result) + '\n'



# Test for various radii
test_radii = [17, 18, 19, 20]

for r in test_radii:
    print(f"\nRadius {r}:")
    output = circle(r)

    lines = output.split('\n')
    for i in range(min(5, len(lines))):
        print(repr(lines[i]))
    print("...")
   
    print(f"Dimensions: {len(lines[0])}x{len(lines)-1}")