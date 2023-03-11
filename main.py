from lib import *


def test_call():
    # Create some clothing items
    socks = Socks("cotton", "white", "medium", "striped")
    shoes = Shoes("leather", "black", "9", "loafers")
    scarf = Scarf("wool", "gray", "one size", "200")
    hat = Hat("wool", "blue", "one size", "beanie")
    gloves = Gloves("leather", "brown", "medium", True)
    pants = Pants("denim", "blue", "32x32", 76)
    dress = Dress("silk", "green", "medium", 115)
    skirt = Skirt("cotton", "pink", "small", 45)
    coat = Coat("wool", "black", "medium", 95)
    shirt = Shirt("button-up", "cotton", "white", "medium", "short")
    tshirt = TShirt("graphic tee", "cotton", "black", "large", "star wars")
    glasses = Glasses("sunglasses", "plastic", "brown", "one size", "brown")
    headband = Headband("sports", "nylon", "red", "one size", "5")
    shawl = Shawl("fringe", "wool", "orange", "one size", "geometric")
    sweatshirt = Sweatshirt("hoodie", "cotton", "gray", "medium", True)

    # Print out the details of each clothing item
    print(socks)
    print(shoes)
    print(scarf)
    print(hat)
    print(gloves)
    print(pants)
    print(dress)
    print(skirt)
    print(coat)
    print(shirt)
    print(tshirt)
    print(glasses)
    print(headband)
    print(shawl)
    print(sweatshirt)

    # Get specific details of some clothing items
    print(f"\n\nThe gloves are {gloves.get_material()} and {gloves.get_color()}")
    print(f"\n\nThe shoes are {shoes.get_size()} and have a {shoes.style} style")


if __name__ == '__main__':
    test_call()
