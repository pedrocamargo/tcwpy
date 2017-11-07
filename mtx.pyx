
cdef extern from "lib/MTXCLASS.HPP" namespace 'std':
    cdef cppclass MatrixClass:
        MatrixClass(string)
        # int   GetStatus()



# cdef extern from "lib/CaliperMTX.h":
#     InitMatDLL(int)
#     MATRIX_LoadFromFile(filename, bo_ol)
#     MATRIX_GetBaseNRows(MATRIX)
#
#
# cdef test(mat_name):
#     InitMatDLL(0)
#     # mat = MATRIX_LoadFromFile(mat_name, True)
#     # print MATRIX_GetBaseNRows(mat)