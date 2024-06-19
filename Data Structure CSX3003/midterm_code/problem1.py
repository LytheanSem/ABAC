def can_reserve(new_time, reservation_list, k):
    left = 0
    right = len(reservation_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if abs(reservation_list[mid] - new_time) <= k:
            return False
        elif reservation_list[mid] < new_time:
            left = mid + 1
        else:
            right = mid - 1

    return True


def add_reservation(reservation_list, new_time):
    reservation_list.append(new_time)
    reservation_list.sort()
    return reservation_list


k, t = map(int, input().split())
R = list(map(int, input().split()))

if t < R[-1] and can_reserve(t, R, k):
    R = add_reservation(R, t)
    print(" ".join(map(str, R)))
else:
    print("Rejected")
