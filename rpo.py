def DelOff(start):
  with open("output.json", "r") as f:
    lines = f.readlines()
  with open("output.json", "w") as f:
    with open("output2.json", "w") as o2:
      for line in lines:
        if start not in line.strip("\n"):
          o2.write(line)

def DelMax(has, has2):
  with open("output2.json", "r") as f:
    lines = f.readlines()
  with open("output2.json", "w") as f:
    with open("output.json", "w") as o2:
      for line in lines:
        if has in line.strip("\n") and has2 in line.strip("\n"):
          o2.write(line)