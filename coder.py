# Your code here
# Read the input ratings as integers
a, b, c, d = map(int, input().split())

if a<b and a>c and a>d or a<d and a>c and a>b or a<c and a>b and a>d:
    print("Anubhav")
elif b<a and b>c and b>d or b<c and b>a and b>d or b<d and b>c and b>a:
    print("Anuj")
elif c<a and c>b and c>d or c<b and c>a and c>d or c<d and c>b and c>a:
    print("Gaurav")
elif d<a and d>b and d>c or d<c and d>b and d>a  or d<b and d>a and d>c :
    print("Ramandeep")
