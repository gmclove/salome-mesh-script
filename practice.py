# Create an instance of smeshBuilder:
from salome.smesh import smeshBuilder
smesh = smeshBuilder.New( salome.myStudy )

Create a mesh object:
mesh = smesh.Mesh( geometry )

# Create and assign algorithms by calling corresponding methods of the mesh. If a sub-shape is provided as an argument, a sub-mesh is implicitly created on this sub-shape:
regular1D = mesh.Segment()
mefisto   = mesh.Triangle( smeshBuilder.MEFISTO )
# use other triangle algorithm on a face -- a sub-mesh appears in the mesh
netgen    = mesh.Triangle( smeshBuilder.NETGEN_1D2D, face )

# Create and assign hypotheses by calling corresponding methods of algorithms:
segLen10 = regular1D.LocalLength( 10. )
maxArea  = mefisto.MaxElementArea( 100. )
netgen.SetMaxSize( 20. )
netgen.SetFineness( smeshBuilder.VeryCoarse )

# Compute the mesh (generate mesh nodes and elements):
mesh.Compute()
