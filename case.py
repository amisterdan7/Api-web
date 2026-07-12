class MinhaClass:
    def __enter__(self):
        print("entrei aqui")
        
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou no exit")
        
with MinhaClass() as mc:
    print("Entrei no with")