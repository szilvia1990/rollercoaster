import pandas as pd
import matplotlib.pyplot as plt


# load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

print(wood.head())

# write function to plot rankings over time for 1 roller coaster here:
def ranking_over_time(name, data_frame, park_name):
  sub = data_frame[(data_frame.Name == name) & (data_frame.Park == park_name)]
  ranking = sub["Rank"]
  plt.plot(sub["Year of Rank"], ranking)
  plt.legend(["Ranking of " + name + " over years"])
  plt.xlabel("Year of Rank")
  plt.ylabel("Ranking")
  plt.show()
  plt.clf()

# ranking_over_time("Boulder Dash", wood, "Lake Compounce")

# write function to plot rankings over time for 2 roller coasters here:
def ranking_over_time_two(name1, name2, data_frame, park_name1, park_name2):
  sub1 = data_frame[(data_frame.Name == name1) & (data_frame.Park == park_name1)]
  sub2 = data_frame[(data_frame.Name == name2) & (data_frame.Park == park_name2)]
  ranking1 = sub1["Rank"]
  ranking2 = sub2["Rank"]
  plt.plot(sub1["Year of Rank"], ranking1)
  plt.plot(sub2["Year of Rank"], ranking2)
  plt.legend(["Ranking of " + name1, "Ranking of " + name2])
  plt.show()
  plt.clf()

#ranking_over_time_two("Boulder Dash", "El Toro", wood, "Lake Compounce", "Six Flags Great Adventure")

# write function to plot top n rankings over time here:
def top_n_over_time(n, data_frame):
  sub = data_frame[data_frame.Rank <= n]

  for coaster in set(sub['Name']):
    rankings = sub[sub["Name"] == coaster]
    ax = plt.subplot()
    ax.plot(rankings["Year of Rank"], rankings["Rank"], label=coaster)
    ax.legend(loc=4, bbox_to_anchor=(-0.5, -0., 0.5, 0.5))
  plt.show()
  plt.clf()

top_n_over_time(10, wood)


# load roller coaster data here:
coasters = pd.read_csv('roller_coasters.csv')
print(coasters.head())

# write function to plot histogram of column values here:
def histogram(data_frame, column_name):
  plt.hist(data_frame[column_name], facecolor = "green")
  plt.grid(True)
  plt.title(column_name.title() + " of Roller Coasters")
  plt.xlabel(column_name)
  plt.ylabel("Number of Roller Coasters")
  plt.show()
  plt.clf()


#histogram(coasters, "height")

# write function to plot inversions by coaster at a park here:

def bar_chart(data_frame, park_name):
  sub = data_frame[data_frame.park == park_name]
  inversions = sub.num_inversions
  ax = plt.subplot()
  ax.bar(range(len(sub.name)), inversions)
  plt.title("Number of inversions in " + park_name)
  ax.set_xticks(range(len(sub.name)))
  ax.set_xticklabels(sub.name, rotation=30)
  plt.show()
  plt.clf()

#bar_chart(coasters, "Kennywood")

# write function to plot pie chart of operating status here:
def pie_chart(data_frame):
  counts = []
  counts.append(len(data_frame[data_frame["status"] == "status.operating"]))
  counts.append(len(data_frame[data_frame["status"] == "status.closed.definitely"]))
  plt.pie(counts, labels = ["Operating", "Closed"], autopct='%0.1f%%', colors = ["green", "red"], shadow = True)
  plt.title("Operating vs. Closed")
  plt.show()
  plt.clf()

# pie_chart(coasters)


# write function to create scatter plot of any two numeric columns here:
def scatter(data_frame, column1, column2):
  plt.scatter(data_frame[column1], data_frame[column2])
  plt.legend([column1, column2])
  plt.show()
  plt.clf()

# scatter(coasters, "length", "num_inversions")

