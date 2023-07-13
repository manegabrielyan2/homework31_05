# file = open('reaganomics.txt', mode='r', encoding='utf-8')
# text = file.read()
# sub = 'Federal income tax and payroll tax levels'
# start_index = text.find(sub)
# flan = text[start_index:]
# file.close()

# fstan = open('output_file.txt', mode='w', encoding='utf-8')
# fstan.write(flan)
# file.close()


with open('reaganomics.txt', mode='r', encoding='utf-8') as file1, \
    open('output_file.txt', mode='w', encoding='utf-8') as file2:
    text = file1.read()
    sub = 'Federal income tax and payroll tax levels'
    start_index = text.find(sub)
    n = text[start_index:]
    file2.write(n)