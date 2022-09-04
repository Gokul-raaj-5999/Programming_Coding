def fun(s):
    if s.count('@')==1 and s.count('.')==1:
        un,we=s.split('@')
        we,ex=we.split('.')
        if  not (len(un)>0 and len(we)>0 and we.isalnum() and len(ex)<=3):return False
        for i in un:
            if  not (i.isalpha() or i.isdigit() or i in ['-','_']):return False
        return True
    return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

###################################################################################################
"""
SAMPLE1:
  INPUT:
    3
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  OUTPUT:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

SAMPLE2:
    INPUT:
        2
        harsh@gmail
        iota_98@hackerrank.com
    OUTPUT:
        ['iota_98@hackerrank.com']

"""
