import os
import pkg_resources

def calc_container(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size



dists = [d for d in pkg_resources.working_set]
module_with_size=[]
for dist in dists:
    try:
        path = os.path.join(dist.location, dist.project_name)
        size = calc_container(path)
        if size/1000 > 1.0:
            module_with_size.append((dist, size))
            # print (f"{dist}: {size/1000} KB or {size/1000000} MB")
            # print("-"*40)
    except OSError:
        '{} no longer exists'.format(dist.project_name)

module_with_size.sort(key=lambda x: x[1], reverse=True)
for module, size in module_with_size:
    print(f"{module}: {size/1000} KB or {size/1000000} MB")
    print("-"*40)
