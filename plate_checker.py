''' Plate Checker rules:

  - Plates must have at least 2 letters minimum. Max of 6 characters (letters or numbers)
  
  - Numbers can't be in middle of combination, must be at end. First number can't be 0.
      EX: AB, ABC, AB1, AB12, ABC12, ABC123 = ✅
      EX: A1, A1B, AB12CD, ABC12D = ❌
      EX: ABC102 = ✅
      EX: ABC012 = ❌
      
  - No special characters( . , ! @ # $ % ^ & *  etc.)
      EX: ABC!@1 = ❌
  
'''


# Main function that determines print statement of valid or invalid 
def main():
    combo = input("Plate combinations please: ")

    if is_valid(combo):
        print("Valid")
    else:
        print("Invalid")


''' Function to check if input is formatted correctly. Returns True of False Boolean.'''

     
def is_valid(c):
    combination = c
    combo_total = len(combinition)
    combo_mid = combo_total // 2
    # print(combo_mid)
    
    # First uses string length if fits required amount, then checks what type of strings are formatted.
    if combo_total >= 2 and combo_total <= 6:
        
        if combination.isalpha():
            return True
        
    # Checks if strings in total are a mix of numbers. First 2 strings and last string if valid letters through slicing
        elif combination.isalnum():
            first_two = combination[:2]
            last_item = combination[-1]
            # print(f"last item: {last_item}")
            
            # Checks last string is just a letter
            if last_item.isalpha():
                return False
            
    # Checking first 2, then using mid point of string to determine second half of strings as mix or straight letters an numbers.
            elif first_two.isalpha():
                second_half = combination[combo_mid:]
                # print(f'the second half is: {second_half}')
                
                if second_half.isdecimal():
                    # print(f'mid point item: {combination[combo_mid]}')
                    if '0' == combination[combo_mid]:
                        return False
                    return True

                # Using mid point to check middle strings positioning if mix or straight numbers/ letters 
                elif second_half.isalnum:
                    x = combination[(combo_mid - 1)]
                    y = combination[(combo_mid)]
                    # print('reach this far')
                    # print(x)
                    # print(y)
                    if x.isalpha() and y.isalpha() or x.isdecimal() and y.isdecimal():
                        return True
                    else:
                        return False

                return True

            return False

        return False

    else:
        return False


main()
