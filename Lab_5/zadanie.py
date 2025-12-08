def func (text):
    result = text
    
    while True:
        start = result.find('(')
        if start == -1:
            break
            
        end = result.find(')', start)
        if end == -1:
            break
            
        to_replace = result[start:end + 1]
        result = result.replace(to_replace, '', 1)
    print(result)
func(input('текст: '))   