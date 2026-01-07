print("<<< Welcome to number system conversion >>>")
#
while True:
    user_input_data=input("Enter your number for conversion: ")
    try:
        if all(c in "-.0123456789abcdefABCDEF" for c in user_input_data) and any(c in "-123456789abcdefABCDEF" for c in user_input_data) and user_input_data.count('.') <= 1 and user_input_data.count('-') <= 1 and '-' not in user_input_data[1:len(user_input_data)]:
            user_input_data=user_input_data
            break
        else:
            print("Please enter valid data!")
    except:
        print("Please enter only numbers!")
#
print(f"Number type-\n1. Binary\n2. Octal\n3. Decimal\n4. Hexadecimal")

# here s = user_input_data 
def is_valid_binary(s):
    if not all(c in "-.01" for c in s): return False
    if not any(c in "01" for c in s): return False
    if s.count('.') > 1: return False
    if s.count('-') > 1: return False
    if '-' in s[1:]: return False
    return True

def is_valid_octal(s):
    if not all(c in "-.01234567" for c in s): return False
    if not any(c in "01234567" for c in s): return False
    if s.count('.') > 1: return False
    if s.count('-') > 1: return False
    if '-' in s[1:]: return False
    return True

def is_valid_decimal(s):
    if not all(c in "-.0123456789" for c in s): return False
    if not any(c in "0123456789" for c in s): return False
    if s.count('.') > 1: return False
    if s.count('-') > 1: return False
    if '-' in s[1:]: return False
    return True

def is_valid_hex(s):
    s = s.lower()
    if not all(c in "-.0123456789abcdef" for c in s): return False
    if not any(c in "0123456789abcdef" for c in s): return False
    if s.count('.') > 1: return False
    if s.count('-') > 1: return False
    if '-' in s[1:]: return False
    return True


#
while True:
    users_1st_option=input(f"Select the type you want to convert from: ")
    try:
        users_1st_option = int(users_1st_option) 
        if users_1st_option < 6 and users_1st_option > 0:
            users_1st_option = users_1st_option
            break
        else:
            print("Wrong input!")
    except:
        print("Please only type the relative number of the option!")
#
while True:
    users_2nd_option=input(f"Select the type you want to convert to: ")
    try:
        users_2nd_option = int(users_2nd_option)
        if users_2nd_option == 1 or users_2nd_option == 2 or users_2nd_option == 3 or users_2nd_option == 4:
            users_2nd_option = users_2nd_option
            break
        else:
            print("Wrong input!")
    except:
        print("Please only type the number corresponding to the option!")
#
user_input_data =user_input_data.lower()  #str_user_data
splited_int_and_float_listdata = user_input_data.split('.')
user_data_int_part = splited_int_and_float_listdata[0] or '0'

if len(splited_int_and_float_listdata) > 1:
    user_data_float_part = splited_int_and_float_listdata[1] or '0'
    len_float_part=len(user_data_float_part)
    float_flag = 1
else:
    user_data_float_part = ''
    float_flag = 0
    # if not, means “no fractional part”

len_int_part=len(user_data_int_part)
int_index_number = 0
padded_int_start_index = 0
padded_int_end_index=0
int_result = ''
conversion_status = 0

float_index_number = 0
padded_float_start_index = 0
padded_float_end_index=0
float_result = ''


# Example usage:
# user_data_float_part = '101010111101110000'
# print('float ', user_data_float_part)
# float_result = ''         
# print(user_data_float_part)


#1 DEF Bin to Octal int  #works

