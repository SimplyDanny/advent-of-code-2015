from common import print_results, readlines


def powerlist(iterable):
    res_list = [[]]
    for l in iterable:
        res_list.extend([subset + [l] for subset in res_list])
    return res_list

containers = map(int, readlines(__file__))

pos = [len(l) for l in powerlist(containers) if sum(l) == 150]

print_results(len(pos), pos.count(min(pos)))
