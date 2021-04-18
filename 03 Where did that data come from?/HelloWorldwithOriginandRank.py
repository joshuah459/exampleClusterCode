from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
name=MPI.Get_processor_name()
print(("Hello World from:",name,"whose rank is",rank))
