def has_tags(tags):
    for tag in tags:
        if tag != -1:
            return True
    return False

def solution(path, unique_len):
    result = []
    with open(path) as fh:
        for line in fh.readlines():
            buf = [' ' for _ in range(unique_len)]
            # tags = [-1 for _ in range(unique_len)]
            for ix, ch in enumerate(line):
                buf[ix%unique_len] = ch
                # # optimisation: don't need a full check if an existing duplicate still exists
                # if tags[ix%unique_len] != -1:
                #     if buf[ix%unique_len] != buf[tags[ix%unique_len]]:
                #         tags[tags[ix%unique_len]] = -1
                #         tags[ix%unique_len] = -1
                # if has_tags(tags) or ' ' in buf:
                #     continue  # still-existing duplicate

                # existing duplicates have been resolved, perform full check
                if ' ' not in buf:
                    unique = True
                    for chk_ix1 in range(unique_len-1):
                        for chk_ix2 in range(chk_ix1+1, unique_len):
                            if buf[chk_ix1] == buf[chk_ix2]:
                                # tags[chk_ix1] = chk_ix2
                                # tags[chk_ix2] = chk_ix1
                                unique = False
                    # if not has_tags(tags) and ' ' not in buf:
                    if unique:
                        result.append(ix+1)
                        break
    return result

# Day 1
_t = solution('sample.txt', 4)
assert _t == [7, 5, 6, 10, 11], _t
print('Ok')
print(f"Part 1 -> {solution('input.txt', 4)}")

# Day 2
_t = solution('sample.txt', 14)
assert _t == [19, 23, 23, 29, 26], _t
print('Ok')
print(f"Part 2 -> {solution('input.txt', 14)}")
