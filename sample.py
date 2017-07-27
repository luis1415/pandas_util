import util.lectura as r

if __name__ == '__main__':
    df = r.leer('datos.csv')
    print df
    df2 = df

    df2['d'] = 10*df2[' c']

    resultado = r.buscarv('a', ' c', df, df2)
    print(resultado)
