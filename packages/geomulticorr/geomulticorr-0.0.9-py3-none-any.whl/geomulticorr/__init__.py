version = '0.0.9'

# User
try:
    from geomulticorr.session import Open
    
# Developer
except ModuleNotFoundError:
   from src.geomulticorr.session import Open

print('''-------------
geomulticorr {version}
-------------''')