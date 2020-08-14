footage = int(input('How big is the pool: '))
series = int(input('How series: '))
sum = 0
for c in range (1,series+1):
    repetitions = int(input('How repetitions: '))
    sum += repetitions
    distance = footage * sum
print('You did {} meters'.format(distance))