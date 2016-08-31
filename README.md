#### tcwpy
Library for reading TransCad files into Numpy arrays
   - Required TransCad license to read matrices
   - User needs to manually change the path to the TransCad matrix dll on disk for this library to work
   - Last tested with Transcad 6, Release 2


NOT RELATED IN ANY WAY WITH CALIPER CORPORATION



********
Usage example (Matrix)
********

#### Instatiating a matrix

from tcwpy import TCWMtx

matrix = 'path+matrix_name.mtx'

cores_to_load = ['core1', 'core2']

mymatrix = TCWMtx()

#### Loading all matrix cores
mymatrix.load(matrix, verbose=True) #### verbose option prints on the screen all loading steps happening

#### Loading only a few cores
mymatrix.load(matrix,  justcores=cores_to_load, verbose=True)

#### Printing names of all loaded cores
for q in mymatrix.matrix.keys():

    print q

#### exports matrix to csv file
mymatrix.export(core_name, file_path_and_name, all_cells=False)

#### Since the matrix has indices that are not necessarily 0, 1, 2, 3, ...
#### accessing the matrix as mymatrix.matrix[core][i,j] does not work
#### one needs to access through

mymatrix.value(core, i, j)

#### The matrix indices can be accesed through
matrix.RHash[:] #### for rows

matrix.CHash[:] #### for columns

  

********
Usage example (binary)
********

from tcwpy import DataBintx

f = DataBin()

f.load(path+name_of_the_file.bin)

#### prints all columns in the bin
for name in a.dtype.names:
    print name

#### prints information about the data table
f.info()

#### Saves data table to a csv
f.savetxt(output_file_name.csv)


