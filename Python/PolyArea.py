class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width *2) + (self.height *2)
    
    def get_diagonal(self):
        return (( (self.width **2) + (self.height **2) ) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            ret_string = ""
            for line in range(self.height):
                ret_string += "*" * self.width + "\n"
            return ret_string
                    
    
    def get_amount_inside(self, shape):
        fitted_width = self.width // shape.width
        fitted_height = self.height // shape.height
        return fitted_height * fitted_width
    
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def __str__(self):
        return "Square(side=" + str(self.width) + ")"
    
    def set_width(self, side):
        self.set_side(side)
        
    def set_height(self, side):
        self.set_side(side)
        
    def set_side(self, side):
        self.width = side
        self.height = side
    

lemon = Square(5)
print(lemon)
print(Rectangle(50, 122).get_picture())