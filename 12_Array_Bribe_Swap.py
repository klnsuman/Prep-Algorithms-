
'''
Player Can move forward in Queue by Paying Bribe. If there are more than 2 Bribes , then Print Chaotic. Else print Moves Done.
 I/p : [1,2,3,5,4] 
o/p : 1 Move
'''
def minBribes(q):
    # Write your code here
    moves = 0
    is_chaotic = False

    for j, P in enumerate(q, 1):
        #if (P > j):
        #    moves = moves + (P - j)
        if (P - j > 2):
            is_chaotic = True

        for k in range(max(P-1, 0), j-1):
            if q[k] > P:
                moves += 1

    if is_chaotic:
        print("Too chaotic")
    else:
        print(moves)

def minimumBribes(Q):
    #
    # initialize the number of moves
    moves = 0
    #
    # decrease Q by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our
    # indices.  (Not necessary but makes it easier to
    # understand.)
    #Q = [P-1 for P in Q]
    #
    # Loop through each person (P) in the queue (Q)
    for i,P in enumerate(Q,1):
        # i is the current position of P, while P is the
        # original position of P.
        #
        # First check if any P is more than two ahead of
        # its original position
        if P - i > 2:
            print("Too chaotic")
            return
        #
        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front if P's original position,
        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1
    print(moves)

Q = [1,2,5,3,7,8,6,4]
#print(minBribes(Q))
print("::::::::")
minimumBribes(Q)

[1,2,3,4,5,6,7,8]
[1,2,5,3,4,6,7,8] #= 2
[1,2,5,3,6,4,7,8] #= 1
[1,2,5,3,6,7,4,8] #= 1
[1,2,5,3,6,7,8,4] #= 1
[1,2,5,3,7,8,6,4] #= 2

[1,2,3,4,5,6,7,8]
