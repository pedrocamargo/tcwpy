# -------------------------------------------------------------------------------
# Name:        Importing TransCad Matrices into Python (Numpy/Scipy) arrays
# Purpose:
#
# Author:      Pedro Camargo
#
# Created:     15/05/2014
# Copyright:   (c) pcamargo 2016
# Licence:     See LICENSE.TXT
# -------------------------------------------------------------------------------

import numpy as np
from ctypes import *
import ctypes


class TCWMtx:
    def __init__(self):
        self.data = None
        self.rows = -1
        self.columns = -1
        self.type = -1
        self.cores = -1
        self.matrix = {}
        self.RIndex = -1  #Dictionary with all indices for the rows
        self.CIndex = -1  #Dictionary with all indices for the columns
        self.datafile = 'No file loaded yet'
        self.RHash = False
        self.CHash = False
        #        self.RIndex= {}     #Dictionary with all indices for the rows
        #        self.CIndex= {}     #Dictionary with all indices for the columns

        self.indexcount = -1  #Tuple with the number of indices for each dimension

    def info(self):
        print 'Number of matrix Cores: ', self.cores
        print 'Matrix Cores: ', self.matrix.keys()
        print 'Number of rows: ', self.rows
        print 'Number of columns: ', self.columns
        print 'Number of indices for rows: ', self.indexcount[0]
        print 'Number of indices for columns: ', self.indexcount[1]

    def load(self, filename, justcores=None, verbose=False, null_is_zero=True):
        # We load the DLL and initiate it
        tcw = cdll.LoadLibrary('C:\\Program Files\\TransCAD 6.0\\CaliperMtx.dll')
        
        initdll = ctypes.c_short(0)
        idll = ctypes.pointer(initdll)
        tcw.InitMatDLL(idll)

        mat = tcw.MATRIX_LoadFromFile(filename, True)

        self.rows = tcw.MATRIX_GetBaseNRows(mat)
        self.columns = tcw.MATRIX_GetBaseNCols(mat)
        self.type = tcw.MATRIX_GetDataType(mat)
        self.indexcount = (tcw.MATRIX_GetNIndices(mat, 0), tcw.MATRIX_GetNIndices(mat, 1))
        self.cores = tcw.MATRIX_GetNCores(mat)
        self.datafile = filename

        v = (self.rows * c_long)()
        tcw.MATRIX_GetIDs(mat, 0, v)
        self.RIndex = np.zeros(self.rows, np.int64)
        self.RIndex[:] = v[:]

        i = np.max(self.RIndex) + 1
        self.RHash = np.zeros(i, np.int64)
        self.RHash[self.RIndex] = np.arange(self.rows)

        v = (self.columns * c_long)()
        tcw.MATRIX_GetIDs(mat, 1, v)
        self.CIndex = np.zeros(self.columns, np.int64)
        self.CIndex[:] = v[:]

        i = np.max(self.CIndex) + 1
        self.CHash = np.zeros(i, np.int64)
        self.CHash[self.CIndex] = np.arange(self.columns)

#        #Reads all the indices for rows and put them in the dictionary
#        for i in range(self.indexcount[0]):
#            tcw.MATRIX_SetIndex(mat, 0, i)
#            v = (tcw.MATRIX_GetNRows(mat) * c_long)()
#            tcw.MATRIX_GetIDs(mat, 0, v)
#            t = np.zeros(tcw.MATRIX_GetNRows(mat), np.int64)
#            t[:] = v[:]
#            self.RIndex[i] = t.copy()
#
#        #Do the same for columns
#        for i in range(self.indexcount[1]):
#            f = tcw.MATRIX_SetIndex(mat, 1, i)
#            v = (tcw.MATRIX_GetNCols(mat) * c_long)()
#            tcw.MATRIX_GetIDs(mat, 1, v)
#            t = np.zeros(tcw.MATRIX_GetNCols(mat), np.int64)
#            t[:] = v[:]
#            self.CIndex[i] = t.copy()

        if justcores is not None:
            if not isinstance(justcores, list):
                justcores = [justcores]
        else:
            justcores = []
            for i in range(self.cores):
                tcw.MATRIX_SetCore(mat, i)
                nameC = ctypes.create_string_buffer(50)
                tcw.MATRIX_GetLabel(mat, i, nameC)
                nameC = repr(nameC.value)
                nameC = nameC[1:len(nameC) - 1]
                justcores.append(nameC)

        if verbose:
            print "Matrix has ", self.cores, " cores.  Loading " + str(len(justcores)) + " core(s)"

        for C in justcores:
            for k in range(self.cores):
                tcw.MATRIX_SetCore(mat, k)
                nameC = ctypes.create_string_buffer(50)
                tcw.MATRIX_GetLabel(mat, k, nameC)
                nameC = repr(nameC.value)
                nameC = nameC[1:len(nameC) - 1]

                if C == nameC:
                    if verbose:
                        print "   Loading core: ", nameC  # If verbose, we list the matrices being loaded
                    # Define the data type Numpy will have according to the data type of the matrix in question
                    dt = np.float64
                    v = (self.columns * c_double)()
                    if self.type == 1:
                        dt = np.int16
                        v = (self.columns * c_long)()
                    if self.type == 2:
                        dt = np.int64
                        v = (self.columns * c_longlong)()
                    if self.type == 3:
                        dt = np.float64
                        v = (self.columns * c_float)()

                    # Instantiate the matrix
                    self.matrix[nameC] = np.zeros((self.rows, self.columns), dtype=dt)
                    replace_by = np.NaN
                    if null_is_zero:
                        replace_by = 0
                    # Read matrix and puts in the numpy array
                    for i in range(self.rows):
                        # tcw.MATRIX_GetBaseVector.restype = None
                        tcw.MATRIX_GetBaseVector(mat, i, 0, self.type, v)
                        self.matrix[nameC][i, :] = v[:]
                    if self.type == 4:
                        self.matrix[nameC][self.matrix[nameC] <= -1.79769e+308] = replace_by
                    if self.type == 3:
                        self.matrix[nameC][self.matrix[nameC] <= -3.40282e+38] = replace_by
                    if self.type == 2:
                        self.matrix[nameC][self.matrix[nameC] <= -2147483647] = replace_by
                    if self.type == 1:
                        self.matrix[nameC][self.matrix[nameC] <= -32767] = replace_by

        #            raise NameError('Not possible to open file. TranCad returned '+ str(tc_value))
        tcw.MATRIX_CloseFile(mat)
        tcw.MATRIX_Done(mat)

    def export(self, core, name, all_cells=False):
        m = self.matrix[core]
        O = open(name, 'w')
        print >> O, 'O,D,VALUE'
        for i, k in enumerate(self.RIndex):
            for j, l in enumerate(self.CIndex):
                if m[i, j] > 0 or all_cells:
                    print >> O, k, ',', l, ',', m[i, j]
        O.flush()
        O.close()

    def value(self, core, i, j):
        return self.matrix[core][self.RHash[i], self.CHash[j]]

    def changevalue(self, core, i, j, new_value):
        self.matrix[core][self.RHash[i], self.CHash[j]] = new_value
