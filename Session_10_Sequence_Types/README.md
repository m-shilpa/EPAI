# Sequence Types

## Assignment

1. A regular strictly convex polygon is a polygon that has the following characteristics:
    * All interior angles are less than 180
    * All sides have equal length

2. For a regular strictly convex polygon with vertices n and circumradius r:
    * interiorAngle = (n−2) * (180/n)
    * edgeLength, s = 2 * R * sin(π/n) 
    * apothem, a = R * cos(π/n)
    * area = (1/2) * n * a
    * perimeter = n * s
3. **Objective 1**:

     Create a Polygon Class:
     
     1. Where initializer takes in:
        * number of edges/vertices
        * circumradius
      2. That can provide these properties:
          * edges
          * vertices
          * interior angle
          * edge length
          * apothem
          * area
          * perimeter
      3. That has these functionalities:
          * a proper __repr__ function
          * implements equality (==) based on # vertices and circumradius (__eq__)
          * implements > based on number of vertices only (__gt__) 
4. **Objective 2**:
    Implement a Custom Polygon sequence type:
    
    1. Where initializer takes in:
        * number of vertices for largest polygon in the sequence
        * common circumradius for all polygons
        * that can provide these properties:
        * max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
     2. that has these functionalities:
        * functions as a sequence type (__getitem__)
        * supports the len() function (__len__)
        * has a proper representation (__repr__)


## Classes and Functions

## **Polygon Class:**

This class provides the properties of a polygon such as vertex, circum radius, interior angle, edge length , apothem, area and perimeter

### Member Functions:

**__init__(n_vertices,circumradius):**

1. This is a constructor which is called for object creation.
2. This function expects the vertex and circum radius as argument.
3. It intializes the vertex, circum radius. 
4. It calculates the interior angle, edge length , apothem, area and perimeter using the respective functions and stores them.

**calc_interiorAngle():**

This function calculates the Interior Angle of the polygon.

**calc_edgeLength():**

This function calculates the Edge Length of the polygon.

**calc_apothem():**

This function calculates the Apothem of the polygon.

**calc_area()**    

This function calculates the Area of the polygon.

**calc_perimeter()**

This function calculates the Perimeter of the polygon.

**__eq__()**

1. This function checks if the polygon is equal to the other polygon or not 
2. If the vertices and circum radius of this polygon is equal to the other then it returns True else returns False.

**__gt__():**

1. This function checks if the polygon is greater than the other polygon or not.
2. If this polygon has a larger number of vertices than the other polygon then this function return True else return False

**__repr__():**

A function to gives the details of the polygon object. 

## **Polygon Sequence Class:**

This class is used to get a sequence of polygons.

### Member Functions:

**__init__(self,n,circumradius):**
1. This is a constructor which is called for object creation.
2. This function expects n (no. of polygons) and one circum radius of all the n polygons as argument.
3. It intializes the n, circum radius 

**get_polygon(self,vertex , circumradius):**

1. This function takes as arguments the values for the vertex and circum radius of the polygon. 
2. It returns the properties of the polygon such as vertex , circum radius, interior angle, edge length , apothem, area, perimeter as a named tuple.
3. lru_cache is as decorator for this function to prevent re-calculation of the polygon properties.

**max_efficiency(self):**

1. This function returns the maximum efficiency polygon.
2. Here, a maximum efficiency polygon is one that has the highest area to perimeter ratio. 

**__getitem__(self,vertex):**

1. This function is called when we access an item of the object using the index.
2. The index which is passed as argument is taken as the vertex of the polygon.
3. The function returns a named tuple containing the properties of the polygon with given vertex and circum radius as originally initialized during object creation. 

**__repr__(self)**:

A function to gives the details of the Polygon Sequence object.

**__len__(self)**

1. This function gives the length of the Polygon Sequence object.
2. Here, length is the parameter n that was passed while object creation.

## **Decorators**

**@validate_type(int)**

1. This is a decorator factory.
2. It takes the type as argument.
3. It used this type provided as argument and checks if all the arguments passed to a function is of this type.
4. If only this condition is satified, the function is executed else an error message is returned.

**@validate_params**

This decorator is used to validate the parameters passed to the Polygon Class during object creation and it checks the following:
1. Checks if number of vertices/polygons provided is less than 3 or not. 
2. Checks if the Circum Radius provided is less than 0 or not.

If both the above conditions are satisfied, it throws an Error message  else it proceeds to creating the Polygon object





