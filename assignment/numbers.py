def main():
    detail = dict()
    person=int(input("Enter number of salesman : "))
    for i in range(person):
        print()
        print("Enter sales of salesman ",i+1)
        ''' w1=float(input("Enter sale for week 1 : "))
        w2=float(input("Enter sale for week 2 : "))
        w3=float(input("Enter sale for week 3 : "))
        w4=float(input("Enter sale for week 4 : "))'''
        weeks = [1000,500,600,700]
        detail[i] = weeks
    sales = sales_calc(detail)

def sales_calc(detail):
    result = dict()
    for k in detail:
        print(k)
        tS = sum(detail[k])
        if tS>50000:
            com=tS/20
        else:
            com=0
        if tS>=80000:
            remark="Excellent"
        elif 60000<=tS<80000:
            remark="Good"
        elif 40000<=tS<60000:
            remark="Average"
        else:
            remark="Work Hard"
        result[k] = [tS,com,remark]
    
    return result

main()