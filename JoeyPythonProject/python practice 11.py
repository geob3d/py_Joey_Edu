formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "own text here",
    "Maybe a poem",
    "Or a song about fear"
))
print(formatter.format("Bruce Lee", "Muhammed Ali", "Sonny Chiba", "Jean Claude Van Damme"))
print(formatter.format("Christina Hendricks", "Alexandra Daddario", "Eva Green", "Beyonce Knowles"))
