import time
import random


num_digits = int(input("Number of Digits: "))
user_seq = []
count = 0


for i in range(num_digits):
    user_seq.append(int(input("Digit: ")))


isEqual = False
start_time = time.perf_counter()
while not isEqual:
    gen_seq = []
    count += 1
    if count % 1000000 == 0:
        print(f"Day {count} :: Sequences per second: {count/(time.perf_counter()-start_time)}")

    isEqual = True
    for i in range(num_digits):
        gen_seq.append(random.randint(1, 9))

        if user_seq[i] != gen_seq[i]:
            isEqual = False
