nomer1 = 1
nomer2 = 2
nama = "fathur"
if nomer2 > nomer1 and nama == "fathur":
	print("nomer2 lebih dari nomer1")
elif nomer 2 > nomer1 and nama != "fathur":
	print("nomer1 lebih dari nomer2")
else:
	print("lainnya")
for i in range(0,5):
	print(i)
print("=======")
arrdata = [3,4,5,6]
print("=======")
arrdatajson = [{"nama": "fathur", "kelas": 8}, {""nama": "bagus", "kelas": 10}, {"nama": "nurmajid", "kelas": 11}]
for i in arrdatajson:
	print(i["nama"])
print("=======")
for i in range(1, len(arrdatajson)):
	print(arrdatajson[i]["nama"])
def menampilkankelas():
	print("=======")
	for i in range(1, len(arrdatajson)):
		print(arrdatajson[i]["kelas"])
menampilkankelas()