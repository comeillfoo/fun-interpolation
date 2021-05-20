def std_print_items( items ):
  for idx, data in enumerate( items, start=1 ):
    print( f'[ {idx} ]: {data}' )
  print( '[ X ]: Выйти' )

def std_read_item_from_items( header, items ):
  item = None
  while True:
    print( header )
    std_print_items( items )
    try:
      item = int( input( '> ' ) )
      if ( item < 1 or item > len( items ) ):
        print( 'Осуществляем выход...' )
        exit()
      else:
        return item - 1
    except ( ValueError ):
      print( "Неверный формат данных. Попробуйте еще раз..." )

def std_read_ipair( i ):
  xy = None
  while True:
    xy = input( f'[ {i + 1} ]: Введите узел ( x, y ): ' )
    try:
      x, y = xy.split( ' ', 2 )
      return ( float( x ), float( y ) )
    except ( ValueError ):
      print( "Неверный формат данных. Попробуйте еще раз..." )
    except ( IndexError ):
      print( "Неверный формат данных. Попробуйте еще раз..." )

def std_read_interpolation_nodes_number():
  nodes_number = None
  while True:
    nodes_number = input( "Введите число узлов интерполяции ( не менее 1 ): " )
    try:
      nodes_number = int( nodes_number )
      if ( nodes_number >= 1 ):
        break
      else:
        print( "Узлов интерполяции должно быть не менее 1. Попробуйте еще раз..." )
    except ( ValueError ):
      print( "Неверный формат данных. Попробуйте еще раз..." )
  return nodes_number

def extract_nodes():
  nodes_number = std_read_interpolation_nodes_number()
  print( f'Будет считано {nodes_number} узлов интерполяции' )
  X = []
  Y = {}
  for node in range( nodes_number ):
    x, y = std_read_ipair( node )
    print( f'Считан узел: ( {x}, {y} )' )
    try:
      X.index( x )
    except ValueError:
      X.append( x )
    Y[ x ] = y

  return ( X, Y )

def std_read_argument( i ):
  x = None
  while True:
    x = input( f'[ {i + 1} ]: Введите аргумент ( x ): ' )
    try:
      return float( x )
    except ( ValueError ):
      print( "Неверный формат данных. Попробуйте еще раз..." )

def extract_arguments( fun ):
  arguments_number = std_read_interpolation_nodes_number()
  print( f'Будет считано {arguments_number} узлов интерполяции' )
  X = []
  Y = {}
  for node in range( arguments_number ):
    x = std_read_argument( node )
    print( f'Получен узел: ( {x}, {fun( x )} )' )
    try:
      X.index( x )
    except ValueError:
      X.append( x )
    Y[ x ] = fun( x )
  return ( X, Y )