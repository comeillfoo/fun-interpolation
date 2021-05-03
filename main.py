from math import sin, exp
import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
from shell import *
from interpolation import L_n, N_n

def draw_array( X, Y ):
  plt.plot( X, [ y for y in Y.values() ], 'ro-', label='y = f( x )' )

def draw_inter( a, b, Xi, Yi, F_n ):
  X = np.arange( a - 2, b + 2, 1e-3 )
  y = []
  for x in X:
    try:
      y.append( F_n( Xi, Yi, x ) )
    except ValueError:
      y.append( 0 )
  plt.plot( X, y, 'b-', label='y = F_n( x )' )

sinx = { 'math': 'sin x', 'f': lambda x: sin( x ) }
expx = { 'math': 'e^x', 'f': lambda x: exp( x ) }
squarex = { 'math': 'x^2', 'f': lambda x: x**2 }

functions = [ sinx, expx, squarex ]

def main():
  try:
    data_type_methods = [ 'Набором данных ( x, y )', 'Выбрать заготовленную функцию' ]
    data_type_method = std_read_item_from_items( 'Выберите способ задания функции:', data_type_methods )
    print( )
    X = None
    Y = None
    if data_type_method == 0:
      X, Y = extract_nodes()
    elif data_type_method == 1:
      fun_number = std_read_item_from_items( 'Выберите функцию для интерполяции', list( map( lambda fun: fun[ 'math' ], functions ) ) )
      X, Y = extract_arguments( functions[ fun_number ][ 'f' ] )
    else:
      print( 'Осуществляем выход...' )
      exit()

    methods = [ 'Многочленом Лагранжа', 'Многочленом Ньютона с конечными разностями' ]
    method = std_read_item_from_items( 'Выберите метод интерполяции:', methods )
    print( )

    x0 = std_read_argument( -1 )
    y0 = 0
    F_n = None

    if method == 0:
      y0 = L_n( X, Y, x0 )
      F_n = L_n
      print( f'L_n( { x0 } ) = { y0 }' )
    elif method == 1:
      y0 = N_n( X, Y, x0 )
      F_n = N_n
      print( f'N_n( { x0 } ) = { y0 }' )
    else:
      print( 'Осуществляем выход...' )
      exit()

    a = min( min( X ), x0 )
    b = max( max( X ), x0 )
    fa = min( min( Y.values() ), y0 )
    fb = max( max( Y.values() ), y0 )
    plt.grid( True, 'both', 'both' )
    plt.axis( [ a, b, fa, fb ] )
    draw_inter( a, b, X, Y, F_n )
    draw_array( X, Y )
    plt.plot( x0, y0, 'bo', label=f'P_n( {x0} )' )
    plt.ylabel( 'y', horizontalalignment='right', y=1.05, rotation=0 )
    plt.xlabel( 'x', horizontalalignment='right', x=1.05 )
    plt.legend()
    plt.show()

  except KeyboardInterrupt:
    print( '\nЗавершение программы...' )
  except EOFError:
    print( '\nЗавершение программы...' )

if ( __name__ == "__main__" ):
  main()