import math
# inspiration code for Python Unit Testing Project


def surfaceArea(radius):
    return 4 * math.pi * (radius * radius)

#Volume = 4/3*pi*rad^3
def volume(radius):
    volume = (4/3) * math.pi * (radius * radius * radius)
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    print("\nThe Volume of a Sphere is = ", volume(radius))

if __name__ == '__main__':
    prompt()
