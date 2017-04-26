def health_calculator(age, apples, cigs):
    answer=(100-age) + (apples * 3.5) - (cigs * 2)
    print(answer)


cam_data = [27,20,0]

health_calculator(cam_data[0], cam_data[1], cam_data[2])
## takes too long
health_calculator(*cam_data)
#unpack arguments, make sure they are in the same format
