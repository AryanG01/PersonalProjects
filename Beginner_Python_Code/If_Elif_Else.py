is_male = False
is_tall = True

if is_male and is_tall:
  print("He is a tall male")
elif is_male and not is_tall:
  print("He is a male but not tall")
elif not is_male and is_tall:
  print("She is a tall woman")
elif not is_male and not is_tall:
  print("She is a woman but not tall")