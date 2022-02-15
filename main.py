from matplotlib import pyplot as plt

seed = input('Write positive integer number: ')
num = int(seed)

steps = 0

results = []
results.append(int(num))

while num != 1:
    if int(num) == 1:
        results.append(int(num))
        #print(f'{num}')
        break
    elif int(num) % 2 == 0:
        num = int(num / 2)
        results.append(int(num))
        steps += 1
        #print(f'{num}')
    elif int(num) % 2 != 0:
        num = (int(num) * 3) + 1
        results.append(int(num))
        steps += 1
        #print(f'{num}')

print(f'Finished in {steps} steps.')

plt.figure('3N+1')
plt.xlabel('steps')
plt.ylabel('log')
plt.title(f'Seed: {seed}')
plt.yscale('log')

plt.plot(results)
plt.show()
