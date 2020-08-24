footage = int(input('How big is the pool: '))
series = int(input('How series: '))
sum = 0
fs = int(input('How repetitions in best shot: '))
shot = fs*footage

for c in range (1,series+1):
    repetitions = int(input('How repetitions: '))
    sum += repetitions
    distance = footage * sum
print('The best shot was: {}'.format(shot))
print('You did {} meters'.format(distance))
