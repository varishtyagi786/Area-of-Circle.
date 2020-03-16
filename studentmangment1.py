student(sid,fname,lname, cc1,mark1,cc2,mark2,cc3,mark3,cc4,mark4,cc5,mark5,cc6,mark6)
"""Constructor for student"""
return [sid,[fname,lname],[(cc1,mark1),(cc2,mark2),(cc3,mark3),(cc4,mark4),(cc5,mark5),(cc6,mark6)]]
 
def get_id(std):
    """Returns students ID"""
    return std[0]
 
def get_name(std):
    """Returns students Name"""
    return std[1]
 
def get_courses(std):
    """Returns a list of tuples of course codes and grade"""
    return std[2]
 
def get_fname(name):
    """Returns first name"""
    return name[0]
 
def get_lname(name):
    """Returns last name"""
    return name[1]
 
def get_ccode(course_det):
    """Returns course code part of the tuple"""
    return course_det[0]
 
def get_grade(course_det):
    """Returns grade part of the tuple"""
    return course_det[1]
 
       
st1=student("620000101","John","Doe","CS11Q",80,"CS11R",60,"CS20R",50,"CS20S",60,"CS22Q",65,"CS23Q",80)
 
credit_list={'CS11Q':6,'CS11R':6,'CS20R':4,'CS23Q':4,'CS22Q':4,'CS20S':4}
 
qp_list = {"A+":4.3,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.7,"D+":1.3,"D": 1.0,"F": 0.0}
        
 
## For this fucntion to work you first need to write calc_gpa()
def print_students_gpa(std):
    """Prints the students details and GPA"""
    print ("Student Id:", get_id(std))
    print ("Student name:", get_fname(get_name(std)), get_lname(get_name(std)))
    print ("GPA: %.2f" %(calc_gpa(std)))
 
 
def compute_letter_grade(num):
    if(num > 85):
        return 'A+'
    elif(num >=70 and num <= 85):
        return 'A'
    elif(num >= 67 and num <= 69):
        return 'A-'
    elif(num >= 63 and num <= 66):
        return 'B+'
    elif(num >= 60 and num <= 62):
        return 'B'
    elif(num >= 57 and num <= 59):
        return 'B-'
    elif(num >= 53 and num <= 56):
        return 'C+'
    elif(num >= 50 and num <= 52):
        return 'C'
    elif(num >= 47 and num <= 49):
        return 'C-'
    elif(num >= 43 and num <= 46):
        return 'D+'
    elif(num >= 36 and num <= 42):
        return 'D'
    elif(num <= 35):
        return 'F'
 
 
def calc_letter_grade(student):
    course = []
    courselist=get_courses(student)
    number_grade= [x[1] for x in courselist]
    course_code= [x[0] for x in courselist]
    letterGrade=map(compute_letter_grade,number_grade)
    course=zip(course_code,letterGrade)
    return course
 
 
def convert_to_wtqp(codegrade):
    result1 = 0
    result2 = 0
    
    for my_key_cc,my_value_cc in credit_list.items():
        if my_key_cc == get_ccode(codegrade).upper():
            result1 = my_value_cc
 
            
    for my_key_lgrade,my_value_lgrade in qp_list.items():
        if my_key_lgrade == get_grade(codegrade):
            result2 = my_value_lgrade
            
    return (result1,result2)
 
 
def calc_gpa(std):
    cc_grade_point = []
    cc_credit_weight = []
    cc_lgrade_value = []
    result = 0
 
    lst_cc_lgrade = calc_letter_grade(std)
 
    for i in lst_cc_lgrade:
        cc_lgrade_value.append(convert_to_wtqp(i))
    
    for i in cc_lgrade_value:
        cc_grade_point.append(i[0]*i[1])
    
    for i in cc_lgrade_value :
        cc_credit_weight.append(i[0])
 
         
    result=(sum(cc_grade_point)/sum(cc_credit_weight))
 
    return result