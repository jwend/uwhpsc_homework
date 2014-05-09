module quadrature

    ! module parameters:
    implicit none
    save
contains

function linspace(a,b,n)

  real(kind=8), dimension(n) :: linspace
  real(kind=8), intent(in) :: a, b
  integer, intent(in) :: n
  real(kind=8) :: delta
  integer :: i

  delta=(b-a)/(n-1)
  linspace=a + delta*(/(i,i=0,n-1)/)

 end function linspace 


real(kind=8) function trapezoid(f,a,b,n)
    use omp_lib     
    implicit none
    real(kind=8), intent(in) :: a,b
    real(kind=8), external :: f
    integer, intent(in) :: n

    real(kind=8) :: h 
    integer :: i,j
    real(kind=8) trap_sum, xj, make_work


    h = (b-a)/(n-1)
    trap_sum = 0.5d0*(f(a) + f(b))  ! endpoint contributions

    !$omp parallel do private(xj) reduction(+: trap_sum)
    do j=2,n-1
        xj = a + (j-1)*h
        trap_sum = trap_sum + f(xj)
        do i=1,10000
          make_work=cos(make_work)
        end do 
!        print *, "j ", j, "n ", n, "thread ", omp_get_thread_num()
    enddo
    !$omp end parallel do 
    trapezoid = h * trap_sum

    
end function trapezoid


subroutine error_table(f,a,b,nvals,int_true)

implicit none
real(kind=8), external :: f
real(kind=8), intent(in) :: a,b
integer, dimension(:), intent(in) :: nvals
real(kind=8), intent(in) :: int_true
real(kind=8) :: t1,t2
integer :: i, n, nvals_size
real(kind=8) :: last_error, error, ratio, int_trap
nvals_size = size(nvals)

print *, "    n         trapezoid            error       ratio      cpu time"

last_error = 0.d0
do i = 1, nvals_size
        n = nvals(i)
        call cpu_time(t1)
        int_trap = trapezoid(f,a,b,n)
        call cpu_time(t2)
        error = abs(int_trap - int_true)
        ratio = last_error / error
        last_error = error
!print *, t1, " ", t2
        print 11, n, int_trap, error, ratio, t2-t1
11      format(i8, es22.14, es13.3, es13.3, es13.3)  
     end do

end subroutine error_table


end module quadrature
