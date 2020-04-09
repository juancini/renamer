# Renombrador multiple V0.1
# By Juan Mancini

import os

# renemer es la funcion encargada de renombrar los archivos
#valores por defecto de newFileName es "archivo" y zeroFill es 3
def renamer(newFileName, zeroFill):
    for count, filename in enumerate(os.listdir(r"C:\Users\Juan\Documents\Programacion\renombrar")):
        # newFileName es el nombre del archivo, zeroFill cuanto padding de ceros
        # TODO lector de tipo de archivos
        dst = newFileName + str(count).zfill(int(zeroFill)) + ".mp3"
        src = r'C:\Users\Juan\Documents\Programacion\renombrar\\' + filename
        dst = r'C:\Users\Juan\Documents\Programacion\renombrar\\' + dst

        # rename() va a renombrar los archivos
        os.rename(src, dst)

# Funcion principal
def main():
    print("Bienvenido al Renamer V0.1 por jMancini")
    # nombre default de newFileName es archivo
    # valor default de zeroFill es 3
    newFileName = input("nombre del archivo, vacio le pone nombre generico: ") or "archivo"
    zeroFill = input("cantidad de ceros, vacio deja un espacio de 3 ceros:") or 3
    print("valores: ")
    print(str(newFileName))
    print(str(zeroFill))

    

    #renamer(newFileName, zeroFill)
    print("Listo!")

# Driver Code
if __name__ == '__main__':
    # llamado a funcion principal
    main()