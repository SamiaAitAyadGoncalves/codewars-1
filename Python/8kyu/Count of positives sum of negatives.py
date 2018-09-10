# https://www.codewars.com/kata/576bb71bbbcf0951d5000044
#
# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#
# If the input array is empty or null, return an empty array:
#
#     C#/Java: new int[] {} / new int[0];
#     C++: std::vector<int>();
#     JavaScript/CoffeeScript/TypeScript/PHP/Haskell: [];
#     Rust: Vec::<i32>::new();
#
# ATTENTION!
#
# The passed array should NOT be changed. Read more here.
#
# For example:
#
# input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# return [10, -65].


def count_positives_sum_negatives(arr):
    if len(arr)==0:
        return []
    else:
        a=0
        b=0
        for i in range(len(arr)):
            if arr[i]>0:
                a+=1
            else:
                b+=arr[i]
        return [a,b]
