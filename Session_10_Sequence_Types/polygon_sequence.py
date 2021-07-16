from polygon import *
import math
from functools import wraps,lru_cache
from collections import namedtuple

def validate_polygon_sequence(poly_class):
    """ This function validates the parameters passed to Polygon_Sequence Class """

    @wraps(poly_class)
    def inner(num_vertices,circumradius):
        """ This Decorator checks if the circumradius <= 0 or num_vertices <3  """

        if circumradius <= 0 or num_vertices <3 :
            return  "Error: Incorrect parameters for Class"
        else:
            return poly_class(num_vertices,circumradius)
    return inner

@validate_type(int)
@validate_polygon_sequence
class Polygon_sequence:

    def __init__(self,n,circumradius):
        """ This function initializes the number of polygons and circum radius. """

        self.n = n
        self.circumradius = circumradius

    @lru_cache(maxsize=2**10)
    def get_polygon(self,vertex , circumradius):
        """ This function returns the properties of the polygon such as vertex , circumradius, interior angle, edge length , apothem, area, perimeter as a named tuple.
        """

        polygon = Polygon(vertex, circumradius)
        interiorAngle = polygon.interiorAngle
        edgeLength  = polygon.edgeLength
        apothem = polygon.apothem
        area = polygon.area    
        perimeter = polygon.perimeter

        prop_names = ('vertex' , 'circumradius', 'interiorAngle', 'edgeLength' , 'apothem', 'area', 'perimeter')
        properties = namedtuple('Polygon', prop_names)

        # print(f'Calculating for Polygon with Vertex:{vertex} , CircumRadius: {circumradius}')

        return properties(vertex , circumradius, interiorAngle, edgeLength , apothem, area, perimeter)
            

    def max_efficiency(self):
        """ This function returns the maximum efficiency polygon.
            Here, a maximum efficiency polygon is one that has the highest area to perimeter ratio. 
        """
        
        ratios = []       
        
        for i in range(3, self.n+1):
            """ This function """

            p = self.get_polygon( i , self.circumradius)
            ratios.append(p.area/p.perimeter)
            # print(ratios)
        max_index = max(range(len(ratios)), key=ratios.__getitem__)
        # print(ratios)

        print(f'Polygon with {max_index+3} vertices has the Max Efficiency of {ratios[max_index]}')
    
    
    def __getitem__(self,vertex):
        """ This function returns the properties of the polygon whose vertices are as passed in the arguments. 
            It returns 'Not a polygon' message if the number of vertices is less than 3.
        """

        if isinstance(vertex,int)==False:
            return 'Error: Incorrect type for parameter '
        elif vertex <3 :
            return 'Error: This is not a polygon'
        else:
            return self.get_polygon( vertex , self.circumradius)
        
    
    def __repr__(self):
        """ This function gives the details of the Polygon Sequence object"""

        return f""" Contains {self.n} polygons with a circum radius of {self.circumradius} and vertices ranging from 3 to {self.n}"""
    
    def __len__(self):
        """ This function gives the length of the Polygon Sequence object """

        return self.n

