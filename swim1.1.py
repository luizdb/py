footage = int(input('How big is the pool: '))
series = int(input('How series: '))
sum = 0
fs = int(input('How repetitions in first shot: '))
shot = fs*footage
print('The fist shot was: {}'.format(shot))
for c in range (1,series+1):
    repetitions = int(input('How repetitions: '))
    sum += repetitions
    distance = footage * sum
print('You did {} meters'.format(distance))
