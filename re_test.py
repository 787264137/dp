import re

pattern = r".*(no (doubt|problem|question)|not (wrong|reject|agree more|bad|impossible|incorrect|more)|not .* more).*"
string = "could not be more right"
obj = re.match(pattern,string)
print obj.group()