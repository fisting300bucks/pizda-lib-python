import math
import cmath
import inspect
import os
import numpy as np
import matplotlib.pyplot as plt

class p:

    def __init__ (self, r: float, phi:float): #хуй знает, ну чисто принимаем
        self.r = r
        self.phi = phi

    def to_polar(z: complex): #алгебраическую в полярную хуярим
        a = z.real
        b = z.imag
        a1 = math.sqrt(a*a+b*b)
        b1 = math.atan2(b, a)*180/math.pi 
        c1 = f"{a1:.4f} {b1:.4f}"
        return c1 
    
    def vivo(x): #Вывод говна
        if not hasattr(vivo, '_initialized'):
            file_path = os.path.join(os.getcwd(), "1.txt")
            with open("1.txt", "w", encoding="utf-8") as f:  # Очищаем файл при первом вызове
                f.write("")
            print(f"Файл создан: {file_path}")
            vivo._initialized = True  # Помечаем как инициализированное
    
        frame = inspect.currentframe().f_back
        name = None
        for var_name, var_val in frame.f_locals.items():
            if var_val is x:
                name = var_name
                break
        if name is None:
            name = "?"
        if isinstance(x, complex): #если комплексная залупа
            real_part = x.real
            imag_part = x.imag
            if imag_part >= 0:
                result = f"{name} : {real_part:.4f} + j({imag_part:.4f})"
            else:
                result = f"{name} : {real_part:.4f} - j({abs(imag_part):.4f})"
        if isinstance(x, str): #если полярная , но питон тупой пиздец, так что это строка нахуй
            full = x.split()
            r = float(full[0])
            phi = float(full[1])
            result = f"{name} : {r:.4f} ∠ {phi:.4f}"
        if isinstance(x, int):
            result = f"{name} : {x:.4f}"
        if isinstance(x, float):
            result = f"{name} : {x:.4f}"
        with open("1.txt", "a", encoding="utf-8") as f:
             f.write(result + "\n")
             f.flush()
        return print(result)
    
    def to_complex(s: str): #с полярной в комлпексную ебашим
        full = s.split()
        r = float(full[0]) 
        phi = float(full[1]) 
        c1 = cmath.rect(r, math.radians(phi))
        return c1
    
    def Slojenie(s:str, d:str):
        a = p.to_complex(s) 
        b = p.to_complex(d)
        c = a+b
        d = p.to_polar(c)
        return d
    
    def Otnimanie(s:str, d:str):
        a = p.to_complex(s) 
        b = p.to_complex(d)
        c = a-b
        d = p.to_polar(c)
        return d
    
    def Ymnojenie(s:str, d:str):
        a = p.to_complex(s) 
        b = p.to_complex(d)
        c = a*b
        d = p.to_polar(c)
        return d
    
    def Delenie(s:str, d:str):
        a = p.to_complex(s) 
        b = p.to_complex(d)
        c = a/b
        d = p.to_polar(c)
        return d
    
    def to_faz(s:str):
        full = s.split()
        r = float(full[0]) 
        phi = float(full[1]) 
        c = r / math.sqrt(3)
        phi = phi - 30
        return f"{c:.2f} {phi}"
    
    def to_line(s:str):
        full = s.split()
        r = float(full[0]) 
        phi = float(full[1]) 
        c = r * math.sqrt(3)
        phi = phi + 30
        return f"{c:.2f} {phi}"
    
    def paralel_comp(x=None, y=None, s=None):
        if isinstance(s, str): 
            full = s.split()
            x = float(full[0]) 
            y = float(full[1]) 
            x = p.to_complex(x) 
            y = p.to_complex(y)
            c= (x*y)/(x+y)
            return c
        else:
            c= (x*y)/(x+y)
            return c
        
    def izdlin(s:str):
        full = s.split()
        r = float(full[0]) 
        return r
    
    def to_zvezda(x:complex, y:complex, z:complex):
        if all(isinstance(val, (complex, int, float)) for val in (x, y, z)):
            r1 = (x*y)/(x+y+z)
            r2 = (x*z)/(x+y+z)
            r3 = (z*y)/(x+y+z)
            return r1 , r2 , r3
        if isinstance(x, str):
            x = p.to_complex(x) 
            y = p.to_complex(y)
            z = p.to_complex(z)
            r1 = (x*y)/(x+y+z)
            r2 = (x*z)/(x+y+z)
            r3 = (z*y)/(x+y+z)
            return r1 , r2 , r3
        
    def izgrad(s:str):
        full = s.split()
        r = float(full[1]) 
        return r
    
    def Ymnojenie_chislo(s:str, y:float):
        full = s.split()
        x = float(full[0]) 
        phi = float(full[1]) 
        x = x*y
        return f"{x:.2f} {phi}"
    
    def Delenie_chislo(s:str, y:float):
        full = s.split()
        x = float(full[0]) 
        phi = float(full[1]) 
        x = x/y
        return f"{x:.2f} {phi}"

    def to_treygolnik(x:complex, y:complex, z:complex):
        if all(isinstance(val, (complex, int, float)) for val in (x, y, z)):
            r1 = x+y+((x*y)/z)
            r2 = y+z+((y*z)/x)
            r3 = z+x+((z*x)/y)
            return r1 , r2 , r3
        if isinstance(x, str):
            x = p.to_complex(x) 
            y = p.to_complex(y)
            z = p.to_complex(z)
            r1 = x+y+((x*y)/z)
            r2 = y+z+((y*z)/x)
            r3 = z+x+((z*x)/y)
            return r1 , r2 , r3
        
    def Providnist(x:complex):
        c = 1/x
        return c
    
    def spraj_polar(v:str):
        full = v.split()
        x = float(full[0]) 
        y = float(full[1]) 
        y *= -1
        return f"{x:.2f} {y}"

vivo = p.vivo
to_polar = p.to_polar
Slojenie = p.Slojenie
Otnimanie = p.Otnimanie
Ymnojenie = p.Ymnojenie
Delenie = p.Delenie
to_complex = p.to_complex
to_faz = p.to_faz
to_line = p.to_line
paralel_comp = p.paralel_comp
izdlin=p.izdlin
to_zvezda=p.to_zvezda
izgrad=p.izgrad
Ymnojenie_chislo=p.Ymnojenie_chislo
Providnist=p.Providnist
to_treygolnik=p.to_treygolnik
spraj_polar=p.spraj_polar
Delenie_chislo=p.Delenie_chislo

class g:
    def __init__(self, r: str):
        self.r = r

    def to_cord(r:str):
        full = r.split()
        r = float(full[0])
        phi = math.radians(float(full[1]))
        x = r * math.cos(phi)
        y = r * math.sin(phi)
        return f"{x:.4f} {y:.4f}"
    
    def Grafik(self):
        pass
    
to_cord = g.to_cord
