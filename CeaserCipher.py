import Art
Alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def Caeser_Cipher(text, shift, direction):
      if direction == 'decode':
            shift *= (-1)
      new_text = ''
      for char in text:
            if char in Alphabets:
                  Position = Alphabets.index(char)
                  Position += shift
                  new_char = Alphabets[Position]
                  new_text += new_char
            else:
                  char += new_text
      return new_text

print(f'WELCOME!\nYou are playing :\n{Art.Ceasar_Cipher}')
Text = str(input('Enter the text to check:').lower())
Shift_amount = int(input('Enter the shift Amount:'))
Direction = str(input('Enter "encode" or "decode"(if something other than these are entered '
                      '"encode will be considered:")').lower())
New_Text = Caeser_Cipher(Text, Shift_amount, Direction)
if Direction == 'decode':
      print(f'The {Direction}ed text of {Text} is :{New_Text}')
else:
      print(f'The encodeded text of {Text} is :{New_Text}')