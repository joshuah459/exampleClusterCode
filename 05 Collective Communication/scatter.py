from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size= comm.Get_size()
rank = comm.Get_rank()

name=MPI.Get_processor_name()


if rank ==0:
        data = np.array([i for i in range(size)])
        print data
else:
        data = np.empty(size, dtype='i')

data = comm.scatter(data,root=0)

print 'name',name,'rank',rank,'data',data
