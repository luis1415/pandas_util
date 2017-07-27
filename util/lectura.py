import pandas as pd


def leer(archivo):
    """
    Recibe el nombre del archivo y retorna el dataframe
    :param archivo: nombre del archivo con la extension
    :return: Dataframe 
    """
    if 'xls' in archivo:
        return pd.read_excel(archivo)
    if 'csv' in archivo:
        return pd.read_csv(archivo, encoding="utf-8")


def buscarv(col_comun, col_buscar, df1, df2):
    """
    Esta funcion es equivalente al buscarv o vlookup de excel
    :param col_comun: columna comun en los dos dataframes
    :param col_buscar: columna que se busca y que se va a agregar
    :param df1: dataframe inicial
    :param df2: dataframe tabla donde buscar
    :return: un dataframe completo con la nueva columna
    """
    return df1.merge(df2[[col_comun, col_buscar]], how='left')
