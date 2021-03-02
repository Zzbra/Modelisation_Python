import os
stream = os.popen('python3 schur_csp.py 3 25 -solver=[choco,v] | python3 test.py')
output = stream.read()
print(output)
