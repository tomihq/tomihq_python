num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11];
count = 0;
for idx, num in enumerate(num_list):
    count+=1;

    if num==36:
        print('Number found at position: ' + str(idx));
        break;
    if num>45:
        print("Over 45: " + str(num));
    elif(num<45):
        print("Under 45: " +str(num));
    

print(count);

