import sys

arguments = sys.argv

# for index in range(len(arguments)):
#     if(arguments[index] == "--in"):
#         file_in  = arguments[index + 1]
#     if(arguments[index] == "--out"):
#         file_out = arguments[index + 1]

file_input = open("in.txt", 'r')
php_code = file_input.read().lower()
obfuscated = """$_="";$____="";$__=[]."_";"""
obfuscated += """$______=$__["."=="."];"""
tmp = "$______++;"*9
obfuscated = obfuscated + tmp
obfuscated += """$___=$______["."=="+"];$_____=$______["."=="+"];"""

php_code_function_list =  []
php_code_param_list = []
php_code_function = php_code[:php_code.find('(')]
php_code_param = php_code[php_code.find('(') + 2 : php_code.find(')') -1]

php_code_function_list[:] = php_code_function
php_code_param_list[:] = php_code_param

print(php_code_function_list)
print(php_code_param_list)

for c in php_code_param_list:
    if c.isalpha():   
        obfuscated += '$_____++;'*(ord(c) - ord('a'))
        obfuscated += '$____=$____.$_____;'
        obfuscated += '$_____=$______["."=="+"];'
    else:
        if (c == '"'):
            obfuscated += "$____.='{0}';".format('\"')
        else:
            obfuscated += '$____.="{0}";'.format(c)

for c in php_code_function_list:
    if c.isalpha():   
        obfuscated += '$___++;'*(ord(c) - ord('a'))
        obfuscated += '$_=$_.$___;'
        obfuscated += '$___=$______["."=="+"];'
    else:
        if (c == '"'):
            obfuscated += "$_=$_.'{0}';".format('\"')
        else:
            obfuscated += '$_=$_."{0}";'.format(c)

obfuscated += "$_($____);"
with open("out.txt", 'w') as file_output:
    file_output.write(obfuscated)