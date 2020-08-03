import tempfile

with tempfile.TemporaryFile() as fp:
	fp.write(b'LAKSHMINATHAN Programpython student')
	fp.seek(0)
	a = fp.read()
	#fp.close()
print(a)
print("temp file create")
