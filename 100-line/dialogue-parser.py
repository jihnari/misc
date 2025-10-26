import csv 
# import flag commandline stuff?


# open csv file 
filename = "file.csv"
rows = []
rows = ["charcter-state","takumi-state","here's some dialogue"]
# not positive this is how it'll be read (the "")
rows.append("charcter-state2,,here's some more dialogue")

# output = []

# theoretically, a line will be as follows: 
# character-state, takumi-state, dialogue

# the intended output is: 
#     <details class="charcter-state takumi-state">
#     <summary>dialogue</summary>
#     </details>


with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  
  # i dont think i need this ?
  for row in csvreader:
    rows.append(row)
  
for row in rows:
  # make output transient     
  output = ""

  # if takumi state is not null (fix this? 0 isnt gonna work)
  # do i even bother with this or do i just do better (format the spreadsheet really specifically)
  # if very specific: do we want to have an if branch for scene changes...? 
  if row[1] != "":
    output+=("<details class=\"" + row[0] + row[1] + " pov-open>\n")
  else:
    output+=("<details class=\"" + row[0] + ">\n")
  
  # append the dialogue
  output+=("<summary>" + row[2] +"</summary> \n</details>")

  # i think i can just output at the same time...? 
  # print(output)
  print(row)
