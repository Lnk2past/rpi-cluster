from dask.distributed import Client, SSHCluster

def inc(x):
    return x + 1

def double(x):
    return x * 2

def add(x, y):
    return x + y


cluster = SSHCluster(
    ["raspberrypi0", "raspberrypi1", "raspberrypi2", "raspberrypi3", "raspberrypi4"],
    remote_python='/home/lnk2past/micromamba/envs/dask/bin/python'
)
client = Client(cluster)

data = list(range(1000000))

output = []
for x in data:
    a = inc(x)
    b = double(x)
    c = add(a, b)
    output.append(c)

total = sum(output)

print(total)
