def timespec_diff( start, stop ):
'''
Calculates the time difference of two 'struct timespec' based objects.

The function returns the time difference between two dictionaries which are
structured like the 'struct timespec' type of the C library <sys/time.h>.
A time dict has the following structure {'tv_sec', tv_nsec}.

Parameters
----------

start : dict
    start time with structure {'tv_sec', tv_nsec}

stop : dict
    stop time with structure {'tv_sec', tv_nsec}

'''
    result = {}
    if( ( stop['tv_nsec'] - start['tv_nsec'] ) < 0 ):
        result['tv_sec']  = stop['tv_sec'] - start['tv_sec'] - 1
        result['tv_nsec']  = stop['tv_nsec'] - start['tv_nsec'] + 1000000000
    else:
        result['tv_sec']  = stop['tv_sec'] - start['tv_sec']
        result['tv_nsec']  = stop['tv_nsec'] - start['tv_nsec']

    return result

