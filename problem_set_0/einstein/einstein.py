# calculate energy
def main():
    m = int(input("Mass? "))
    print(energy(m))

def energy(m):
    
    c = 300000000
    return m*c**2


if __name__ == "__main__":
    main()
