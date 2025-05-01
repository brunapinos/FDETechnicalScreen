def sort(width, height, length, mass):
    bulky = False
    heavy = False
    
    sorted_dimensions = sorted([width, height, length])
    volume = width * height * length

    if sorted_dimensions[-1] >= 150 or volume > 1000000:
        bulky = True
    
    if mass >= 20:
        heavy = True
    
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

def main():
    count = int(input())
    for i in range(count):
        width, height, length, mass = map(int, input().split())
        result = sort(width, height, length, mass)
        print(result)

if __name__ == "__main__":
    main()