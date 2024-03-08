import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print("This programme will help you type faster. You will have to type the word 'programming' as fast as you can for five(5) times")
input("Press enter to continue.")

while len(times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if (word.lower() != "programming"):
        mistakes += 1

print("You made " + str(mistakes) + " mistake(s).")
print("Now let's see your evolution")
t.sleep(3)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend =["1", "2", "3", "4" "5"]
plt.xticks(x,legend)
plt.ylable("Time in seconds")
plt.xlabel("Attempts")
plt.title("Your typing evolution")
plt.show()
k = plt.show()
print(k)
