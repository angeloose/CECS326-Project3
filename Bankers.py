# CECS 326 Xu
# Project 3
# Group members: Angelo Cervana (029977556)


def main():
    # initialize processes

    n = 5   # number of processes
    m = 3   # number of resource types

    # available vector/initial resources
    avail = [3, 3, 2]

    # maximum matrix
    max = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    # allocation matrix
    alloc = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    # need matrix (max - alloc)
    need = [
        [7, 4, 3],
        [1, 2, 2],
        [6, 0, 0],
        [0, 1, 1],
        [4, 3, 1]
    ]

    # safety algorithm
    finish = [False] * n    # initialize finish states for processes
    safe_sequence = [0] * n
    ss_index = 0
    
    for _ in range(n):      # loop n * n times to ensure whether a process is found with appropriate resources
        for i in range(n):
            if finish[i] == False:  # check process if it has not been checked yet
                safe = True
                for j in range(m):
                    if need[i][j] > avail[j]:   # compare needed resources to available
                        safe = False
                        break 

                # if needed resources are less than available resources
                if safe == True:
                    # assign process i to safe sequence
                    safe_sequence[ss_index] = i
                    ss_index += 1


                    # deallocate needed resources from process i and add to available resources
                    for x in range(m):
                        avail[x] += need[i][x]
                
                    # change finish state of process i to true
                    finish[i] = True

    print("Safe Sequence:", safe_sequence)
    

    # resource-request algorithm

    # initialize test cases 1 and 2
    resource_requests = [
        [1, 0, 2, 1],    # the last index represents the process number
        [3, 3, 1, 4]    # ex: [3, 3, 1, 4] = process 4 requests [3, 3, 1]
    ]

    for i in range (2):
        process = resource_requests[i][3]
        for j in range(m):
            if resource_requests[i][j] <= need[process][j]:
                continue
            else:
                print("Error: Request is larger than needed resources for process.")

        for k in range(m):
            if resource_requests[i][j] <= avail[j]:
                continue
            else: 
                print("Not enough available resources currently, process must wait.")
            
        print("Resources may be allocated to process {} \nrequest_resources({})".format(process, process))

            # allocate resources










# run main
main()