import re

with open('preproinsulin-seq.txt', 'r') as file:
    file_content = file.read()
    print(file_content)
    
    print("--------")
    
cleaned_content = re.sub(r'^ORIGIN\s*', '', file_content, flags=re.MULTILINE) # removes 'origin'
print(cleaned_content)

cleaned_content = re.sub(r'\d+', '', cleaned_content) # removes 'numbers'
print(cleaned_content)

cleaned_content = re.sub(r'\/\/', '', cleaned_content) # removes '//'
print(cleaned_content)

cleaned_content = re.sub(r'\s+', '', cleaned_content) # removes 'spaces with a single space'
print(cleaned_content)

cleaned_content = re.sub(r'[\r\n]+', '', cleaned_content) # removes 'line breaks and carriage returns'
print(cleaned_content)


