#import libaries
from mpi4py import MPI
import numpy as np

#start communication with world
comm = MPI.COMM_WORLD

#gets rank of processor
rank = comm.Get_rank()

#gets number of processors available
size= comm.Get_size()

#gets name of node
name=MPI.Get_processor_name()


if rank==0:
        data=rank
        for i in range(size):
                comm.send(data,dest=i)
data=comm.recv(source=0)
print("Name:",name,"rank",rank,"data",data)

MPI.Finalize
