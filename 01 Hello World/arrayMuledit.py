from mpi4py import MPI
import numpy as np
import sys
import random
comm = MPI.COMM_WORLD
global size
size = 3
rank = comm.Get_rank()
numOfPis=comm.Get_size()


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


for r in range(0,size):
        if rank == 0:
                print(numOfPis)
                print(r)
                rowmat=np.array([[0 for i in range(size)]])
                print(rowmat)
                dest=0
                #comm.bcast(mat1[:,r],root=0)
                for c in range(0,size):
                        dest=dest+1
                        if (dest==numOfPis):
                                dest=1
                        print("rank "+str(rank)+" sending to dest "+str(dest)+"....")
                        comm.send(mat1[:,r],dest=dest)
                        comm.send(mat2[c],dest=dest)
                        print("rank "+str(rank)+ " receving from dest "+str(dest)+"....")
                        rowmat[0][c]=comm.recv(source=dest)
                        print(rowmat)
                del rowmat
        else:
                print("rank "+str(rank)+" recieving from master....")
                matr1=comm.recv(source=0)
                matr2=comm.recv(source=0)
                result=np.dot(matr1,matr2)
                print("rank "+str(rank)+" sending result "+str(result)+" to master....")
                comm.send(result,dest=0)
                del matr1
                del matr2
                del result
        #input the column of dot product to row
MPI.Finalize
