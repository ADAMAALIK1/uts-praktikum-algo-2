#menghitung huruf konsonan
kalimat=input('masukan sebuah kata/kalimat')
vokal = 'a,i,u,e,o'
jumlah_vokal =sum(1 for char in kalimat if char in vokal)
print(f'jumlah huruf vokal adalah :',jumlah_vokal)