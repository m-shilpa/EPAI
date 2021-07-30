# **Iterables II:**

## **Assignment:**

The starting point for this project is the Polygon class and the Polygons sequence type we created in the <a href="https://github.com/m-shilpa/EPAI/tree/main/Session_10_Sequence_Types">here</a>.

### **Goal 1:**
Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").

### **Goal 2:**
Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

You'll need to implement both an iterable, and an iterator.

## Classes and Functions

<a href="https://colab.research.google.com/drive/1QhdOQehsCBEvySigZB2mKIX8abM8gjlC?usp=sharing"><b>Colab Link</b></a>


### **Polygon Class:**

This class provides the properties of a polygon such as vertex, circum radius, interior angle, edge length , apothem, area and perimeter. All the properties are calculated only once for an object. They are stored after being calculated for the first time, then they are re-used when called more than once.

### **Polygon Sequence Class:**

This class is used to get a sequence of polygons.

### **PolygonIter Class:**

This Class is an iterator which helps to iter over the objects in the Polygon Sequence and calculate them on the fly instead of pre-calculating them.
