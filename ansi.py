
# You can get more information about ansi codes at 
# https://www.folkstalk.com/tech/python-ansi-colors-with-code-examples/
# https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
# https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#:~:text=Bright%20Green%3A%20%5Cu001b%5B32,%3A%20%5Cu001b%5B33%3B1m

for i in range(30,37):
    print(f"{i} We begin ANSI code with an \u001b[{i}mescape code\u001b[0m")


for i in range(30,37):
    print(f"{i} Bold: \u001b[{i};1mescape code\u001b[0m")
