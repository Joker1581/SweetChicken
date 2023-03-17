def sweet_chicken(num_flowers, num_chicken, num_universal):
    if num_universal == 0:
        return min(num_chicken, num_flowers)//2
    else:
        for i in range(num_universal):
            if num_chicken <= num_flowers:
                num_chicken += 1
            else:
                num_flowers += 1
        return min(num_chicken, num_flowers)//2

print(sweet_chicken(10,4,2))