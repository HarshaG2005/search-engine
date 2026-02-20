from nltk.stem import PorterStemmer

ps = PorterStemmer()

x=ps.stem("prawns")
y=ps.stem("cooking")   # stem of cooking is cook, but it is not cooking
z=ps.stem("deviled")   # stem of cooked is cook, but it is not cooked 
print(x)
print(y)
print(z)
