age= int(input())

def detailed_ageinfo(age):
    year=age//365
    r=age%365
    month=r//30
    r=r%30
    day=r
    print(f"{year} ano(s)", f"{month} mes(es)",f"{day} dia(s)",sep="\n")

detailed_ageinfo(age)    