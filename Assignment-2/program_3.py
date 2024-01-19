# Question: Write a program, which reads heights (inches.) of customers into a list and convert these heights to centimeters in a separate list using: 
#  1) Nested Interactive loop. 
#  2) List comprehensions 

l =  [150,155, 145, 148]
 
def inch_to_cms(l):
    output1 = []
    output2 = []
    # Nested Interactive loop
    for i in l:
        output1.append(round(i / 2.54,2))

    # List comprehensions   
    output2 = [round(i/2.54,2) for i in l]
       
    print("Output from Nested Interactive Loop: {}, Output from List Comprehensions:{}".format(output1,output2))

if __name__ == "__main__":
  inch_to_cms(l)
