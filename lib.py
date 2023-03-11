class ClothingItem:
    def __init__(self, name, material, color, size):
        self.name = name
        self.material = material
        self.color = color
        self.size = size

    def __str__(self):
        return f"\n\n{self.name} -- {self.size} {self.color} {self.material} {self.name}\n"

    def get_material(self):
        return self.material

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size


class Socks(ClothingItem):
    def __init__(self, material, color, size, pattern):
        super().__init__("socks", material, color, size)
        self.pattern = pattern

    def __str__(self):
        return super().__str__() + f" ({self.pattern} pattern)"


class Shoes(ClothingItem):
    def __init__(self, material, color, size, style):
        super().__init__("shoes", material, color, size)
        self.style = style

    def __str__(self):
        return super().__str__() + f" ({self.style} style)"


class Scarf(ClothingItem):
    def __init__(self, material, color, size, length):
        super().__init__("scarf", material, color, size)
        self.length = length

    def __str__(self):
        return super().__str__() + f" ({self.length} cm long)"


class Hat(ClothingItem):
    def __init__(self, material, color, size, style):
        super().__init__("hat", material, color, size)
        self.style = style

    def __str__(self):
        return super().__str__() + f" ({self.style} style)"


class Gloves(ClothingItem):
    def __init__(self, material, color, size, fingerless):
        super().__init__("gloves", material, color, size)
        self.fingerless = fingerless

    def __str__(self):
        if self.fingerless:
            return super().__str__() + " (fingerless)"
        else:
            return super().__str__() + " (full fingered)"


class Pants(ClothingItem):
    def __init__(self, material, color, size, length):
        super().__init__("pants", material, color, size)
        self.length = length

    def __str__(self):
        return super().__str__() + f" ({self.length} cm inseam)"


class Dress(ClothingItem):
    def __init__(self, material, color, size, length):
        super().__init__("dress", material, color, size)
        self.length = length

    def __str__(self):
        return super().__str__() + f" ({self.length} cm long)"


class Skirt(ClothingItem):
    def __init__(self, material, color, size, length):
        super().__init__("skirt", material, color, size)
        self.length = length

    def __str__(self):
        return super().__str__() + f" ({self.length} cm long)"


class Coat(ClothingItem):
    def __init__(self, material, color, size, length):
        super().__init__("coat", material, color, size)
        self.length = length

    def __str__(self):
        return super().__str__() + f" ({self.length} cm long)"


class Shirt(ClothingItem):
    def __init__(self, name, material, color, size, sleeve_length):
        super().__init__(name, material, color, size)
        self.sleeve_length = sleeve_length

    def __str__(self):
        return f"{super().__str__()} with {self.sleeve_length} sleeves"

    def get_sleeve_length(self):
        return self.sleeve_length


class TShirt(ClothingItem):
    def __init__(self, name, material, color, size, graphic):
        super().__init__(name, material, color, size)
        self.graphic = graphic

    def __str__(self):
        return f"{super().__str__()} with {self.graphic} graphic"

    def get_graphic(self):
        return self.graphic


class Glasses(ClothingItem):
    def __init__(self, name, material, color, size, lens_color):
        super().__init__(name, material, color, size)
        self.lens_color = lens_color

    def __str__(self):
        return f"{super().__str__()} with {self.lens_color} lenses"

    def get_lens_color(self):
        return self.lens_color


class Headband(ClothingItem):
    def __init__(self, name, material, color, size, width):
        super().__init__(name, material, color, size)
        self.width = width

    def __str__(self):
        return f"{super().__str__()} with {self.width} width"

    def get_width(self):
        return self.width


class Shawl(ClothingItem):
    def __init__(self, name, material, color, size, pattern):
        super().__init__(name, material, color, size)
        self.pattern = pattern

    def __str__(self):
        return f"{super().__str__()} with {self.pattern} pattern"

    def get_pattern(self):
        return self.pattern


class Sweatshirt(ClothingItem):
    def __init__(self, name, material, color, size, hooded):
        super().__init__(name, material, color, size)
        self.hooded = hooded

    def __str__(self):
        if self.hooded:
            return f"{super().__str__()} with a hood"
        else:
            return f"{super().__str__()} without a hood"

    def is_hooded(self):
        return self.hooded


class Sweater(ClothingItem):
    def __init__(self, name, material, color, size, pattern):
        super().__init__(name, material, color, size)
        self.pattern = pattern

    def __str__(self):
        return f"{super().__str__()} with {self.pattern} pattern"

    def get_pattern(self):
        return self.pattern
