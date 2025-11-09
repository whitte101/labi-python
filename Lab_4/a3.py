def main():
    packets = input("введите 0 и/или 1:")

    if len(packets) < 5:
        print("минимальное количество пакетов 5!!!")
        return
    
    if not all(char in "01" for char in packets):
        print('допустимы только 0 и 1!!!')
        return
    
    vse_pakets = len(packets)

     
              
              