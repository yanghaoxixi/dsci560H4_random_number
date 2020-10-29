import matplotlib.pyplot as plt
from a import x 
from b import y

#print('list of random number x: ')
#print(x)
#print('list of random number y: ')
#print(y)

plt.scatter(x,y,s=0.3)

plt.title('Question_1_Visualization')
plt.xlabel('x index from a')
plt.ylabel('y index from b')
plt.show()