def bin_to_oct_int(user_data_int_part):
    len_int_part = len(user_data_int_part)

    #global int_result
    int_index_number = 0
    padded_int_start_index = 0
    padded_int_end_index = 0
    groups_3_bin_ints = []
            
    padded0_int_part = user_data_int_part.zfill(len_int_part+(3-(len_int_part%3)))
    
    for i in padded0_int_part:
        padded_int_end_index += 1
        if padded_int_end_index%3 == 0:
            groups_3_bin_ints = groups_3_bin_ints + [padded0_int_part[padded_int_start_index:padded_int_end_index]]
            padded_int_start_index+=3

    list_intbin_converted_t_oct = []
    bin_to_oct_map = {
        '000': 0,
        '001': 1,
        '010': 2,
        '011': 3,
        '100': 4,
        '101': 5,
        '110': 6,
        '111': 7
    }

    for j in groups_3_bin_ints:
        group = groups_3_bin_ints[int_index_number]
        if group in bin_to_oct_map:
            list_intbin_converted_t_oct = list_intbin_converted_t_oct + [bin_to_oct_map[group]]
            int_index_number += 1
        else:
            break
    int_result = ''.join(map(str, list_intbin_converted_t_oct)).lstrip('0')
    return int_result
        #return int_result    

#2 DEF Bin to Octal float  #works

def bin_to_oct_float(user_data_float_part):
    len_float_part=len(user_data_float_part)
    
    #global float_result
    float_index_number = 0
    padded_float_start_index = 0
    padded_float_end_index=0
    
    zneed = 3-(len_float_part%3)+len_float_part
    padded0_fractional_part = user_data_float_part.ljust(zneed, '0')
    groups_3_bin_floats=[]
    
    for io in padded0_fractional_part:
        padded_float_end_index += 1
        if padded_float_end_index%3 == 0:
            groups_3_bin_floats = groups_3_bin_floats + [padded0_fractional_part[padded_float_start_index:padded_float_end_index]]
            padded_float_start_index+=3
    
    list_floatbin_converted_t_oct = []
    bin_to_oct_map = {
        '000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7
    }
    
    for ji in groups_3_bin_floats:
        group = groups_3_bin_floats[float_index_number]
        if group in bin_to_oct_map:
            list_floatbin_converted_t_oct = list_floatbin_converted_t_oct + [bin_to_oct_map[group]]
            float_index_number += 1
        else:
            break
    float_result = ''.join(map(str, list_floatbin_converted_t_oct)).rstrip('0')
    return float_result

#3 DEF Bin to Hexadecimal int   #works

def bin_to_hex_int(user_data_int_part):
    len_int_part = len(user_data_int_part)

    #global int_result
    int_index_number = 0
    padded_int_start_index = 0
    padded_int_end_index = 0
    groups_4_bin_ints = []
            
    padded0_int_part = user_data_int_part.zfill(len_int_part+(4-(len_int_part%4)))

    for i in padded0_int_part:
        padded_int_end_index += 1
        if padded_int_end_index%4 == 0:
            groups_4_bin_ints = groups_4_bin_ints + [padded0_int_part[padded_int_start_index:padded_int_end_index]]
            padded_int_start_index+=4

    list_intbin_converted_t_hex = []
    bin_to_hex_map = {
        '0000': '0','0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }

    for j in groups_4_bin_ints:
        group = groups_4_bin_ints[int_index_number]
        if group in bin_to_hex_map:
            list_intbin_converted_t_hex = list_intbin_converted_t_hex + [bin_to_hex_map[group]]
            int_index_number += 1
        else:
            break
    int_result = ''.join(list_intbin_converted_t_hex)  #''.join(map(str, list_intbin_converted_t_hex))
    return int_result


#4 DEF Bin to Hexadecimal float   #works

def bin_to_hex_float(user_data_float_part):
    len_float_part=len(user_data_float_part)
    
    #global float_result
    float_index_number = 0
    padded_float_start_index = 0
    padded_float_end_index=0
    
    zneed = 4-(len_float_part%4)+len_float_part
    padded0_fractional_part = user_data_float_part.ljust(zneed, '0')
    groups_4_bin_floats=[]

    for io in padded0_fractional_part:
        padded_float_end_index += 1
        if padded_float_end_index%4 == 0:
            groups_4_bin_floats = groups_4_bin_floats + [padded0_fractional_part[padded_float_start_index:padded_float_end_index]]
            padded_float_start_index+=4
    
    list_floatbin_converted_t_hex = []
    bin_to_hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }

    for ji in groups_4_bin_floats:
        group = groups_4_bin_floats[float_index_number]
        if group in bin_to_hex_map:
            list_floatbin_converted_t_hex = list_floatbin_converted_t_hex + [bin_to_hex_map[group]]
            float_index_number += 1
        else:
            break
    float_result = ''.join(list_floatbin_converted_t_hex).rstrip('0') #''.join(map(str, list_floatbin_converted_t_hex))
    return float_result



