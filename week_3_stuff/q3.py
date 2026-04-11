# In three-dimensional space, a Platonic solid is a regular, convex polyhedron. There are five Platonic solids.

# Using string format to write a program that produces the following output where
# - the 1st column using right alignment and 10 spaces
# - the 2nd column using center alignment and 30 spaces
# - the 3rd column using left alignment and 10 spaces

# For example:
# Result

#      Faces             Name             Vertices  
#          4         Tetrahedron          4         
#          6             Cube             8         
#          8          Octahedron          6         
#         12         Dodecahedron         20        
#         20         Icosahedron          12        

headers = ["Faces","Name","Vertices"]
faces = [4, 6, 8, 12, 20]
name = ["Tetrahedron", "Cube", "Octahedron", "Dodecahedron", "Icosahedron"]
verticies = [4, 8, 6, 20, 12]
print(f"|{headers[0]:<10}|{headers[1]:^30}|{headers[2]:>10}|")
for i in range(len(faces)):
    print(f"|{faces[i]:<10}|{name[i]:^30}|{verticies[i]:>10}|")

# |Faces     |             Name             |  Vertices|
# |4         |         Tetrahedron          |         4|
# |6         |             Cube             |         8|
# |8         |          Octahedron          |         6|
# |12        |         Dodecahedron         |        20|
# |20        |         Icosahedron          |        12|