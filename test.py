from multiprocessing import Pool


def f(x):
   for i in range(10000000000):
       print(i)

if __name__ == '__main__':
    with Pool(10) as p:
        p.map(f, [1, 2, 3])

