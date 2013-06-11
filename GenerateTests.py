from Collatz import collatz_eval
import random

min_num = 1
max_num = 1000000

def generate_new_test () :
    num_1 = random.randint (min_num, max_num)
    num_2 = random.randint (num_1, max_num)
    result = collatz_eval (num_1, num_2)
    in_out = {}
    in_out['in'] = str(num_1) + " " + str(num_2) + "\n"
    in_out['out'] = str(num_1) + " " + str(num_2) + " " + str(result) + "\n"
    return in_out

in_file = open ("RunCollatz.in", "a+")
out_file = open ("RunCollatz_out", "a+")

for i in range(20) :
    in_out = generate_new_test()
    print str(i) + "\t" + in_out['out']
    in_file.write (in_out['in'])
    out_file.write (in_out['out'])

in_file.close()
out_file.close()

