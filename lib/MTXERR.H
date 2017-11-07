
#if !defined(MTXERR_H)
#define MTXERR_H

// tc status codes

// user errors
#define TC_DBOPEN    -1    // database not opened
#define TC_INVSET    -2    // invalid set
#define TC_INVREC    -3    // invalid record
#define TC_INVDB     -4    // invalid database
#define TC_INVFLD    -5    // invalid field name
#define TC_INVADDR   -6    // invalid db_address
#define TC_NOCR      -7    // no current record
#define TC_NOCO      -8    // set has no current owner
#define TC_NOCM      -9    // set has no current member
#define TC_KEYREQD   -10   // key value required
#define TC_BADTYPE   -11   // invalid lock type
#define TC_HASMEM    -12   // record is owner of non-empty set(s)
#define TC_ISMEM     -13   // record is member of set(s)
#define TC_ISOWNED   -14   // member already owned
#define TC_ISCOMKEY  -15   // field is a compound key
#define TC_NOTCON    -16   // record not connected to set
#define TC_NOTKEY    -17   // field is not a valid key
#define TC_INVOWN    -18   // record not legal owner of set
#define TC_INVMEM    -19   // record not legal member of set
#define TC_SETPAGES  -20   // error in d_setpages (database open or bad param)
#define TC_INCOMPAT  -21   // incompatible dictionary file
#define TC_DELSYS    -22   // illegal attempt to delete system record
#define TC_NOTFREE   -23   // attempt to locked previously locked rec or set
#define TC_NOTLOCKED -24   // attempt to access unlocked record or set
#define TC_TRANSID   -25   // transaction id not be supplied
#define TC_TRACTIVE  -26   // transaction already active
#define TC_TRNOTACT  -27   // transaction not currently active
#define TC_TRLOCKS   -28   // transaction cannot begin due to locked files
#define TC_TRFREE    -29   // attempt to free a lock inside a transaction
#define TC_TRCHANGES -30   // too many pages changed within transaction
#define TC_NOTRANS   -31   // attempted update outside of transaction
#define TC_EXCLUSIVE -32   // functions requires exclusive db access
#define TC_STATIC    -33   // Attempted to write lock a static file
#define TC_USERID    -34   // No user id exists
#define TC_NAMELEN   -35   // database file/path name too long
#define TC_RENAME    -36   // invalid file number was passed to d_renfile
#define TC_NOTOPTKEY -37   // field is not an optional key
#define TC_BADFIELD  -38   // field not defined in current record type
#define TC_COMKEY    -39   // record/field has/in a compound key
#define TC_INVNUM    -40   // invalid record or set number
#define TC_TIMESTAMP -41   // record or set not timestamped
#define TC_CORRUPT   -42   // corrupted copy protected file 

#define TC_FPERROR   -950  // floating point error trap

// system errors
#define TC_NOSPACE   -900  // no more space on file
#define TC_SYSERR    -901  // system error
#define TC_FAULT     -902  // page fault -- changed during usage
#define TC_NOWORK    -903  // no working file set in dio
#define TC_NOMEMORY  -904  // unable to allocate sufficient memory
#define TC_NOFILE    -905  // unable to locate a file
#define TC_DBLACCESS -906  // unable to access db lock file
#define TC_DBLERR    -907  // db lock file open/access error
#define TC_BADLOCKS  -908  // inconsistent database locks
#define TC_RECLIMIT  -909  // file record limit reached
#define TC_KEYERR    -910  // key file inconsistency detected
#define TC_USERLIMIT -911  // Max concurrent user limit reached
#define TC_FSEEK     -912  // Bad seek on database file
#define TC_INVFILE   -913  // Invalid file specified
#define TC_READ      -914  // Bad read on database/overflow file
#define TC_NETSYNC   -915  // Network synchronization error
#define TC_DEBUG     -916  // Debugging check interrupt
#define TC_NETERR    -917  // Network communications error
#define TC_RECOVERY  -918  // Auto-recovery is in process
#define TC_WRITE     -919  // Bad write on database/overflow file
#define TC_NOLOCKMGR -920  // Unable to open lockmgr session
#define TC_DUPUSERID -921  // DBUSERID is already used by another user
#define TC_LMBUSY    -922  // The lock manager is busy
#define TC_NOROOM    -933  // port/field not wide enough to show all text
#define TC_INVINPUT  -934  // invalid input
#define TC_NODEVICE  -935  // device off-line or otherwise timed-out

// function statuses
#define TC_OKAY      0     // normal return, okay
#define TC_EOS       1     // end of set
#define TC_NOTFOUND  2     // record not found
#define TC_DUPLICATE 3     // duplicate key
#define TC_KEYSEQ    4     // field type used out of sequence in d_keynext
#define TC_UNAVAIL   5     // database file currently unavailable
#define TC_DELETED   6     // record/set deleted since last accessed
#define TC_UPDATED   7     // record/set updated since last accessed
#define TC_LOCKED    8     // current record's lock bit is set
#define TC_UNLOCKED  9     // current record's lock bit is clear

#define TC_NOUNDO    10    // no more undo records in file
#define TC_ESCAPED   11    // input function returns ESC
#define TC_RESIZE    12    // editor needs re-sizing
#define TC_MISSING   13    // Missing value
#define TC_INTERRUPT 14    // Interrupted operations
#define TC_MOVED     15    // Moved to a different location


#endif
