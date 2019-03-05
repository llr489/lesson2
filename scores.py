students_scores = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, 
    {'school_class': '4b', 'scores': [5, 3, 4, 4, 1, 2]}, 
    {'school_class': '5a', 'scores': [4, 5, 5, 3]},
    {'school_class': '5b', 'scores': [4, 4, 3, 5, 3, 2, 4, 4, 3]}
    ]

def count_average(students_scores):
    sum_school = 0
    school_counter = 0
    
    for i_class in students_scores:
        sum_class = 0
        
        for score in i_class['scores']:
            sum_class += score
            sum_school += score
        
        school_counter += len(i_class['scores'])
        average_class = sum_class / len(i_class['scores'])
        print(f"Средняя оценка по классу {i_class['school_class']}: {average_class}")
    
    average_school = sum_school/school_counter
    print(f"Средняя оценка по школе: {average_school}")

count_average(students_scores)

