def Encode(string):
  # Create a dictionary of the secret language
  Algorithm = {
    'a': 'q',
    'b': 'w',
    'c': 'e',
    'd': 'r',
    'e': 't',
    'f': 'y',
    'g': 'u',
    'h': 'i',
    'i': 'o',
    'j': 'p',
    'k': 'a',
    'l': 's',
    'm': 'd',
    'n': 'f',
    'o': 'g',
    'p': 'h',
    'q': 'j',
    'r': 'k',
    's': 'l',
    't': 'z',
    'u': 'x',
    'v': 'c',
    'w': 'v',
    'x': 'b',
    'y': 'n',
    'z': 'm',
    '@': '*',
    '5': '['
  }

  # Initialize an empty string for the converted message
  converted_string = ''

  # Iterate through each character in the string and convert it to the secret language
  for char in string:
    if char in Algorithm:
      converted_string += Algorithm[char]
    else:
      # If the character is not in the secret language, just add it to the converted string as is
      converted_string += char

# Return the converted string
  return converted_string


# Secret language decoder
def Decode(string):

  # Create a dictionary of the secret language
  Algorithm = {
    'q': 'a',
    'w': 'b',
    'e': 'c',
    'r': 'd',
    't': 'e',
    'y': 'f',
    'u': 'g',
    'i': 'h',
    'o': 'i',
    'p': 'j',
    'a': 'k',
    's': 'l',
    'd': 'm',
    'f': 'n',
    'g': 'o',
    'h': 'p',
    'j': 'q',
    'k': 'r',
    'l': 's',
    'z': 't',
    'x': 'u',
    'c': 'v',
    'v': 'w',
    'b': 'x',
    'n': 'y',
    'm': 'z',
    '*': '@',
    '[': '5'
  }

  # Initialize an empty string for the decoded message
  decoded_string = ''

  # Iterate through each character in the string and decode it to the original language
  for char in string:
    if char in Algorithm:
      decoded_string += Algorithm[char]
    else:
      # If the character is not in the secret language, just add it to the decoded string as is
      decoded_string += char

  # Return the decoded string
  return decoded_string
