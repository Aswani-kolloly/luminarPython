students=['aswani','abhi','anju','anjaley']
failed=['aswani','abhi']
passed=set(students).difference(set(failed))
print("Passed students: ",passed)