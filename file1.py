import numpy as np
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print("Original array\n",sampleArray)
sortby2=sampleArray[:,sampleArray[1].argsort()]
print("sorted by 2nd row\n",sortby2)
sortby2=sampleArray[sampleArray[:,1].argsort()]
print("sorted by 2nd coloum\n",sortby2)