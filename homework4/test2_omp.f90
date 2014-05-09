
program test2
    use omp_lib
    use quadrature, only: linspace, error_table

    implicit none
    real(kind=8) :: a,b,int_true
    integer :: nvals(11), i
    integer(kind=8) :: tclock1, tclock2, clock_rate, nthreads
    real(kind=8) :: elapsed_time

    nthreads = 2

    !$ call omp_set_num_threads(nthreads)

    call system_clock(tclock1)  ! start wall timer

    a = 0.d0
    b = 2.d0
    int_true = (b-a) + (b**4 - a**4) / 4.d0

    print 10, int_true
 10 format("true integral: ", es22.14)
    print *, " "  ! blank line

    ! values of n to test:
    do i=1,11
        nvals(i) = 5 * 2**(i-1)
    enddo

    call error_table(f, a, b, nvals, int_true)

    call system_clock(tclock2, clock_rate)
    elapsed_time = float(tclock2 - tclock1) / float(clock_rate)
    print 11, elapsed_time
 11 format("Elapsed time = ",f12.8, " seconds")


contains

    real(kind=8) function f(x)
        implicit none
        real(kind=8), intent(in) :: x 
        
        f = 1.d0 + x**3 + sin(1000.d0 * x)
    end function f

end program test2
