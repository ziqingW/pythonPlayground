# It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.

# Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n = 8 and  Person 5 bribes Person 4 , the queue will look like this: 1,2,3,5,4,6,7,8.

# Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!


def minimumBribes(q):
    answer = 0
    for i in range(len(q), 0 , -1):
        if q[i-1] - i > 2:
            print("Too chaotic")
            return
        else:
            for j in range(max(0, q[i-1] - 2), i-1):
                if q[j] > q[i-1]:
                    answer += 1
    print(answer)