""" Create a function that takes a positive integer and returns the next
bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1 """


def next_bigger(n):
    n = list(str(n)[::-1])

    for idx, val in enumerate(n):
        next_ = idx + 1

        if next_ == len(n):
            break

        if n[idx] > n[next_]:
            unchanged = n[next_:]
            changed = n[:next_]
            changed = sorted(changed)

            for i, v in enumerate(changed):
                if v > unchanged[0]:
                    changed[i], unchanged[0] = unchanged[0], changed[i]
                    break

            unchanged = unchanged[::-1]
            merged = unchanged + changed

            return int(''.join(map(str, merged)))
    return -1
