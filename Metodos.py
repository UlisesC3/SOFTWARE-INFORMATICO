class Metodos:

    def Biseccion(self,a,b,tolera):
              
        #Bisección
        import numpy as np
        import matplotlib.pyplot as plt

        fx = lambda x: x**2 + 4*x- 10 

        tramo = b-a
        while not(tramo<tolera):
            c = (a+b)/2
            fa = fx(a)
            fb = fx(b)
            fc = fx(c)
            cambia = np.sign(fa)*np.sign(fc)
            if cambia < 0: 
                a = a
                b = c
            if cambia > 0:
                a = c
                b = b
            tramo = b-a

        print("Bisección")
        print('       Raiz en: ', c)
        print('error en tramo: ', tramo)



            

    def Newton(self, x0, tolera):
        import numpy as np
 
        fx  = lambda x: x**2 + 4*x- 10 
        dfx = lambda x: 2*x + 4
        tabla = []
        tramo = abs(2*tolera)
        xi = x0
        while (tramo>=tolera):
            xnuevo = xi - fx(xi)/dfx(xi)
            tramo  = abs(xnuevo-xi)
            tabla.append([xi,xnuevo,tramo])
            xi = xnuevo

        tabla = np.array(tabla)
        n = len(tabla)

        print("Newton")
        print(['xi', '       xnuevo', '   tramo'])
        np.set_printoptions(precision = 4)
        print(tabla)
        print('raiz en: ', xi)
        print('error en tramo: ', tramo)
        
      
        
    def Secante(self,fa,b,tolera):        
        import numpy as np
        def secante_tabla(fx,xa,tolera):
            dx = 4*tolera
            xb = xa + dx
            tramo = dx
            tabla = []
            while (tramo>=tolera):
                fa = fx(xa)
                fb = fx(xb)
                xc = xa - fa*(xb-xa)/(fb-fa)
                tramo = abs(xc-xa)
                
                tabla.append([xa,xb,xc,tramo])
                xb = xa
                xa = xc

            tabla = np.array(tabla)
            return(tabla)

        fx = lambda x: x**2 + 4*x- 10 
        a  = 1
        b  = 2
        xa = 1.5
        tolera = 0.001
        tramos = 100

        tabla = secante_tabla(fx,xa,tolera)
        n = len(tabla)
        raiz = tabla[n-1,2]

        print("--Secante")
        np.set_printoptions(precision=4)
        print('[xa ,\t xb , \t xc , \t tramo]')
        for i in range(0,n,1):
            print(tabla[i])
        print('raiz en: ', raiz)
        

aproximacion = Metodos()

#Se llama a los objetos
aproximacion.Biseccion(1,2,0.01)
aproximacion.Newton(2,0.01)
aproximacion.Secante(1,3,0.1)