#5 DEF Octal to Binary int   #works

def oct_to_bin_int(user_data_int_part):
    
    #global int_result
    int_index_number = 0
    list_intoct_converted_t_bin = []
    
    oct_to_bin_map = {
        '0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'
    }

    for j in user_data_int_part:
        group = user_data_int_part[int_index_number]
        if group in oct_to_bin_map:
            list_intoct_converted_t_bin = list_intoct_converted_t_bin + [oct_to_bin_map[group]]
            int_index_number += 1
        else:
            break
    int_result = ''.join(list_intoct_converted_t_bin)  #''.join(map(str, list_intoct_converted_t_bin))
    int_result = int_result.lstrip('0')
    return int_result
        


#6 DEF Octal to Binary float    #works

def oct_to_bin_float(user_data_float_part):
    
    #global float_result
    float_index_number = 0
    list_floatoct_converted_t_bin = []
    
    oct_to_bin_map = {
        '0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'
    }
    for j in user_data_float_part:
        group = user_data_float_part[float_index_number]
        if group in oct_to_bin_map:
            list_floatoct_converted_t_bin = list_floatoct_converted_t_bin + [oct_to_bin_map[group]]
            float_index_number += 1
        else:
            break
    float_result = ''.join(list_floatoct_converted_t_bin)  #''.join(map(str, list_intoct_converted_t_bin))
    float_result = float_result.rstrip('0')
    return float_result


#7 DEF Hexadecimal to Binary int #works

def hex_to_bin_int(user_data_int_part):
    
    #global int_result
    int_index_number = 0
    list_inthex_converted_t_bin = []
    
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
    }
    #key_to_search = user_input_data.casefold().strip
    #print(hex_to_bin_map.get(key_to_search, "not found!"))

    for j in user_data_int_part:
        group = user_data_int_part[int_index_number]
        if group in hex_to_bin_map:
            list_inthex_converted_t_bin = list_inthex_converted_t_bin + [hex_to_bin_map[group]]
            int_index_number += 1
        else:
            break
    int_result = ''.join(list_inthex_converted_t_bin)  #''.join(map(str, list_floathex_converted_t_bin))
    int_result = int_result.lstrip('0')
    return int_result
        


#8 DEF Hexadecimal to Binary float #works

def hex_to_bin_float(user_data_float_part):
    
    #global float_result
    float_index_number = 0
    list_floathex_converted_t_bin = []

    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
    }
    for j in user_data_float_part:
        group = user_data_float_part[float_index_number]
        if group in hex_to_bin_map:
            list_floathex_converted_t_bin = list_floathex_converted_t_bin + [hex_to_bin_map[group]]
            float_index_number += 1
        else:
            break
    float_result = ''.join(list_floathex_converted_t_bin)  #''.join(map(str, list_intoct_converted_t_bin))
    float_result = float_result.rstrip('0')
    return float_result


#9 DEF Binary to Decimal integetr #works

def bin_to_decimal_int(user_data_int_part):  #, int_result

    intbin_converted_t_deci = 0 #type int
    int_user_data_int_part = int(user_data_int_part) #str to int
    num_possition_fm_right = len(user_data_int_part)
    num_possition_fm_left = 0
    for i in str(int_user_data_int_part):
        intbin_converted_t_deci += int(user_data_int_part[num_possition_fm_right-1])*(2**num_possition_fm_left)
        num_possition_fm_right -= 1
        num_possition_fm_left += 1
    int_result = str(intbin_converted_t_deci)
    return int_result
    

