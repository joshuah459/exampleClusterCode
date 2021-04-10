from mpi4py import MPI
import numpy as np
import random


comm = MPI.COMM_WORLD
size= 60
prc= comm.Get_size()
rank = comm.Get_rank()

if rank==0:
        mat1=np.array([[random.randint(0,10) for i in range(size)] for j in range(size)])
        #print(mat1)
        mat2=np.array([[random.randint(0,10) for i in range(size)] for j in range(size)])
        #print(mat2)
        #mat3=np.array([[0 for i in range(size)] for j in range(size)])

        #for r in range(0,size):
                #for c in range(0,size):
                        #mat3[r][c]=np.dot(mat1[:,r],mat2[c])
        #print (mat3)
	sum = np.zeros(size)
	#dot=np.zeros(size/prc)
	print 'size', size, 'size/4', size/prc
dot=np.zeros(size/prc)


#loop going through all of the matrix multiplication
for y  in range(0,size):

	#broadcasting of matrix 1s columns
	if rank == 0:
        	row=np.ascontiguousarray(mat1[:,y])
	else:
        	row=np.empty(size, dtype='i')

	comm.Bcast(row, root=0)

	result=0
	#print 'row',row

	#loop for spliting array up into smaller pieces,...
	#...scattering of smaller arrays and sending back result, summation of results
	for x in range(0,size):
		if rank ==0:
        		colSub = np.split(mat2[x],size/prc)
        		#print 'colSub', colSub

		#loop for scattering arrays based on the size over the processors available...
		#...then multiplication of row and col to then reduce part of the array
		for r in range(0,size/prc):

		#print 'colSub[r]',r,colSub[r]
			if rank ==0:
				col = colSub[r]
			else:
				col = np.empty(prc, dtype='i')

			col = comm.scatter(col,root=0)
			#print 'rank',rank,'col',col
			#printt 'rank',rank,'row',row[rank+prc*r]
			result=row[rank+prc*r]*col
			#print 'rank',rank,'result',result
			dot[r]=comm.reduce(result,root=0)
        		#if rank == 0 and r == (size/prc-1):
				#print 'dot',dot

		#sums up dot which contains reduced result from smaller arrays 
		if rank == 0:
			sum[x] = np.sum(dot)

		#if rank == 0 and x == size-1:
			#print 'sum', sum
MPI.Finalize()
