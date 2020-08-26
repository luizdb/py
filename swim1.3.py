footage = int(input('How big is the pool: '))
series = int(input('How series: '))
time = int(input('How time you swim (minutes): '))
sum = 0
fs = int(input('How repetitions in best shot: '))
shot = fs*footage
for c in range (1,series+1):
    repetitions = int(input('How repetitions: '))
    sum += repetitions
    distance = footage * sum
    media = (distance / time)/60
print('The best shot was: {}'.format(shot))
print('You did {} meters'.format(distance))
print('You media time is {} minutes/meter'.format(media))