#10 DEF Binary to Decimal float #works

def bin_to_decimal_float(user_data_float_part):
    
    user_data_float_part = user_data_float_part #str to int though other functions are using list/string
    floatbin_converted_t_deci = 0 #type float
    num_possition_fm_left0 = 0
    num_possition_fm_leftn = -1
    for i in str(user_data_float_part):
        floatbin_converted_t_deci += int(user_data_float_part[num_possition_fm_left0])*(2**num_possition_fm_leftn)
        num_possition_fm_left0 += 1
        num_possition_fm_leftn -= 1
    float_result = str(floatbin_converted_t_deci)
    return float_result





#11 DEF Decimal to Binary integetr #works

def decimal_to_bin_int(user_data_int_part):
    intdeci_converted_t_bin = []
    quotient = int(user_data_int_part)
    while quotient > 1:
        intdeci_converted_t_bin.append(str(quotient % 2))  # append()  cleaner than += str()
        quotient = quotient // 2
    intdeci_converted_t_bin.append(str(quotient))
    int_result = ''.join(intdeci_converted_t_bin[::-1])  # Reverse for MSB-first
    return int_result
    
    
#12 DEF Decimal to Binary float #works

def decimal_to_bin_float(user_data_float_part):
    #global float_result
    # Convert '2343' to 0.2343
    float_user_data = float('0.' + user_data_float_part)
    max_digit_bin_float = 0
    floatdeci_converted_t_bin = []

    # Changed to < 20 to get exactly 20 digits
    while float_user_data != 0.0 and max_digit_bin_float < 20:
        float_user_data = float_user_data * 2
        
        # Instead of splitting strings, we use int() to get the 1 or 0
        updated_result = int(float_user_data) 
        floatdeci_converted_t_bin.append(str(updated_result))
        
        # Remove the integer part to keep the decimal for the next loop
        float_user_data = float_user_data - updated_result
        
        max_digit_bin_float += 1

    float_result = "".join(floatdeci_converted_t_bin)
    return float_result

#13 DEF Hexadecimal to Decimal int #works

def hex_to_decimal_int(user_data_int_part):  #, int_result
    hex_to_deci_map = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    hex_digit_in_deci = []
    #for i in user_data_int_part:
     #   if 
    int_index_number = 0
    for j in user_data_int_part:
        group = user_data_int_part[int_index_number]
        if group in hex_to_deci_map:
            hex_digit_in_deci.append(hex_to_deci_map[group])
            int_index_number += 1
        else:
            hex_digit_in_deci.append(int(group))
            int_index_number += 1

    intbin_converted_t_hex = 0 #type int
    #int_user_data_int_part = hex_digit_in_deci   # #str to int
    num_possition_fm_right = len(hex_digit_in_deci)
    num_possition_fm_left = 0
    for i in hex_digit_in_deci:
        intbin_converted_t_hex += int(hex_digit_in_deci[num_possition_fm_right-1])*(16**num_possition_fm_left)
        num_possition_fm_right -= 1
        num_possition_fm_left += 1
    int_result = str(intbin_converted_t_hex)
    return int_result

#14 DEF Hexadecimal to Decimal float
  
def hex_to_decimal_float(user_data_float_part):  #, int_result
    hex_to_deci_map = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    hex_digit_in_deci = []
    #for i in user_data_int_part:
     #   if 
    float_index_number = 0
    for j in user_data_float_part:
        group = user_data_float_part[float_index_number]
        if group in hex_to_deci_map:
            hex_digit_in_deci.append(hex_to_deci_map[group])
            float_index_number += 1
        else:
            hex_digit_in_deci.append(int(group))
            float_index_number += 1

    #user_data_float_part = user_data_float_part #str to int though other functions are using list/string
    floathex_converted_t_deci = 0 #type float
    num_possition_fm_left0 = 0
    num_possition_fm_leftn = -1
    for i in str(user_data_float_part):
        floathex_converted_t_deci += int(hex_digit_in_deci[num_possition_fm_left0])*(16**num_possition_fm_leftn)
        num_possition_fm_left0 += 1
        num_possition_fm_leftn -= 1
    float_result = str(floathex_converted_t_deci)
    return float_result

