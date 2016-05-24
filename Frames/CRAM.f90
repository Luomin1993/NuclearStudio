module CRAM

public
complex::seta(14)
complex::alpha(14)
interger::N=2000
real::A(N,N)

contains

subroutine GAUSS_solve(A,B,X,N,M)
!-----------------------------------------------------
!  Purpose   :  高斯列主元消去法计算矩阵方程组
!  AX=B
!-----------------------------------------------------
!  Input  parameters  :
!       1.   A  A(N,N)系数矩阵
!       2.   B  B(N,M)右向量
!       3.   N  N方程维数
!       4.   M  M右矩阵的列数
!  Output parameters  :
!       1.  X 方程的解矩阵
!----------------------------------------------------
implicit real*8(a-z)
integer::i,k,N,M
integer::id_max 
real*8::A(N,N),B(N,M),X(N,M)
real*8::Aup(N,N),Bup(N,M)
real*8::AB(N,N+M)
real*8::vtemp1(N+M),vtemp2(N+M)
real*8::vtmp(N),xtmp(N)
AB(1:N,1:N)=A
AB(:,N+1:N+M)=B
do k=1,N-1
    elmax=dabs(Ab(k,k))
    id_max=k
	do i=k+1,n
      if (dabs(Ab(i,k))>elmax) then
         elmax=Ab(i,k)
        id_max=i
      end if          
    end do
    vtemp1=Ab(k,:)
    vtemp2=Ab(id_max,:)
    Ab(k,:)=vtemp2
    Ab(id_max,:)=vtemp1   
  do i=k+1,N
     temp=Ab(i,k)/Ab(k,k)
     Ab(i,:)=Ab(i,:)-temp*Ab(k,:)
   end do
end do
Aup(:,:)=AB(1:N,1:N)
do i=1,m
vtmp=AB(:,N+i)
call uptri(Aup,vtmp,xtmp,n)
X(:,i)=xtmp
end do

end subroutine GAUSS_solve

subroutine uptri(A,b,x,N)
!-----------------------------------------------------
!  Purpose   :  上三角方程组的回带方法
!  Ax=b
!-----------------------------------------------------
!  Input  parameters  :
!       1.   A(N,N)系数矩阵
!       2.   b(N)右向量
!       3.   N方程维数
!  Output parameters  :
!       1.  x  方程的根
!----------------------------------------------------
implicit real*8(a-z)
integer::i,j,N
real*8::A(N,N),b(N),x(N)
x(N)=b(N)/A(N,N)
do i=n-1,1,-1   
    x(i)=b(i)
   do j=i+1,N
    x(i)=x(i)-a(i,j)*x(j)
   end do
    x(i)=x(i)/A(i,i)
end do

end subroutine uptri

subroutine driver(N,M)
!-----------------------------------------------------
!  Purpose   : 驱动程序
!-----------------------------------------------------
!  Input  parameters  :
!       1.   N     描述A(N,N)
!       2.   M     描述方程 X(N,M)，B(N,M)
!  P.S  :
!      N,M  从文件中读取
!----------------------------------------------------
end subroutine driver

subroutine inv_solve(A,invA,N)  
!-----------------------------------------------------
!  Purpose   :  计算逆矩阵    
!-----------------------------------------------------
!  Input  parameters  :
!       1.A矩阵
!       2.invA 待计算逆矩阵
!       3.N A的维数
!  Output parameters  :
!       1.
!----------------------------------------------------
implicit real*8(a-z)
integer::n
integer::i
real*8::A(n,n),invA(n,n),E(n,n)
E=0
do i=1,n
   E(i,i)=1
end do
call GAUSS_solve(A,E,invA,N,N)

end subroutine inv_solve

end module CRAM
	