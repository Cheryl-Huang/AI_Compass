size=21
num_kernel=10
pool=2
size1=252-size+1
size1=int(size1/pool)
size2=size1-size+1
size2=int(size2/pool)
print(size2)
total=size2*size2*num_kernel
print(total)