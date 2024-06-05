def length_of_longest_substring(s):
  character_count = {}
  maxim = 0
  cur = -1
  for i in range(0,len(s)):
      if s[i] in character_count and character_count[s[i]] >= cur:
          cur = character_count[s[i]]
      maxim = max(maxim, i - cur)
      character_count[s[i]] = i
      
  return maxim


print(length_of_longest_substring("abcabcsab"))