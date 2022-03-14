def count_find_num(prime_nums, limit):
    mult = eval('*'.join(map(str, prime_nums)))

    if mult > limit:
        return []

    ret_list = [mult]

    for x in prime_nums:
        max_mult = mult

        while max_mult * x <= limit:
            ret_list.append(max_mult * x)
            max_mult = max_mult * x

    for n in ret_list:
        for p in prime_nums:
            if n * p <= limit:
                if n * p not in ret_list:
                    ret_list.append(n * p)

    ret_list.sort()

    return [ret_list.__len__(), ret_list[-1]]


# def count_find_num(primes_list, limit):
#     res = set()
#
#     def search(i, prod):
#         if prod > limit:
#             return
#         if i == len(primes_list):
#             res.add(prod)
#             return
#         search(i, prod * primes_list[i])
#         search(i + 1, prod * primes_list[i])
#
#     search(0, 1)
#     return res and [len(res), max(res)] or []
