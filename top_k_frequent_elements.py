def topKFrequent( nums, k):
    count_map = {}
    bucket_array = [[]for i in range(len(nums)+1)]
    print(bucket_array)
    for i,num in enumerate(nums):
        current_count = count_map.get(num,0)
        count_map[num] = current_count + 1     
    print(count_map)

    for key,value in count_map.items():
        bucket_array[value].append(key)

    print(bucket_array)

    top_k_frequent_element = []
    for i in range(len(bucket_array)-1, -1, -1):
        if len(bucket_array[i]):
            top_k_frequent_element.append(bucket_array[i])
        
        if len(top_k_frequent_element) == k:
            return top_k_frequent_element




res = topKFrequent([1,1,1,2,2,3],2)
print("RES :", res)