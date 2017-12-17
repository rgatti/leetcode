# https://leetcode.com/problems/my-calendar-iii/description/
#
# Implement a MyCalendarThree class to store your events. A new event can
# always be added.
#
# Your class will have one method, book(int start, int end). Formally, this
# represents a booking on the half open interval [start, end), the range of
# real numbers x such that start <= x < end.
#
# A K-booking happens when K events have some non-empty intersection (ie.,
# there is some time that is common to all K events.)
#
# For each call to the method MyCalendar.book, return an integer K
# representing the largest integer such that there exists a K-booking in the calendar.
#
# Your class will be called like this: MyCalendarThree cal = new MyCalendarThree(); MyCalendarThree.book(start, end)
#
# Example:
######
# MyCalendarThree.book(10, 20); // returns 1
# MyCalendarThree.book(50, 60); // returns 1
# MyCalendarThree.book(10, 40); // returns 2
# MyCalendarThree.book(5, 15); // returns 3
# MyCalendarThree.book(5, 10); // returns 3
# MyCalendarThree.book(25, 55); // returns 3



# Naive approach ...
#
# 1. Track start/end values and max K
# 2. For each booking search all existing bookings for ovlerlaps
# 3. Compare to max K
#
# Time complexity O(n), increases with every booking

from random import randrange

starts = []
ends = []
max_k = 0

def find_overlaps(s,e):
    k = 1
    global max_k
    for i in range(len(starts)):
        if s <= starts[i] and e > starts[i]:
            k += 1
        elif s < ends[i] and e > ends[i]:
            k += 1
        elif s >= starts[i] and e < ends[i]:
            k += 1
    max_k = max(k, max_k)
    return (k, max_k)

def add_booking(s,e):
    starts.append(s)
    ends.append(e)

def book(s,e):
    if e < s:
        s, e = e, s
    local_k, max_k = find_overlaps(s,e)
    add_booking(s,e)
    print('start: {0:9d} | end: {1:9d} | k: {2:5d}, {3:5d} (local)'.format(s, e, max_k, local_k))

# From example
book(10,20)
book(50,60)
book(10,40)
book(5,15)
book(5,10)
book(25,55)

# Generate random bookings
for b in range(0, 400):
    book(randrange(0, 10**9), randrange(0, 10**9))
