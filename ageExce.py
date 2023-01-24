#age exception
class INVALIDAGE(Exception):
  def __str__(self):
    return "ERROR RAISED LESS THAN 18"
stid=int(input("enter your age"))
try:
  if stid<18:
    raise INVALIDAGE
  else:
    print("verified")
except INVALIDAGE as i:
  print(i)
print("details checked")