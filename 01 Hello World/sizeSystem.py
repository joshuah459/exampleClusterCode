

from mpi4py import MPI
import numpy as np
import random

name = MPI.Get_processor_name()
comm = MPI.COMM_WORLD
#size = 10
proc = comm.Get_size()
size = comm.Get_size()
rank = comm.Get_rank()


if rank==0:
        mat1=np.array([[random.randint(0,10) for i in range(size)] for j in range(size)])
        print(mat1)
        mat2=np.array([[random.randint(0,10) for i in range(size)] for j in range(size)])
        print(mat2)
        mat3=np.array([[0 for i in range(size)] for j in range(size)])

        for r in range(0,size):
                for c in range(0,size):
                        mat3[r][c]=np.dot(mat1[:,r],mat2[c])
        print (mat3)

#develop system to manage sizing for scatter
#i.e scatters needs appropiate amount of data compared to number of processors

reps = size/4
rem = size%4


print 'name', name, 'reps',reps,'rem',rem



for r in range(0,size):
        if rank == 0:
                row=np.ascontiguousarray(mat1[:,r])
        else:
                row = np.empty(size, dtype='i')
        comm.Bcast(row, root=0)

	#for loop scattering 
	#for x in range(0,reps):
        if rank ==0:
               	col = mat2
        else:
               	col = np.empty(size, dtype='i')

        col = comm.scatter(col,root=0)

        col = np.dot(row,col)

        print 'rank',rank,'result',col

        dot=comm.gather(col,root=0)

        if rank==0:
                print dot




MPI.Finalize()
