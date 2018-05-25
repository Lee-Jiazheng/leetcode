def find(target):
    ans = [0] * 10
    for i in range(1, 10):
        v = 1
        while i * v <= target:
            s = i * v
            while s <= min(i*v+v-1, target):
                mult=int(target/s);rema=target-(int(target/s))*s
                slip=1
                slip+=min(int(rema/mult),i*v+v-1-s)
                ans[i]+=(mult*slip)
                print(s, mult, slip, rema)
                s += slip
            v *= 10

find(200)