#15 DEF Decimal to Hexadecimal int

def deci_to_hex_int(user_data_int_part):
#def decimal_to_bin_int(user_data_int_part):
    intdeci_converted_t_hex = []
    quotient = int(user_data_int_part)
    while quotient > 1:
        intdeci_converted_t_hex.append(str(quotient % 16))  # append()  cleaner than += str()
        quotient = quotient // 16
    intdeci_converted_t_hex.append(str(quotient))
    deci_to_hex_map = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    deci_digit_in_hex = []
    #for i in user_data_int_part:
     #   if 
    #int_index_number = 0
    for j in intdeci_converted_t_hex:
        #group = intdeci_converted_t_hex[j]
        if j in deci_to_hex_map:
            deci_digit_in_hex.append(deci_to_hex_map[j])  #[group]
            #int_index_number += 1
        else:
            deci_digit_in_hex.append(j)
            #int_index_number += 1
    int_result = ''.join(deci_digit_in_hex[::-1]).lstrip()  # Reverse for MSB-first
    return int_result

#16 DEF Decimal to Hexadecimal float

def deci_to_hex_float(user_data_float_part):
    float_user_data = float('0.' + user_data_float_part)
    max_digit_bin_float = 0
    floatdeci_converted_t_hex = []

    # Changed to < 20 to get exactly 20 digits
    while float_user_data != 0.0 and max_digit_bin_float < 20:
        float_user_data = float_user_data * 16
        # Instead of splitting strings, we use int() to get the 1 or 0
        updated_result = int(float_user_data) 
        floatdeci_converted_t_hex.append(str(updated_result))
        # Remove the integer part to keep the decimal for the next loop
        float_user_data = float_user_data - updated_result
        max_digit_bin_float += 1

    deci_to_hex_map = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    deci_digit_in_hex = []
    for j in floatdeci_converted_t_hex:
        #group = intdeci_converted_t_hex[j]
        if j in deci_to_hex_map:
            deci_digit_in_hex.append(deci_to_hex_map[j])  #[group]
            #int_index_number += 1
        else:
            deci_digit_in_hex.append(j)
            #int_index_number += 1
    int_result = ''.join(deci_digit_in_hex).lstrip()  # Reverse for MSB-first
    return int_result

#    <<<<< execution code >>>>>    #

#01 DEF Binary to Octal exe
if users_1st_option == 1 and users_2nd_option == 2 and is_valid_binary(user_input_data) == True:
    int_result = bin_to_oct_int(user_data_int_part)
    if float_flag == 1:
        float_result = bin_to_oct_float(user_data_float_part)
    if float_flag == 1:
        print(f"Binary: {user_data_int_part}.{user_data_float_part}")
        print(f"Octal: {int_result}.{float_result}")
    elif float_flag == 0:
        print(f"Binary: {user_data_int_part}")
        print(f"Octal: {int_result}")
elif users_1st_option == 1 and users_2nd_option == 2 and is_valid_binary(user_input_data) == False:
    print('Invalid number instead of binary!')

#02  DEF Binary to Hexadecimal exe
if users_1st_option == 1 and users_2nd_option == 4 and is_valid_binary(user_input_data) == True:
    int_result = bin_to_hex_int(user_data_int_part)
    if float_flag == 1:
        float_result = bin_to_hex_float(user_data_float_part)
    if float_flag == 1:
        print(f"Binary: {user_data_int_part}.{user_data_float_part}")
        print(f"Hexadecimal: {int_result}.{float_result}")
    elif float_flag == 0:
        print(f"Binary: {user_data_int_part}")
        print(f"Hexadecimal: {int_result}")
