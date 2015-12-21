#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""Student selection process"""


from student_data import *
import pprint


def passed_exam(student_list):
    """This function will filter and selct students for medical program.

    Args:
        final_selections(list): This list will have students with 125 and higer.

    Return:
        retrurns students list.
    """      
    selected_list = []
    
    for student in student_list:
        if student[1] > 125:
            selected_list.append(student)
    return selected_list


                     
    if __name__ == '__main__':
        import doctest
        doctest.testmod()
   

def final_list(final_selections):
    """This function will filter and selct students who has passed interview.

    Args:
        final_selections(list): This list will have students with high MACT and 
        passed interviews.

    Return:
        retrurns students list.

    Examples:
        >>> fianl_list(student_list)
        ('Tomas', 126),
        ('Amy', 130),
        ('Dave', 130),
        ('Justin', 130),
        ('Joseph', 134),
        ('James', 140),
        ('Sumon', 160),
        ('Smith', 165)]
    """
    final_selections = passed_exam(student_list)
    final_round=[]

    for item in final_selections:
        passed=raw_input('passed the interview '+str(item[0])+' with MCAT '
                   +str(item[1])+' (enter n for no, y for yes: )')
        final_round.append(passed)


  
    final_list=[]
    for score in range(0,len(final_round)):
        if final_round[score]=='y':
            final_list.append(final_selections[score])


    final_list.sort(key=lambda tup: tup[1])

    print('Student sorted in increasing order of their GPA: ')
    final_list.insert(0, final_list)
    pprint.pprint(final_list)
