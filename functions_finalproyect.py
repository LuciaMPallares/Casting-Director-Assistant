#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def edades(df, column):
    '''Agrupa la fecha de nacimiento por rango de edad y genera una nueva columna'''
    
    Rango_Edad=[]
    
    for fecha in column:
        if fecha >= 1997:
            Rango_Edad.append('Joven')
        elif fecha <= 1998 and fecha >= 1982:
            Rango_Edad.append('Adulto Joven')
        elif fecha <= 1983 and fecha >= 1963:
            Rango_Edad.append('Adulto medio')
        elif fecha <= 1964:
            Rango_Edad.append('Adulto maduro')
        
    df['Rango_Edad']= Rango_Edad
    
    df= df.drop(df[column < 1947].index).reset_index(drop=True)
    
    
    return df




def genero(df, column, x, y):
    '''Genero una columna por cada genero que encuentra en la columna genero y borra paréntesis'''
    df.loc[column.str.split('(').str[0]== x , y ]= column.str.split('(').str[1].str.rstrip(')')
    
    return df



def prem_nom (df, columna):
    '''Genero 2 nuevas columnas de separar la colm Premios segun sus datos, me quedo del espacio a la iz para premios y del espacio a la drc
    para nominaciones. Relleno los nan con 0'''
    
    df[['Premios','Nominaciones']]= columna.str.extract(r'(.*)[y]+(.*)', expand=True)
    df['Premios']= df['Premios'].str.split(' ').str[0]
    df['Nominaciones']= df['Nominaciones'].str.split(' ').str[1]
    df[['Premios', 'Nominaciones']]= df[['Premios', 'Nominaciones']].fillna(value=0)
    
    return df




