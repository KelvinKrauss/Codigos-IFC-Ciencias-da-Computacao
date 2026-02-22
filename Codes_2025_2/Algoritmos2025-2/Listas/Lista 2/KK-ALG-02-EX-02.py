s = float(input("digite os segundos : "))
d = int(s // (24 * 60 * 60))
s = s % (24 * 60 * 60)
h = int(s // 3600)
s = s % 3600
m = int(s // 60)
s = int(s % 60)
print(f"{d}:{h:02d}:{m:02d}:{s:02d}")