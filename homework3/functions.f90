! $UWHPSC/codes/fortran/newton/functions.f90

module functions

real(kind=8), parameter :: pi = 4.*atan(1.)


contains



real(kind=8) function f_func(x)
    implicit none
    real(kind=8), intent(in) :: x

    f_func =  (x*cos(pi*x)) - (1.d0 - 0.6d0*x*x)

end function f_func


real(kind=8) function fprime_func(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    fprime_func = (cos(pi*x) - pi*x*sin(pi*x)) - (-1.2d0*x)

end function fprime_func


real(kind=8) function f_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x

    f_sqrt = x**2 - 4.d0

end function f_sqrt


real(kind=8) function fprime_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    fprime_sqrt = 2.d0 * x

end function fprime_sqrt

end module functions
