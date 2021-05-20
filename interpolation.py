from math import factorial

def c_i( i, X, Y ):
  y_i = Y[ X[ i ] ]
  denominator = 1
  for j in range( len( X ) ):
    if i != j:
      denominator = denominator * ( X[ i ] - X[ j ] )
  return y_i / denominator

def c_n( X, Y ):
  return [ c_i( i, X, Y ) for i in range( len( X ) ) ]

def l_i( X, Y, i, c_i, x ):
  product = c_i
  for j in range( len( X ) ):
    if i != j:
      product = product * ( x - X[ j ] )
  return product

def l_n( X, Y, x ):
  cn = c_n( X, Y )
  return [ l_i( X, Y, i, cn[ i ], x ) for i in range( len( X ) ) ]

def L_n( X, Y, x ):
  return sum( l_n( X, Y, x ) )

def d_ky_i( k, i, X, Y ):
  if k == 0:
    return Y[ X[ i ] ]
  else:
    return d_ky_i( k - 1, i + 1, X, Y ) - d_ky_i( k - 1, i, X, Y )

def a_k( k, h, X, Y ):
  return d_ky_i( k, 0, X, Y ) / ( factorial( k ) * h**k )

def N_n( X, Y, x ):
  h = X[ 1 ] - X[ 0 ]
  sum = a_k( 0, h, X, Y )
  print( f'a_0 = {sum}' )
  product = 1
  for k in range( 1, len( X ) ):
    coeff = ( x - X[ k - 1 ] )
    product = product * ( x - X[ k - 1 ] )
    print( f'product = {product}' )
    print( f'( {x} - x_{k - 1}) = {x} - {X[ k - 1]} = {coeff}' )
    ak = a_k( k, h, X, Y )
    print( f'a_{k} = {ak}' )
    sum = sum + ak * product
  return sum