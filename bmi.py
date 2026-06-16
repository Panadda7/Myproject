# โปรแกรมคำนวณ BMI

weight = float(input("กรอกน้ำหนัก (กิโลกรัม): "))
height = float(input("กรอกส่วนสูง (เมตร): "))

bmi = weight / (height ** 2)

print("\nBMI =", round(bmi, 2))

if bmi < 18.5:
     print("ผลสุขภาพ: น้ำหนักน้อย")
elif bmi < 23:
     print("ผลสุขภาพ: น้ำหนักปกติ")
elif bmi < 25:
     print("ผลสุขภาพ: น้ำหนักเกิน")
elif bmi < 30:
     print("ผลสุขภาพ: อ้วนระดับ 1")
else:
     print("ผลสุขภาพ: อ้วนระดับ 2")
