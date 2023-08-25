from xml.dom import minidom

myTree = minidom.parse("ltl.xml")
group= myTree.documentElement
tr=group.getElementsByTagName('template')
golbal_variables = myTree.getElementsByTagName('declaration')
file = open ("mycode.txt", 'w')
# print("---------- global variables--------------------:")
# for x in golbal_variables:
#     print(x.firstChild.data)
# print("-----------------------------------------------:")
for t in tr :
    name= t.getElementsByTagName('name')[0].childNodes[0].nodeValue
    # transitions= t.getElementsByTagName('transition')[0].childNodes[0].nodeValue
    # source= t.getElementsByTagName('source')
    # destination= t.getElementsByTagName('target')
    lentgh = t.getElementsByTagName('label')[0].childNodes[0].nodeValue
    LTL= t.getElementsByTagName('label')[1].childNodes[0].nodeValue


    print("-------------------------MINIZINC CODE----------------------")
    # print(f"Name: {name}")

    #    ref= s.getAttribute("ref")
    #    print(f"Source: {ref}")
    # for tr in destination:
    #     d = tr.getAttribute("ref")
    #     print(f"Destination: {d}")
    # print(f"LENTGH OF TRACE IS : {lentgh}")
    # print(f"LTL Fromula: {LTL}")
    if LTL == "P":
        file.write(f"predicate P ( array[0..{lentgh}] of var 0..1:q)=\nq[0]=1;")
        print(f"predicate P ( array[0..{lentgh}] of var 0..1:q)=q[0]=1;")
        file.write('\n\n')
    if LTL == "G":
        file.write(f"predicate G( array[0..{lentgh}] of var 0..1:q)=\nforall (i in 0..{lentgh})(q[i]=1);")
        print(f"predicate G( array[0..{lentgh}] of var 0..1:q)= forall (i in 0..{lentgh})(q[i]=1);")

        file.write('\n\n')


    if LTL == "F":
        file.write(f"predicate F( array[0..{lentgh}] of var 0..1:q)= \nexists (i in 0..{lentgh})(q[i]=1);")
        print(f"predicate F( array[0..{lentgh}] of var 0..1:q)= exists (i in 0..{lentgh})(q[i]=1);")
        file.write('\n\n')
    if LTL == "X":
        file.write(f"predicate X( array[0..{lentgh}] of var 0..1:q)=\nq[1]=1;")
        print(f"predicate X( array[0..{lentgh}] of var 0..1:q)=q[1]=1;")
        file.write('\n\n')
    if LTL == "U":
         file.write(f"predicate U( array[0..{lentgh}] of var 0..1:q1,array[0..{lentgh}] of var 0..1:q2)=\n"
                    f" exists(j in 0..n) (forall(i in 0..j-1)((q2[i] =1 and q1[j]=1) ));")
         print(f"predicate U( array[0..{lentgh}] of var 0..1:q1,array[0..{lentgh}] of var 0..1:q2)="
               f"exists(j in 0..n) (forall(i in 0..j-1)((q2[i] =1 and q1[j]=1) ));")
         file.write('\n\n')
    if LTL == "GF":
        file.write(f"predicate GF( array[0..{lentgh}] of var 0..1:q)=\n"
                   f" exists(j in 0..n) (forall(i in j+1..n)((q[i] =1 /\ q[j]=1) ));")
        print(f"predicate GF( array[0..{lentgh}] of var 0..1:q)="
              f"exists(j in 0..n) (forall(i in j+1..n)((q[i] =1 /\ q[j]=1) ));")
        file.write('\n\n')
    if LTL == "FG":
        file.write(f"predicate FG( array[0..{lentgh}] of var 0..1:q)= \n"
                   f"forall(j in 0..n) (exists(i in j+1..n)((q[i] =1 /\ q[j]=1) ));")
        print(f"predicate FG( array[0..{lentgh}] of var 0..1:q)= forall(j in 0..n) (exists(i in j+1..n)((q[i] =1 /\ q[j]=1) ));")

print("------------------------------------------------------------")
























