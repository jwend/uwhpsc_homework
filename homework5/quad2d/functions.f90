
module functions

    use omp_lib
    implicit none
    integer :: fevals(0:7)
    integer :: gevals(0:7)
    real(kind=8) :: k
    save

contains

    real(kind=8) function forig(x)
        implicit none
        real(kind=8), intent(in) :: x 
        integer thread_num

        ! keep track of number of function evaluations by
        ! each thread:
        thread_num = 0   ! serial mode
        !$ thread_num = omp_get_thread_num()
        fevals(thread_num) = fevals(thread_num) + 1
        
        forig = 1.d0 + x**3 + sin(k*x)
        
    end function forig

    real(kind=8) function f(x)
      implicit none
      real(kind=8), intent(in) :: x 
      integer thread_num

     


      real(kind=8) :: a,b
      integer  :: n

      ! Local variables:
      integer :: j
      real(kind=8) :: h, trap_sum, yj
     
      ! keep track of number of function evaluations by
      ! each thread:
      thread_num = 0   ! serial mode
      !$ thread_num = omp_get_thread_num()
      fevals(thread_num) = fevals(thread_num) + 1


      a = 1.d0
      b = 4.d0
      n = 1000
      h = (b-a)/(n-1)
      trap_sum = 0.5d0*(g(x,a) + g(x,b))  ! endpoint contributions

      !    !$omp parallel do private(xj) reduction(+ : trap_sum) 
      do j=2,n-1
         yj = a + (j-1)*h
         trap_sum = trap_sum + g(x,yj)
      enddo

      f = h * trap_sum

    end function f

    real(kind=8) function g(x,y)
      implicit none
      real(kind=8), intent(in) :: x ,y 
      integer :: thread_num
      ! keep track of number of function evaluations by
      ! each thread:
      thread_num = 0   ! serial mode
      !$ thread_num = omp_get_thread_num()
      gevals(thread_num) = gevals(thread_num) + 1


      g = sin(x+y)

    end function g


end module functions
