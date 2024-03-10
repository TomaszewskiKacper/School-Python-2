import matplotlib.pyplot as plt

ratings = [15.63, 11.17, 10.70, 8.95, 7.54, 3.38, 1.92, 1.56, 1.46, 1.42, 1.39, 1.32, 1.24, 1.22, 1.22]
names = ["Python", "C", "C++", "Java", "C#", "JavaScript", "SQL", "Go", "Scratch", "Visual Basic", "Assembly language", "PHP", "MATLAB", "Fortran", "Delphi/Object Pascal"]

plt.figure(figsize=(10,6))
plt.bar(names, ratings, edgecolor = "black", linewidth = 2) #bar plot
plt.xticks(rotation = 45, ha = "right", fontsize = 8)   #rotate names
plt.title("Popularmosc jezykow programowania")  
plt.xlabel("Jezyk programowania")
plt.ylabel("Popularnosc [%]")
plt.tight_layout()
plt.show()