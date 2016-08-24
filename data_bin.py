# -------------------------------------------------------------------------------
# Name:        Importing TransCad Binary files into Python (Numpy) arrays
# Purpose:
#
# Author:      Pedro Camargo
#
# Created:     15/05/2014
# Copyright:   (c) pcamargo 2014
# Licence:     See LICENSE.TXT
#-------------------------------------------------------------------------------

import os
import numpy as np
import numpy.ma as ma
import time

# A TCW bin has both data and data dictionary
class DataBin:
    def __init__(self):
        self.datafile = "No file loaded yet"
        self.dictfile = "No file loaded yet"
        self.dictionary = None
        self._dict2 = {}
        self.data = None

    def load(self, binfile):
        self.datafile = binfile
        self.dictfile = binfile[0:len(binfile) - 3] + "dcb"
        self.builds_dt()
        self.loads_data()

    def builds_dt(self):
        b = True
        try:
            w = open(self.dictfile, 'rb')

        except:
            b = False
            print 'Dictionary file missing'

        if b == True:
            try:
                prev = ""
                prev_end = ""

                q = w.readline()
                q = w.readline().rstrip().split()[0]
                size = int(q)
                q = w.readline()
                dt = []
                to_sort = []
                all_sizes = []
                while len(q) > 0:
                    a = q.rstrip().split(',')
                    field_name = a[0]
                    field_name = field_name[1:len(field_name) - 1]
                    field_type = a[1]

                    endianess = "<"
                    if field_type == "I" or field_type == "S":
                        field_type = "i"
                    if field_type == "R" or field_type == "F":
                        field_type = "f"

                    if field_type == "C":
                        field_type = "S"
                        endianess = ">"

                    if prev == "S" and prev_end == ">":
                        endianess = "<"

                    field_length = a[3]
                    dt.append((field_name, endianess + field_type + field_length))
                    q = w.readline()

                    prev = field_type
                    prev_end = endianess
                    to_sort.append(int(a[2]))

                    self._dict2[field_name] = field_type + field_length
                    size -= int(field_length)
                    all_sizes.append(int(field_length))
                dt2 = []

                # The fields need to be sorted in order to allow for correct data loading
                [dt2.append(d) for y, d in sorted(zip(to_sort, dt))]

                # IF Binnary file is malformed, with empty spaces in between fields
                p = 1
                if size > 0:
                    pos = []
                    [pos.append(d) for y, d in sorted(zip(to_sort, to_sort))]
                    s = []
                    [s.append(d) for y, d in sorted(zip(to_sort, all_sizes))]
                    for i in xrange(1, len(pos)):
                        if pos[i] <> pos[i - 1] + s[i - 1]:
                            dt.append(('Malformed_fieldTcW' + str(p),
                                       'i' + str(pos[i] - pos[i - 1] - s[i - 1])))  #An imaginary field
                            to_sort.append(pos[i - 1] + s[i - 1])  #in the imaginary position
                            self._dict2['Malformed_fieldTcW' + str(p)] = 'i' + str(pos[i] - pos[i - 1] - s[i - 1])
                            p += 1

                    dt2 = []
                    # The fields need to be sorted in order to allow for correct data loading
                    [dt2.append(d) for y, d in sorted(zip(to_sort, dt))]

                self.dictionary = dt2
            except:
                print 'Dictionary file with structural problems'

    def loads_data(self):
        f = open(self.datafile, 'rb')
        self.data = np.fromfile(f, dtype=self.dictionary)

        for name in self.data.dtype.names:
            myarray = self.data[name]
            tp = self._dict2[name]
            lim = 0
            if tp == 'i1':
                lim = -1
            if tp == 'i2':
                lim = -32767
            if tp == 'i4':
                lim = -2147483647
            if tp == 'f4':
                lim = -3.40282e+38
            if tp == 'f8':
                lim = -1.79769e+308
            if lim < 0:
                myarray[myarray <= lim] = 0

    def info(self):
        print "Binnary Source: ", self.datafile
        print "   Data Type:", self.dictionary
        try:
            print "   Number of records: ", self.data.shape[0]
        except:
            print "   No valid data loaded"
            
    def savetxt(self, filename):
        with open(filename, 'w') as f:
            for name in self.data.dtype.names:
                f.write(name + ',')  # or write(repr(name)) to keep the quote marks
            f.write('\n')
            for row in self.data:
                for el in row:
                    f.write(repr(el) + ',')
                f.write('\n')
            f.flush()
