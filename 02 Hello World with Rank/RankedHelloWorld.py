from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

data="Hello World"

print 'rank: ',rank,data

