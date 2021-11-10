b = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/"

def rot32(s):
    o = ""
    for c in s:
        if c not in b:
            o += c
        else:
            o += b[b.find(c) ^ 32]
    return o

if __name__ == "__main__":
   a = "1234567890"
   print(rot32(a))