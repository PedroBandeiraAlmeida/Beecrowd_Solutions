c, g = map(int, input().split())

if (c == 1 and g == 0) or (c == 1 and g == 1):
    print("vivo e morto")

elif (c == 0 and g == 1):
    print("vivo")

else:
    print("morto")