elif users_1st_option == 1 and users_2nd_option == 4 and is_valid_binary(user_input_data) == False:
    print('Invalid number instead of binary!')

#03  DEF Octal to Bin exe
if users_1st_option == 2 and users_2nd_option == 1 and is_valid_octal(user_input_data) == True:
    int_result = oct_to_bin_int(user_data_int_part)
    if float_flag == 1:
        float_result = oct_to_bin_float(user_data_float_part)
    if float_flag == 1:
        print(f"Octal: {user_data_int_part}.{user_data_float_part}")
        print(f"Binary: {int_result}.{float_result}")
    elif float_flag == 0:
        print(f"Octal: {user_data_int_part}")
        print(f"Binary: {int_result}")
elif users_1st_option == 2 and users_2nd_option == 1 and is_valid_octal(user_input_data) == False:
    print('Invalid number instead of octal!')

#04  DEF Hexadecimal to Binary exe
if users_1st_option == 4 and users_2nd_option == 1 and is_valid_hex(user_input_data) == True:
    int_result = hex_to_bin_int(user_data_int_part)
    if float_flag == 1:
        float_result = hex_to_bin_float(user_data_float_part)
    if float_flag == 1:
        print(f'Hexadecimal: {user_data_int_part}.{user_data_float_part}')
        print(f"Binary: {int_result}.{float_result}")
    else:
        print(f"Hexadecimal: {user_data_int_part}")
        print(f"Binary: {int_result}")
elif users_1st_option == 4 and users_2nd_option == 1 and is_valid_hex(user_input_data) == False:
    print('Invalid number instead of hexadecimal!')

#05 DEF Binary to decimal exe
if users_1st_option == 1 and users_2nd_option == 3 and is_valid_binary(user_input_data) == True:
    int_result = bin_to_decimal_int(user_data_int_part)
    if float_flag == 1:
        float_result = bin_to_decimal_float(user_data_float_part)
    if float_flag == 1:
        print(f"Binary: {user_data_int_part}.{user_data_float_part}")
        print(f"Decimal: {int(int_result)+float(float_result)}")
    else:
        print(f"Binary: {user_data_int_part}")
        print(f"Decimal: {int_result}")
elif users_1st_option == 1 and users_2nd_option == 3 and is_valid_binary(user_input_data) == False:
    print('Invalid number instead of binary!')

#06 DEF Decimal to Binary exe
if users_1st_option == 3 and users_2nd_option == 1 and is_valid_decimal(user_input_data) == True:
    int_result = decimal_to_bin_int(user_data_int_part)
    if float_flag == 1:
        float_result = decimal_to_bin_float(user_data_float_part)
    if float_flag == 1:
        print(f"Decimal: {user_data_int_part}.{user_data_float_part}")
        print(f"Binary: {int_result}.{float_result}")
    else:
        print(f"Decimal: {user_data_int_part}")
        print(f"Binary: {int_result}")
elif users_1st_option == 3 and users_2nd_option == 1 and is_valid_decimal(user_input_data) == False:
    print('Invalid number instead of decimal!')

#07 DEF Octal to Decimal exe
if users_1st_option == 2 and users_2nd_option == 3 and is_valid_octal(user_input_data) == True:
    int_result1 = oct_to_bin_int(user_data_int_part)
    int_result = int(bin_to_decimal_int(int_result1))
    if float_flag == 1:
        float_result1 = oct_to_bin_float(user_data_float_part)
        float_result = float(bin_to_decimal_float(float_result1))
    if float_flag == 1:
        print(f"Octal: {user_data_int_part}.{user_data_float_part}")
        print(f"Decimal: {int_result + float_result}")
    else:
        print(f"Octal: {user_data_int_part}")
        print(f"Decimal: {int_result}")
elif users_1st_option == 2 and users_2nd_option == 3 and is_valid_octal(user_input_data) == False:
    print('Invalid number instead of octal!')

