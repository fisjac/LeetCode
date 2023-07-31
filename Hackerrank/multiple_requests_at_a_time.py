# read the string filename
filename = input()

times = set()
repeat_times = set()
with open(filename, 'r') as file:
  line = file.readline()
  while line:
    delim  = line.split(' ')
    time = delim[3].replace('[', '')

    if time in times:
      repeat_times.add(time)
    else:
      times.add(time)
    line = file.readline()


# print(repeat_times)
with open(f'req_{filename}', 'x') as outfile:
  lines = '\n'.join(list(repeat_times))
  outfile.write(lines)
