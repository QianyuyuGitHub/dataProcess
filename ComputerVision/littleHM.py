import torch as pytc
import numpy as np
from PIL import Image
'''
This file is the homework of segmentation
'''

def get_mean(data_list):
    if data_list == []:
        return []
    data_list_dimension = len(data_list[0])
    instance_sum = []
    for count in range(data_list_dimension):
        instance_sum.append(0)

    instance_count = 0
    for instance in data_list:
        instance_count += 1
        for instance_dimension_index, instance_dimension_data in enumerate(instance):
            instance_sum[instance_dimension_index] += instance_dimension_data

    instance_mean = [sum_instance/instance_count for sum_instance in instance_sum]

    return  instance_mean

def get_theta(data_list, mean_list=None):
    if data_list == []:
        return []
    if len(data_list) == 1:
        result = []
        for i in range(len(data_list[0])):
            result.append(1.)
        return result
    data_list_dimension = len(data_list[0])
    instance_delta_sum = []
    for count in range(data_list_dimension):
        instance_delta_sum.append(0)

    if not mean_list:
        mean_list = get_mean(data_list)
    else:
        pass

    instance_count = 0
    for instance in data_list:
        instance_count += 1
        for instance_dimension_index, instance_dimension_data in enumerate(instance):
            instance_delta_sum[instance_dimension_index] += (instance_dimension_data - mean_list[instance_dimension_index])**2

    instance_theta = [np.sqrt(delta_sum/instance_count) for delta_sum in instance_delta_sum]

    return instance_theta

def get_minimal_data_range(data_list):
    '''
    Get the minimal data list (smaller than 1000)
    
    :param data_list: 
    :return: 
    '''
    minimal_list_length = len(data_list[0])
    minimal_list = []
    for i in range(minimal_list_length):
        minimal_list.append(1000)
    for point_data_pair in data_list:
        for index, item_single in enumerate(point_data_pair):
            if minimal_list[index] > item_single:
                minimal_list[index] = item_single
    return minimal_list

def get_maximal_data_range(data_list):
    '''
    Get the maximal data list (larger than -1000)

    :param data_list: 
    :return: 
    '''
    maximal_list_length = len(data_list[0])
    maximal_list = []
    for i in range(maximal_list_length):
        maximal_list.append(-1000)
    for point_data_pair in data_list:
        for index, item_single in enumerate(point_data_pair):
            if maximal_list[index] < item_single:
                maximal_list[index] = item_single
    return maximal_list

def graph_theoretic_clustering():
    pass

def get_initial_mean_theta_pairs(data_list, classes_expect_to_divide):
    '''
    :param data_list: 
    :param classes_expect_to_divide: This is how many parts you want to get for the final division result
    :return: 
    '''
    new_mean_pairs_list = []  # store seperate $classes_expect_to_divide$ number pairs of (mean, theta)
    new_theta_pairs_list = []  # store seperate $classes_expect_to_divide$ number pairs of (mean, theta)
    mean_list = get_mean(data_list)
    theta_list = get_theta(data_list, mean_list)
    minimal_list = get_minimal_data_range(data_list)
    maximal_list = get_maximal_data_range(data_list)

    for i in range(len(data_list[0])):  # dimension
        count = 0
        step = (maximal_list[i] - minimal_list[i]) / (classes_expect_to_divide+1)
        for j in range(classes_expect_to_divide):
            if i == 0:
                new_mean_pairs_list.append([(j+1)*step])
            else:
                new_mean_pairs_list[count].append((j+1)*step)
            count += 1

    for i in range(len(data_list[0])):  # dimension
        step = theta_list[i]
        count = 0
        for j in range(classes_expect_to_divide):
            if i == 0:
                new_theta_pairs_list.append([step])
            else:
                new_theta_pairs_list[count].append(step)
            count += 1

    return new_mean_pairs_list, new_theta_pairs_list

