! $UWHPSC/codes/fortran/newton/test1.f90

program test_quartic

    use newton, only: solve, tol
    use functions, only: f_quartic, fprime_quartic, epsilon

    implicit none
    real(kind=8) :: x, x0, fx, xstar
    real(kind=8) :: tols(3)
    real(kind=8) :: epsilons(3)
    integer :: iters, i, j
    logical :: debug         ! set to .true. or .false.


    debug = .false.

    ! values to test as x0:
    x0= 4.d0;
    tols = (/ 1d-5, 1d-10, 1d-14 /)
    epsilons = (/ 1d-4, 1d-8, 1d-12 /)

    print *, 'Starting with the initial guess ', x0
    print *, '    epsilon        tol    iters          x                 f(x)        x-xstar'
    do i=1,3
        epsilon = epsilons(i)
		print *, ' '  ! blank line
        do j=1,3
           tol = tols(j)
           call solve(f_quartic, fprime_quartic, x0, x, iters, debug)
           fx = (x-1.d0)**4 - epsilon
           xstar = 1 + epsilon**(0.25d0)
           print 11, epsilon, tol, iters, x, fx, x-xstar
11         format(2es13.3, i4, es24.15, 2es13.3)
        end do
	print *, ' '  ! blank line
    end do 
 
end program test_quartic
