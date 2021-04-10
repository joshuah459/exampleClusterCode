from mpi4py import MPI
import numpy as np
import sys
import random
comm = MPI.COMM_WORLD
global size
size = 10
rank = comm.Get_rank()
numOfPis=comm.Get_size()
dest = 0


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

if rank == 0:
	for r in range(0,size):
        	rowmat=np.array([[0 for i in range(size)]])
                print(rowmat)
        	dest=0
		for c in range(0,size):
			print("sending with c:"+str(c)+"....")
                	if dest>numOfPis:
                               	dest=1
                        else:
                               	dest=dest+1
                        comm.send(mat1[:,r],dest=dest)
                        comm.send(mat2[c],dest=dest)
		for c in range(0,size):
			print("receving with c:"+str(c)+"....")
			rowmat[0][c]=comm.recv(source=dest)
                        print(rowmat)

else:
	print("recieing from master....")
	matr1=comm.recv(source=0)
	matr2=comm.recv(source=0)
	result=np.dot(matr1,matr2)
       	print("sending result:"+str(result)+" to master....")
	comm.send(result,dest=0)

MPI.Finalize