def calculate_the_possibility(data_list, mean_pair, theta_pair, class_num_of_division):
    '''
    
    :param data_list: 
    :param mean_pair: 
    :param theta_pair: 
    :param class_num_of_division: 
    :return: possibility[instance_count][class_count] = nultiplied_possibility_of_three_dimension
    '''
    ###################
    # p_of_all_class_and_all_instanc = []
    # for class_number in range(class_num_of_division):
    #     p_of_all_instance_with_all_dimension_in_one_class = []
    #     for instance in data_list:
    #         p_of_all_dimension_one_instance = []
    #         for index, single_dimension in enumerate(instance):  # repeat to check the instance $class_num_of_division$ times used for different possibility in corresponding part
    #             p_of_all_dimension_one_instance.append(np.exp(-((single_dimension-mean_pair[class_number][index])**2)/(2*theta_pair[class_number][index]**2)) / (theta_pair[class_number][index] * np.sqrt(2*np.pi)))
    #         p_of_all_instance_with_all_dimension_in_one_class.append(p_of_all_dimension_one_instance)
    #     p_of_all_class_and_all_instanc.append(p_of_all_instance_with_all_dimension_in_one_class)
    ####################

    possibility = []
    for instance in data_list:
        p_of_all_class_in_one_instance = []
        for class_number in range(class_num_of_division):
            p = 1.0
            for index, single_dimension in enumerate(instance):
                p *= 100*(np.exp(-((single_dimension-mean_pair[class_number][index])**2)/(2*theta_pair[class_number][index]**2)) / (theta_pair[class_number][index] * np.sqrt(2*np.pi)))
            p_of_all_class_in_one_instance.append(p)
        possibility.append(p_of_all_class_in_one_instance)

    return possibility

def Expectation_Maximization_clustring(data_list, classes_expect_to_divide):
    mean_pair, theta_pair = get_initial_mean_theta_pairs(data_list, classes_expect_to_divide)
    print(mean_pair)
    print(theta_pair)
    possibility_of_all_instance = calculate_the_possibility(data_list, mean_pair, theta_pair, classes_expect_to_divide)

    # for i in possibility_of_all_instance:
    #     print(i)

    classes_now_to_divide = classes_expect_to_divide
    rounds = 10
    for step in range(rounds):
        data_in_group = []
        data_in_group_index = []
        for i in range(classes_now_to_divide):
            data_in_group.append([])
            data_in_group_index.append([])

        group_tag_list = []
        for index in range(len(data_list)):
            max = 0.0
            max_index = 0
            for j in range(classes_now_to_divide):
                if max < possibility_of_all_instance[index][j]:
                    max = possibility_of_all_instance[index][j]
                    max_index = j
            group_tag_list.append(max_index)
        print(group_tag_list)

        for class_tag in range(classes_now_to_divide):
            for index, tag in enumerate(group_tag_list):
                if tag == class_tag:
                    data_in_group_index[class_tag].append(index)
                    data_in_group[class_tag].append(data_list[index])
        print(data_in_group)
        print(data_in_group_index)

        new_mean = []
        new_theta = []
        for class_tag in range(classes_now_to_divide):
            new_mean.append(get_mean(data_in_group[class_tag]))  # return mean[dimension]
            new_theta.append(get_theta(data_in_group[class_tag]))  # return theta[dimension]

        print("Mean:", new_mean)
        print("Theta", new_theta)
        classes_now_to_divide = 0
        mean_pair = []
        theta_pair = []
        for index, group_index in enumerate(data_in_group_index):
            if group_index != []:  # this class has points inside
                classes_now_to_divide += 1
                mean_pair.append(new_mean[index])
                theta_pair.append(new_theta[index])

        possibility_of_all_instance = calculate_the_possibility(data_list, mean_pair, theta_pair,
                                                                classes_now_to_divide)
        print("Possibility:", possibility_of_all_instance)

def main():
    data_test1 = [[1.,2.,3.], [34.,67.,90.], [3.,4.,5.], [4.,5.,6.], [22.,34.,15.], [1.,7.,30.], [0.0,0.0,0.0]]  # size 7
    # print(get_theta(data))
    im = Image.open('./dog1.jpg')
    print(type(im))
    # im.show()

    # Expectation_Maximization_clustring(data, 5)


if __name__ == '__main__':
    main()