class B(Exception):
    pass

class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D, None]:
    try:
        if cls == None:
            raise ValueError;
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
    except Exception as e:
        print("outra exceção:" + e.__class__.__name__ )    
        print("Mensagem:" + str(e))