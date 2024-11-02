from SetCoveringProblemCreator import *
import time
import random
# import matplotlib.pyplot as plt
# import statistics


POPULATION_SIZE = 50
MAX_TIME = 43
GENERATIONS = 400

def mutate(binary_string, mutation_rate):
    mutated_string = []
    
    for bit in binary_string:
        # print(random.random())
        # different mutation rate for included and excluded subsets
        if bit == '1':
            if random.random() < mutation_rate:
                mutated_bit = '1' if bit == '0' else '0'
            else:
                mutated_bit = bit
        else :
            if random.random() < mutation_rate/10:
                mutated_bit = '1' if bit == '0' else '0'
            else:
                mutated_bit = bit       
        mutated_string.append(mutated_bit)
    
    return ''.join(mutated_string)


def generate_random_binary_strings(n, count=POPULATION_SIZE):
    # keeping the choice for set bit to be 1 to 10 unset bits
    binary_strings = [''.join(random.choice('00000000001') for _ in range(n)) for _ in range(count)]
    return binary_strings

def fitness_score(strr,subsets , n ):
    my_set=set()
    cnt=0
    # print(type(subsets))
    for i in range(0,len(strr)):
        # print(type(subsets[i
        if(strr[i]=='1'):
            cnt=cnt+1
            # print(subsets[i])
            for item in subsets[i]:
                my_set.add(item)
    if(len(my_set)==100):
        return len(my_set) + 100*(n - cnt) # 
    else:
        return len(my_set)


def calc(strr):
    cnt = 0
    for i in range(0, len(strr)):
        if strr[i] == "1":
            cnt = cnt+1
    return cnt

def main():
    start_time = time.time()
    scp = SetCoveringProblemCreator()
    # mp = {}
    # gradually decreasing
    mutation_rate = 0.4
    
    subsets = scp.ReadSetsFromJson("scp_test.json") #Your submission program should read from scp_test.json file and provide a good solution for the SetCoveringProblem.
    # subsets = scp.Create(usize=100,totalSets=250)
    n=len(subsets)
    list=generate_random_binary_strings(n)

    fitval = []
    values = []
    for generations in range (GENERATIONS):
        fitval.clear()
        score=[]
        tfi = []
        for i in range(0,len(list)):
            score.append(fitness_score(list[i],subsets , n))
            tfi.append([fitness_score(list[i],subsets , n) , list[i]])
            sum=0
        for val in score:
            sum=sum+val
        for i in range(0,len(score)):
            score[i]=score[i]/sum 
        tfi.sort()
        tfi.reverse()
        # print(tfi)

        # elitism
        for i in range(0 , 10):
            fitval.append(tfi[i])
        # print(fitval)
        for _ in range(0,300):
            chosen_elements = random.choices(list, score, k=2) 
            rand_value=random.randint(0,n-1)
            #child1
            strr = ""
            strr+= chosen_elements[0][0:rand_value]
            strr+= chosen_elements[1][rand_value:]
            # fitval.append([fitness_score(strr,subsets , n),strr])
            strr = mutate(strr, mutation_rate)
            fitval.append([fitness_score(strr,subsets , n),strr])
            strr = ""
            #child2
            strr+= chosen_elements[1][0:rand_value]
            strr+= chosen_elements[0][rand_value:]
            strr = mutate(strr, mutation_rate)
            fitval.append([fitness_score(strr,subsets , n),strr])
        fitval.sort()
        fitval.reverse()
        print( "geneation: " + str(generations) + " fitness value " + str(fitval[0][0]))
        values.append(fitval[0][0])
        list1 = []
        for k in range(POPULATION_SIZE ):
            list1.append(fitval[k][1])
        list = list1
        mutation_rate = mutation_rate - 0.001
        end_time = time.time()
        elapsed_time = end_time - start_time
        if(elapsed_time > MAX_TIME):
            break

    bestresult = fitval[0][1]
    print("Roll No : 2021A7PS2567G")
    print("Number of subsets used in json file : " + str(n))
    print("Solution :")
    fans= [f'{i}:{bestresult[i]}' for i in range(n)]
    print(', '.join(fans))

    # for i in range(0, n):
    #     fans += str(i ) + ':' + tempo[i] + ', '
    # fans.pop()
    # print(fans)
    print("Fitness value of best state : " + str(fitval[0][0]))
    print("Minimum number of subsets that can cover the Universe-set : " + str(calc(fitval[0][1])))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")
    
    

if __name__=='__main__':
    main()