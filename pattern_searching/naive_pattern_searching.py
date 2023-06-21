def pattern_search(text, pattern):
  print("Input Text:", text, "Input Pattern:", pattern)
  for index in range(len(text)):
    print("Text Index:", index)
    match_count = 0

    for char in range(len(pattern)):
      print("Pattern Index:", char)
      if text[index+char] == pattern[char]:
        print("Matching index found")
        print("Match count: {}".format(match_count))
        match_count += 1
      else:
        break
    
    if match_count == len(pattern):
      print("{} found at index {}".format(pattern, index))

text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
pattern_search(text, pattern)