# https://www.codewars.com/kata/59f70440bee845599c000085
#
# Someone was hacking the score. Each student's record is given as an array The objects in the array are given again as an array of scores for each name and total score. ex>
#
# array = [
# ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
# ["name2", 140, ["B", "A", "A", "A"]],
# ["name3", 200, ["B", "A", "A", "C"]]
# ]
#
# The scores for each grade is:
#
#     A: 30 points
#     B: 20 points
#     C: 10 points
#     D: 5 points
#     Everything else: 0 points
#
# If there are 5 or more courses and all courses has a grade of B or above, additional 20 points are awarded. After all the calculations, the total score should be capped at 200 points.
#
# Returns the name of the hacked name as an array when scoring with this rule.
#
# var array = [
# ["name1", 445, ["B", "A", "A", "C", "A", "A"]], # name1 total point is over 200 => hacked
# ["name2", 140, ["B", "A", "A", "A"]], #  name2 point is right
# ["name3", 200, ["B", "A", "A", "C"]] # name3 point is 200 but real point is 90 => hacked
# ];
#
# return ["name1", "name2"]


def find_hack(arr):
    hacked_list = []
    grades = ['A', 'B', 'C', 'D']
    points = [30, 20, 10, 5]
    extra = 20

    for i in range(len(arr)):
        hacked = False
        grade_count = [0, 0, 0, 0]
        p = 0
        for j in range(len(arr[i][2])):
            for k in range(4):
                if grades[k] == arr[i][2][j]:
                    p += points[k]
                    grade_count[k] +=1
        if (grade_count[0]+grade_count[1]) == len(arr[i][2]) and len(arr[i][2]) >= 5:
            p += extra
        if p > 200:    #most important line in the code..
            p = 200

        if arr[i][1] != p:
           hacked = True
        if arr[i][1] > 200:
            hacked = True

        if hacked == True:
            hacked_list.append(arr[i][0])
    return hacked_list
