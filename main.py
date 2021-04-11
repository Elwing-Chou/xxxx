# 計算bmi: 體重 / 身高(m) ^ 2
weight = float(input("請輸入體重:"))
height = float(input("請輸入身高:"))
bmi = weight / (height / 100) ** 2
print("體重是:" + str(weight))
print("身高是:" + str(height))
print("bmi是:" + str(bmi))