#08 DEF Decimal to Octal exe
if users_1st_option == 3 and users_2nd_option == 2 and is_valid_decimal(user_input_data) == True:
    int_result1 = decimal_to_bin_int(user_data_int_part)
    int_result = bin_to_oct_int(int_result1)
    if float_flag == 1:
        float_result1 = decimal_to_bin_float(user_data_float_part)
        float_result = bin_to_oct_float(float_result1)
    if float_flag == 1:
        print(f"Decinal: {user_data_int_part}.{user_data_float_part}")
        print(f"Octal: {int_result}.{float_result}")
    else:
        print(f"Decimal: {user_data_int_part}")
        print(f"Octal: {int_result}")
elif users_1st_option == 3 and users_2nd_option == 2 and is_valid_decimal(user_input_data) == False:
    print('Invalid number instead of decimal!')

#09 DEF Hexadecimal to Decimal exe
if users_1st_option == 4 and users_2nd_option == 3 and is_valid_hex(user_input_data) == True:
    int_result = hex_to_decimal_int(user_data_int_part)
    if float_flag == 1:
        float_result = hex_to_decimal_float(user_data_float_part)
    if float_flag == 1:
        print(f"Hexadecimal: {user_data_int_part}.{user_data_float_part}")
        print(f"Decimal: {int(int_result) + float(float_result)}")
    else:
        print(f"Hexadecimal: {user_data_int_part}")
        print(f"Decimal: {int_result}")
elif users_1st_option == 4 and users_2nd_option == 3 and is_valid_hex(user_input_data) == False:
    print('Invalid number instead of hexadecimal!')

#010 DEF Decimal to Hexadecimal exe
if users_1st_option == 3 and users_2nd_option == 4 and is_valid_decimal(user_input_data) == True:
    int_result = deci_to_hex_int(user_data_int_part)
    if float_flag == 1:
        float_result = deci_to_hex_float(user_data_float_part)
    if float_flag == 1:
        print(f'Decimal: {user_data_int_part}.{user_data_float_part}')
        print(f'Hexadecimal: {int_result}.{float_result}')
    else:
        print('Decimal: ',user_data_int_part)
        print('Hecadecimal: ', int_result)
elif users_1st_option == 3 and users_2nd_option == 4 and is_valid_decimal(user_input_data) == False:
    print('Invalid number instead of decimal!')

#011 DEF Octal to Hexadecimal exe
if users_1st_option == 2 and users_2nd_option == 4 and is_valid_octal(user_input_data) == True:
    int_result0 = oct_to_bin_int(user_data_int_part)
    int_result = bin_to_hex_int(int_result0)
    if float_flag == 1:
        float_result0 = oct_to_bin_float(user_data_float_part)
        float_result = bin_to_hex_float(float_result0)
    if float_flag == 1:
        print(f'Octal: {user_data_int_part}.{user_data_float_part}')
        print(f'Hexadecimal: {int_result}.{float_result}')
    else:
        print('Octal: ', user_data_int_part)
        print('Hexadecimal: ', int_result)
elif users_1st_option == 2 and users_2nd_option == 4 and is_valid_octal(user_input_data) == False:
    print('Invalid number instead of octal!')

#012 DEF Hexadecimal to Octal exe
if users_1st_option == 4 and users_2nd_option == 2 and is_valid_hex(user_input_data) == True:
    int_result0 = hex_to_bin_int(user_data_int_part)
    int_result = bin_to_oct_int(int_result0)
    if float_flag == 1:
        float_result0 = hex_to_bin_float(user_data_float_part)
        float_result = bin_to_oct_float(float_result0)
    if float_flag == 1:
        print(f'Hexadecimal: {user_data_int_part}.{user_data_float_part}')
        print(f'Octal: {int_result}.{float_result}')
    else:
        print('Hexadecimal: ', user_data_int_part)
        print('Octal: ', int_result)
elif users_1st_option == 4 and users_2nd_option == 2 and is_valid_hex(user_input_data) == False:
    print('Invalid number instead of hexadecimal!')

#####