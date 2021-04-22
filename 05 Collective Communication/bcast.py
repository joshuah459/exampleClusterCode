
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size= comm.Get_size()
rank = comm.Get_rank()
if rank == 0:
        data= np.array([i for i in range(size)],dtype='i')
else:
        data = np.empty(size,dtype='i')

comm.Bcast(data, root=0)

print ("Rank: ", rank,"Data", data)
