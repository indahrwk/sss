# SOAL IMT
massa = int(input("Masukkan Massa : "));
tinggi = int(input("Masukkan Tinggi : "));

text = "";
IMT = massa/((tinggi/100)**2);

if(IMT < 18.5):
    text = "BERAT BADAN KURANG !";
elif(IMT >= 18.5 and IMT <= 24.9):
    text = "BERAT BADAN IDEAL !";
elif(IMT >= 25.0 and IMT <= 29.9):
    text = "BB Berlebih";
elif(IMT >= 30.0 and IMT <= 39.9):
    text = "BB SANGAT BERLEBIH !";
else:
    text = "OBESITAS";


print("Massa" + str(massa) + " kg & tinggi" + str(tinggi) + " m");
print("IMT = " + str(IMT) + " ," + text);
