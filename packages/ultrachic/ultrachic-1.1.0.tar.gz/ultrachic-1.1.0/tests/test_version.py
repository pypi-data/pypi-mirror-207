import pytest
import os
import re

def test_version():
    import ultrachic
    
    # Python
    pyversion = ultrachic.UltraVersion.ULTRAVERSION
    print('pyversion:   {}'.format(pyversion))
    
    # c
    cversion  = None
    with open(os.path.join('..','src_c','ultraversion.h'),'r') as f:
        lines = f.readlines()
        for line in lines:
            # format of the line: "#define ULTRAVERSION {1,2,3}"
            m = re.match('#define ULTRAVERSION {([0-9]*),([0-9]*),([0-9]*)}', line)
            if m:
                cversion = (int(m[1]),int(m[2]),int(m[3]))
                break
    print('cversion:    {}'.format(cversion))
    
    # compare
    assert pyversion==cversion
