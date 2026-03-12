a = [
b = [
c = []
r = ""
for i in range(len(a)):
    for j in range(len(a[i])):
        print(r)
        # or a second version:
            a = [
            b = [
            # Pre-allocate the size of c.
            c = [[0] * len(a[0]) for _ in range(len
            r = ""
            for i in range(len(a)):
                for j in range(len(a[i])):
                    print(r)