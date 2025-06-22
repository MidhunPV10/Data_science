ipv1=int(input("Enter first octet : "))
ipv2=int(input("Enter second octet : "))
ipv3=int(input("Enter third octet : "))
ipv4=int(input("Enter fourth octet : "))

for i in range(0,5):
    if ipv4<255:
        ipv4+=1
    elif ipv4==255:
        if ipv3<255:
            ipv3+=1
            ipv4=0
        elif ipv3==255:
            if ipv2<255:
                ipv2+=1
                ipv3,ipv4=0,0
            elif ipv2==255:
                if ipv1<255:
                    ipv1+=1
                    ipv2,ipv3,ipv4=0,0,0
                elif ipv1==255:
                    ipv1,ipv2,ipv3,ipv4=0,0,0,0

    print(ipv1,ipv2,ipv3,ipv4)

