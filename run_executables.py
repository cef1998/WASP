import os
import os
import os.path
from glob import glob

def run_executable(exec_name):

	# exec_name is the name of exec received in lower case
	exec_name = ''.join(exec_name.split(" "))
	exec_name += '.lnk'
	exec_name = exec_name.lower()

	result = [y for x in os.walk("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs") for y in glob(os.path.join(x[0], '*.lnk'))]

	shortcuts=[]
	
	index = 0
	for files in result:
		index = files.rfind('\\') + 1
		shortcuts.append(files[index:])

	nw_names=[]
	for names in shortcuts:
		nw_names.append(''.join(names.split(" ")).lower())

#	for b in nw_names:
#		print(b)

	if exec_name in nw_names:
		index = nw_names.index(exec_name)
		stri = shortcuts[index]
		os.system("start "+'"" '+'"'+'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\'+stri+'"')
	else:
		print('No such application found')

#run_executable('Firefox')

#for nw in nw_names:
	#print(nw)

#for names in shortcuts:
#	print(names)

#os.system("start "+'"" '+'"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++.lnk"')





