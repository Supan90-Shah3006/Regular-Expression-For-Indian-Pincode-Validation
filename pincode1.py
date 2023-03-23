import re

pattern = '(^(?!(?:10|29|35|54|55|65|66|86|87|88|89))([1-9][0-9]{2}(|744|160|396|406|682|609|737))\s{0,1}[0-9]{3}$)'


txt = '111048'

x = re.search(pattern , txt)

if x:
  print("YES! We have a match")
else:
  print("No match")