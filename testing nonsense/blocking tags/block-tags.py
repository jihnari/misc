'''
notes about tags: 
  capitalization MATTERS
  / becomes *s* 
  spaces MUST be %20
  must have NO leading or trailing spaces
  must be the OFFICIAL SORTABLE tag, not an off-shoot tag that links to the same place
  (may have to add multiple versions of the same tag)
  
hint: grab tags from the URL (still gotta add the %20 tho)

example tags: 
  Bakugou%20Katsuki*s*Midoriya%20Izuku
  Fluff
  Angst
  Implied*s*Referenced%20Child%20Abuse
  Other%20Additional%20Tags%20to%20Be%20Added
    
todo: 
  parse a file and not a hardcoded value
  parse the input, replace / with *s* and url encode the whole thing 
  output results to file instead of stdout 
  consider: tier 1 tags blocked and tier 2 tags warned. tier 1 would colapse the whole work, leaving only the title. tier 2 would only highlight the given tag.
''' 


# get list from file (no file currently, too lazy)
# file = ["Fluff", "Angst"]
file = ["Trans%20Character", "Trans%20Male%20Character", "Trans", "Trans%20Female%20Character", "Daddy%20Kink", "Alpha*s*Beta*s*Omega%20Dynamics", "Fluff", "Omega%20Verse", "Piss%20Kink", "Scat", "Mpreg", "Mpreg%20|%20Male%20Pregnancy","Major%20Character%20Death"]


warning = ["Fluff", "Major%20Character%20Death"]

hide = ["Trans%20Character", "Trans%20Male%20Character", "Trans", "Trans%20Female%20Character", "Daddy%20Kink", "Alpha*s*Beta*s*Omega%20Dynamics", "Omega%20Verse", "Piss%20Kink", "Scat", "Mpreg", "Mpreg%20|%20Male%20Pregnancy"]


# cycle through array contents
for tag in warning:
  # highlight the tag
  line = "li:has(a[href=\"/tags/%s/works\"]) a[href=\"/tags/%s/works\"]{background:pink;} " % (tag, tag)

  #print css to screen
  print(line)

# cycle through array contents
for tag in hide: 
  # sanity checking
  # print(tag)
  
  # highlight the tag
  line = "li:has(a[href=\"/tags/%s/works\"]) a[href=\"/tags/%s/works\"]{background:pink;} " % (tag, tag)

  # display:none of everything except the fic title
  line += "\nli:has(a[href=\"/tags/%s/works\"]) > div:first-child > *:first-child ~ *, li:has(a[href=\"/tags/%s/works\"]) > div:first-of-type ~ * { display:none; } " % (tag, tag)
  line += "\nli:has(a[href=\"/tags/%s/works\"]).blurb .header{ min-height:0px !important; }" % tag
 
  # on hover, display:block (for the things you hid earlier)
  line += "\nli:has(a[href=\"/tags/%s/works\"]):hover > div:first-child > *:first-child ~ * { display:block; }" % tag
  line += "\nli:has(a[href=\"/tags/%s/works\"]):hover > div:first-of-type ~ * { display:block; } \n" % tag

  # might need another \n, only tested this on the online python interpreter 

  # print css to screen
  print(line)
