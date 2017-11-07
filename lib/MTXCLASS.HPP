// #pragma library("matrix.lib")
// compile with: /EHsc

#include <iostream>
#include "mtxerr.h"
// compile with: /EHsc
using namespace std;

class MatrixClass
{
public:

    // Constructors:
    MatrixClass(char *file_name);

    // Destructor:
    ~MatrixClass();

    // Methods:
    int   GetStatus();
    
    short GetNCores()          { return MATRIX_GetNCores(hMatrix); }
    short SetCore(short iCore) { return MATRIX_SetCore(hMatrix, iCore); }
    
    long  GetNRows()     { return MATRIX_GetNRows(hMatrix);  }
    long  GetNCols()     { return MATRIX_GetNCols(hMatrix); }

    long  GetBaseNRows() { return MATRIX_GetBaseNRows(hMatrix);  }
    long  GetBaseNCols() { return MATRIX_GetBaseNCols(hMatrix); }

    short GetElement(long idRow, long idCol, DATA_TYPE Type, void *p);
    short GetVector(long idRow, MATRIX_DIM dim, DATA_TYPE Type, void *p);
    short GetBaseVector(long index, MATRIX_DIM dim, DATA_TYPE Type, void *p);


    void  ToString(char *s)  { sprintf(s,"<matrix cores: %d rows: %d columns: %d>",this->GetNCores(),this->GetNRows(),this->GetNCols()); }    

    friend ostream& operator<< ( ostream& os, MatrixClass& m );

    // Properties:

private:

    // handle to the private C data structure.
    MATRIX hMatrix;

};


