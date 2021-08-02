if __name__ == '__main__':
    n = int(input())
    total= 0
    prom = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    for student in student_marks:
       if student == query_name:
        for note in student_marks[query_name]:
            print(note)
            total += note
            print(total)
        
    prom = total/n
            
    print("{0:.2f}".format(prom))       
        
