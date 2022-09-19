import parsedatetime as pdt
from datetime import datetime

cal =pdt.Calendar()

examples = [
        '19 November 1975',
        '19 November 75',
        '19 Ноя 75',
        'tomorrow',
        'вчера',
        '10 minutes from now',
        'three months ago',
        '2 weeks and 3 days in the future',]

print ('\nNow: {}'.format(datetime.now().ctime()), end='\n\n')
print ('{0:^50s}{1:<20s}'.format('Input', 'Result'))
print ('=' * 70)

for e in examples:
    dt, result = cal.parseDT(e)
    print('{:<30s}{:>40}'.format(e,dt.ctime()))
