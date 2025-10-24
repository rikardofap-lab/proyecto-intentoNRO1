from cryptography.fernet import Fernet

clave_fernet = Fernet.generate_key()
print(f"Clave Fernet: {clave_fernet.decode()}")
print(f"longitud {len(clave_fernet)}"), end="\n\n"
contraseña = input("Ingrese su contraseña: ")
clave_fernet = "aqui inserto la clave generada anteriormente"

f = Fernet(clave_fernet)
contrasena_encriptada = f.encrypt(contraseña.encode())
print(f"Contraseña encriptada: {contrasena_encriptada.decode()}")
print(f"longitud {len(contrasena_encriptada)}"), end="\n\n"

contrasena_desencriptada = f.decrypt(contrasena_encriptada)
print(f"Contraseña desencriptada: {contrasena_desencriptada.decode()}")
print(f"longitud {len(contrasena_desencriptada)}"), end="\n\n"