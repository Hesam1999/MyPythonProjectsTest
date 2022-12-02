
N, M = map(int, input().split())

mat = ""

s = (M//2)+1
lsz = 0
sz = 0
lz = 0
z = 1
lzx = 0
zx = -1
i = 0
x = 0
u = 0
while i < N:
    while x < M:
        u = 1
        if i < (N//2):
            # create line
            if x == ((M // 2) - (1 + z + zx)):
                #-------------------------
                lz = z
                lzx = zx
                lsz = sz
                #-------------------------
                for c in range(0, z):
                    mat += ".|."

                x = (M // 2) + z + sz
                
                           
            else : 
                mat += "-"
            
        elif i == (N//2):
            u = 0
            if x < ((M - 6) // 2):
                mat += "-"
            elif x == ((M - 6) // 2):
                q = "WELCOME"
                mat += q
                x += len(q) -1
                # ----------------------------
                z = lz
                zx = lzx
                sz = lsz
            else:
                mat += "-"
        elif i > (N//2):
            u = 2
            if x == ((M // 2) - (1 + z + zx)):
                for c in range(0, z):
                    mat += ".|."

                x = (M // 2) + z + sz
            elif (x < ((M // 2) - (1 + z + zx))) or (x > (M // 2) + z + sz):
                mat += "-"
        x += 1
    mat += "\n"
    i += 1
    x = 0 
    if u == 1:
        z += 2
        zx += 1
        sz += 1
    elif u == 2:
        z -= 2
        zx -= 1
        sz -= 1
print(mat)