# todo: 
# - could try to remove extra spaces from pre-dialogue code 
# - added in some qol updates and didnt test them <3 gl future me 
# - clean up code / remove commented out lines 
# - make code more readable? 

import csv 
import sys
import argparse 


def main():
  # open csv file 
  # we're on windows so you have to escape the \
  # filename = ".\\100-line\\file.csv"
  csvfile = ".\\100-line\\input.csv"
  txtfile =".\\100-line\\text.txt"

  parser = argparse.ArgumentParser()
  parser.add_argument("-c", "--CSV", help="Provide a CSV file to parse")
  parser.add_argument("-t", "--TXT", help="Provide a TXT file to parse")
  args = parser.parse_args()

  # print("entering loop")

  if args.CSV:
    # print("CSV:", args.CSV)
    # filename = args.CSV
    csv_to_html(csvfile)

  elif args.TXT:
    # txtfile = args.TXT
    txt_to_csv(txtfile)

  else:
    print("done!")


# pot.: 
# write a txt to csv parser.
# take: 
# <takumi>/n line1 /n line2 /n <eito>/n line3
# and turn it into 
# ,takumi,pov-open, line1
# ,,pov-open, line2
# eito,,, line3 

# checking for "if takumi: put in row0. else put in row1." for all strings encased in <>. and dialogue goes in row3. 
# 
# yeah???
# 
def txt_to_csv(txtfile): 
  with open(txtfile, 'r') as file:
    buffer = ""
    charname=""

    # is the delimeter automatically /n? double check
    for row in file: 

      # if newline
      if row == "\n":
        pass

      # if character name
      elif "<" in row:
        # strip out <>
        # print(row)
        charname = row.replace('<', '')
        charname = charname.replace('>', '')
        charname = charname.replace(' ', '')
        charname = charname.replace('\n', '')
        # print(charname)

      # room changes, > 
      elif ">" in row:
        print("ROOM")
        # room = row[0].replace('>', '')
        # room = room.replace(' ', '')
        # buffer.append(row + "\n")
        buffer += row
      

      # else if dialogue 
      else: 
        # print(charname)
        # row = row.replace(',', '\\,')
        row = row.replace('\n', '')
        row = "\"" + row + "\"\n"
        # if takumi
        if "takumi" in charname:
          # print("TAKUMI")
          # buffer.append("\n,takumi,pov-open," + row + "\n")
          buffer += ",takumi-talk,pov-open," + row 

        elif "thought" in charname:
          # print("THOUGHT")
          # buffer.append("\n,takumi,thought," + row + "\n")
          buffer += ",takumi-base,thought," + row

        # if not takumi
        else: 
          # print(charname)
          # buffer.append(charname + ",,," + row + "\n")
          buffer += charname + "-talk,,," + row
          
    # exit forever loop, print to file 
    # print(buffer)
    with open("output.csv", 'w') as f:
      # print(buffer, file=f)
      f.write(buffer)
      
    # this was a fun thought but actually we need to do a lot of editing to the csv file first. like, so much. every emotion change. 
    # csv_to_html("output.csv")
          


# a line needs: 
# - is takumi talking? (pov-open)
# - is takumi thinking? (thoughts)
# - is takumi having an emotion different from the default (takumi-emotion)
# - is the other character talking? (pov-open is absent)

# (theoretically) a line will be as follows: 
# character-state, takumi-state, name-box-state, dialogue

# if name-box-state is empty, target-character is talking
# (exception: choice time)

# the intended output is: 
#     <details class="character-state takumi-state name-box-state">
#     <summary>dialogue</summary>
#     </details>

def csv_to_html(filename):
  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
      # output is transient     
      output = ""
      first=0

      # if takumi state is not null 
      # if row[2] != "":
      #   output+=("<details class=\"" + row[0] + " " + row[1] + " " + row[2] + " pov-open\">\n")
      # else:
      #   output+=("<details class=\"" + row[0] + " " + row[1] + "\">\n")

      # if the row isn't empty
      # if row[0] != "":
      try:

        # if very specific: do we want to have an if branch for scene changes...? 
        # need: room, seed character? 
        # see: new 135
        if ">" in row[0]:
          # close out current room
          output +=("\n<\\div><\\div><\\div>\n<!-- end of current room-->\n\n\n")

          room = row[0].replace('>', '')
          room = room.replace(' ', '')
          # could have a switch statement for the room name. maybe should. would it save you time? probably not. 
          roomname=row[0]
          if room == "biolab":
            roomname="Bio Lab"
          if room == "library":
            roomname="Library"

          # whoops. if room == black, do a whole different thing, huh. 
          # or do you...? cant remember how its set up, black might supress the room title/clock/etc. ...no it might not supress the clock. 
          if room == "black":
            # room
            pass


          # could have another switch statement lol
          character = row[1].replace(' ', '')
          charactername=character
          if character == "yugamu":
            charactername="Yugamu Omokage"
          if character == "eito":
            charactername="Eito Aotsuki"
          if character == "shion":
            charactername="???"
          if character == "kako":
            charactername="Kako Tsukumo"

          # test output
          # output+=(room + roomname + character + charactername + "/n")
            

          output+=("<!-- move to " + room + "-->\n<div class=\"main-box hidden\">\n  <div class=\"room " + room + " blur\">\n  </div>\n<p class=\"location\">" + roomname + "\n</p>\n<!-- update date -->\n<div class=\"clock afternoon\"><p class=\"date\"><span class=\"zero\"></span><span class=\"two\"></span><span class=\"six\"></span></p></div>\n\n  <!-- seed scene characters -->\n  <div class=\"character " + character + "\"></div>\n  <div class=\"takumi-box pov-element\">\n    <div class=\"takumi-bg " + room + "\">\n    <div class=\"takumi-insert\"></div>\n    </div>\n  </div>\n\n  <!-- choice code goes here (if applicable)  -->\n\n\n<div class=\"anchor\">\n<div class=\"name-box right pov-element\">Takumi Sumino</div>\n<div class=\"name-box target-element\">" + charactername + "</div>\n\n<div class=\"text-box\">\n ")


        # line of dialogue, normal text
        else:
          # print dialogue code
          # start clock if first time here
          # first = first + 1
          # if first == 1:
          #   output+=("<details class=\"rotate " + row[0] + " " + row[1]+ " " + row[2] + "\">\n")
          # else:
            
            
          # where row[2] is pov-open/thoughts/null
          output+=("<details class=\"" + row[0] + " " + row[1]+ " " + row[2] + "\">\n")
          
          # append the dialogue
          # the "s added in by the csv file (in the case of " or , in the line) are filtered out by the csv parser naturally, dont worry about them. 
          output+=("<summary>" + row[3] +"</summary> \n</details> \n")


        # print whatever's in output before looping 
        print(output)

      except:
        pass

      # close out the room 
      # this is no longer working for some reason so i killed it
      # print("\n<\\div><\\div><\\div>\n\n")


if __name__ == "__main__":
  main()