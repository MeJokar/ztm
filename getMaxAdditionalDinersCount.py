# Write any import statements here

def getMaxAdditionalDinersCount(N, K, M, S):
  # Write your code here
  i = 0
  S= set(S)
#   S = S.sort()
  empty_seats = 0
  empty_seats_list = []
  while i < N:
    #if i != taken_seat and
    seat_open = True 
    if i+1 in S:
        seat_open = False
    else: 
        for j in range(-K,K+1,1):
            if i+1+j in S:
                seat_open = False
                break
    if seat_open:
      empty_seats +=1
      empty_seats_list.append(i+1)
      i += K+1
    else:
      i +=1
  print(i)    
  return empty_seats, empty_seats_list


def getMaxAdditionalDinersCount1(N, K, M, S):
  # Write your code here
  i = 0
  empty_seats = 0
  empty_seats_list = []
  while i < N:
    #if i != taken_seat and
    seat_open = True 
    if i+1 in S:
        seat_open = False
    elif any(j+1 in S for j in range(max(1, i-K),i)) or any(j+1 in S for j in range(i+1,min(N+1, i+K+1))):
        #for j in range(0,K+1):
           # if (i+1+j in S) or (i+1-j) in S:
        seat_open = False
             # break
    if seat_open:
      empty_seats +=1
      empty_seats_list.append(i+1)
      i += K+1
    else:
      i +=1
  return empty_seats, empty_seats_list

def getMaxAdditionalDinersCount2(N, K, M, S):
  # Write your code here
  i = 0
  empty_seats = 0
  empty_seats_list = []
  while i < N:
    #if i != taken_seat and
    if M == 0: 
      empty_seats = N // (K+1) 
      return empty_seats
    if (i+1 in S) or any(j+1 in S for j in range(max(1, i-K),i)) or any(j+1 in S for j in range(i+1,min(N+1, i+K+1))):
      i +=1
    else:
      empty_seats +=1
      empty_seats_list.append(i+1)
      i += K+1
  return empty_seats, empty_seats_list


def getMaxAdditionalDinersCount3(N, K, M, S):
    # Write your code here
    i = 0
    empty_seats = 0
    empty_seats_list = []
    if M == 0: 
        empty_seats = N // (K+1) 
        return empty_seats
    while i < N:
        current_seat_open = True
        if (i+1 in S):
            current_seat_open = False
            S.remove(i+1)
            i += K+1
        elif S: 
            for j in range(1,K+1):
                if i+1+j in S:
                    S.remove(i+1+j)
                    i += j+K+1
                    current_seat_open = False
                    break
                elif i+1-j in S:
                    S.remove(i+1-j)
                    i +=1
                    current_seat_open = False
                    break
            if not(S):
               print('sfsd;lshdf')
            #    i += K
        if current_seat_open:
            empty_seats +=1
            empty_seats_list.append(i+1)
            i += K+1
    return empty_seats, empty_seats_list


def getMaxAdditionalDinersCount4(N, K, M, S):
    i = 0
    empty_seats = 0
    while i < N:
        if M == 0: 
            empty_seats = N // (K+1) 
            return empty_seats
        if i+1 in S:
            i += 1
            continue
        range_start = max(1, i-K)
        range_end = min(N+1, i+K+2)
        has_taken_seat = False
        for j in range(range_start, i):
            if j+1 in S:
                has_taken_seat = True
                break
        if not has_taken_seat:
            for j in range(i+1, range_end):
                if j in S:
                    has_taken_seat = True
                    break
        if not has_taken_seat:
            empty_seats += 1
            i += K+1
        else:
            i += 1
    return empty_seats
      
if __name__ == '__main__': 
    print(getMaxAdditionalDinersCount4(10,1,2, [2,6]))
    print(getMaxAdditionalDinersCount4(15,2,3, [11,6,14]))
    print(getMaxAdditionalDinersCount4(10,2,0, []))



