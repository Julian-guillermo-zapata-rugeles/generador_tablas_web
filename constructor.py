""""
Creado por Julian Rugeles
2019
proyecto colossus-A


modulo para la creacion de el index web
modulos del sistema
nohup 
sleep
ls

descripcion: lee el archivo data alojado en el directorio main


<td><a href="file_name"> Link </a> file_name </td></tr> 
"""










import os #modulo para ejecutar comandos de la terminal

def generar_plantilla():
	#funcion leer archivo, recibe nombre archivo ubicado en el main
	def readFile(filename):
		file=open(filename,"r")
		file=file.read()
		return file

	def load_files():
		#full_list=[]
		os.system("rm outputs")
		os.system("clear")
		os.system("ls >> outputs")
		loaded=open("outputs","r")
		loaded=loaded.read()
		data=loaded.split('\n')
		return data
	retorned=load_files()
	print("############################################")
	print(" Generando los enlaces para el host statico")
	print("############################################")
	exportable=open("index.html","w")
	basefile=readFile("base")
	exportable.write(basefile)
	for x in retorned:
		flushed="<td><a href='https://bootes-void.firebaseapp.com/file_name1'> Link </a> file_name2 </td></tr>"
		flushed=flushed.replace("file_name1",str(x))
		flushed=flushed.replace("file_name2",str(x))
		exportable.write(flushed)
		exportable.write('\n')
	exportable.close()
	print("################################")
	print("      MODULO FINALIZADO")
	
generar_plantilla()
