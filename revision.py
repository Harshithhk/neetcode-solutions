def productExceptSelf(nums):
    products_arr = []
    for num in nums:
        if not products_arr:
            products_arr.append(num)
        else:
            products_arr.append(products_arr[-1] * num)

    res = []

    print(products_arr)
    for i in range(len(products_arr) - 1, -1, -1):
       if not res:
           res.append(products_arr[i])
       else:
           
           res.append(products_arr[i-1]*nums[i+1])


productExceptSelf([1, 2, 3, 4])
