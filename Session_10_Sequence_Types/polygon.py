import math
from functools import wraps

def validate_type(d_type):
    def validate(fn):
        @wraps(fn)
        def inner(*args,**kwargs):
            for i in args:
                if isinstance(i, d_type) == False:
                    return  "Error: Incorrect Parameter types"
            return fn(*args,**kwargs)
        return inner
    return validate
  
  def validate_polygon(poly_class):
    """ Function to validate the parameters passed to the Polygon Class  """

    @wraps(poly_class)
    def inner(num_vertices,circumradius):
        """ Decorator that checks:
            1. If the Number of Vertices passed to the Class to more than 3
            2. IF the Curcum Radius is more than 0  
        """

        if circumradius <= 0 :
            return "Error: Cannot create polygon.Circum Radius is too small"
        elif num_vertices < 3:
            return "Error: Cannot create polygon.No. of vertices is too small"
        else:
            return poly_class(num_vertices,circumradius)
    return inner

@validate_type(int)
@validate_polygon
class Polygon:
    """ A Polygon Class """

    def __init__(self,n_vertices,circumradius):
        """ Initialize the vertices, circumradius, interiorAngle, edgeLength , apothem, area, perimeter. """

        self.n_vertices = n_vertices
        self.circumradius = circumradius
        self.interiorAngle = self.calc_interiorAngle()
        self.edgeLength  = self.calc_edgeLength() 
        self.apothem = self.calc_apothem()       
        self.area = self.calc_area()    
        self.perimeter = self.calc_perimeter()
    
    def calc_interiorAngle(self):
        """ This function calculates the Interior Angle of the polygon. """
        
        return (self.n_vertices - 2) * (180/self.n_vertices)
    
    def calc_edgeLength(self):
        """ This function calculates the Edge Length of the polygon. """

        return 2*self.circumradius * math.sin(math.pi/self.n_vertices)

    def calc_apothem(self):
        """ This function calculates the Apothem of the polygon. """

        return self.circumradius * math.cos(math.pi * self.n_vertices)
    
    def calc_area(self):
        """ This function calculates the Area of the polygon. """

        s = self.calc_edgeLength() 
        a = self.calc_apothem()
        return (1/2) * self.n_vertices * s * a
    
    def calc_perimeter(self):
        """ This function calculates the Perimeter of the polygon. """

        s = self.calc_edgeLength() 
        return self.n_vertices * s

    def __eq__(self,other):
        """ This function checks if the polygon is equal to the other polygon or not 
            If the vertices and circum radius of this polygon is equal to the other then it returns True else returns False.
        """

        return self.n_vertices == other.n_vertices and self.circumradius == other.circumradius

    def __gt__(self,other):
        """ This function checks if the polygon is greater than the other polygon or not.
            If this polygon has a larger number of vertices than the other polygon then this function return True else return False
        """

        return self.n_vertices > other.n_vertices
    
    def __repr__(self):
        """ A function to gives the details of the polygon object. """

        return f""" A Polygon with the following properties: \n No. of Vertices: {self.n_vertices} \n CircumRadius:{self.circumradius} \n Interior Angle: {self.interiorAngle} \n Edge Length: {self.edgeLength}  \n Apothem: {self.apothem}\n Area: {self.area}\n Perimeter: {self.perimeter} """
  
  
