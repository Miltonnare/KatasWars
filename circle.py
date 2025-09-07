import math

def circle(radius):
    if radius < 0:
        return ""
    if radius == 0:
        return "\n"
    
    diameter = 2 * radius + 1
    result = []

    if radius <= 2:
        diameter = 2 * radius - 1  
        for i in range(diameter):
            result.append('#' * diameter) 
        return '\n'.join(result) + '\n'
    
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


test_radii = [3, 15, 11, 30, 26, 28]

for r in test_radii:
    print(f"Radius: {r}")
    output = circle(r)
    lines = output.split('\n')
    for i in range(min(5, len(lines))):
        print(repr(lines[i]))
    print("...")
    print(f"Dimensions: {len(lines[0])}x{len(lines)-1}")