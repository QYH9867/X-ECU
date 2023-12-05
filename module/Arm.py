def read_file(file_name):
    '''
    Used for reading firmware. Due to variations in file formats resulting from
    different tools or methods used for extraction, modifications may be required here
    based on the different file types. Here, we convert the original firmware to a hexadecimal string,
    save it as TXT, where every two characters correspond to one byte.
    This allows easy and universal use of this function for reading.
    '''
    with open(file_name, 'r') as f:
        data = f.read()
    return data

def search_instructions(data):
    '''
    #Find the addresses of all 'BL' instructions in the ECU firmware.
    Since reverse engineering ECU firmware is done in terms of bytes,
    we convert the results to corresponding addresses in byte addressing for
    convenient reverse engineering.
    '''
    address = []
    for i in range(0,len(data)-7,4):
        # Check the conditions
        if int(data[i+2],16) == 0xf and int(data[i+3],16) == 0x0: # Check whether it is backward or forward
            if int(data[i+6],16) == 0xf and int(data[i+7],16) >= 0x8: # Check whether it further satisfies Cbackward
                position = hex(int(i/2))
                address.append(position)
        elif int(data[i+2],16) == 0xf and int(data[i+3],16) == 0x7: # Check whether it is backward or forward
            if int(data[i+6],16) == 0xf and int(data[i+7],16) >= 0x8: # Check whether it further satisfies Cforward
                position = hex(int(i/2))
                address.append(position)
    return address

def output_results(address):
    '''
    Used to output all addresses, displaying 10 addresses per line.
    '''
    print(f'There are {len(address)} \'BL\' instructions found in this ECU firmware(Arm Architecture):')
    for i in range(len(address)):
        if i%10 == 9:
            print(f'{address[i]:<8}')
        else:
            print(f'{address[i]:<8}', end=' ')
def Arm(file_name):
    '''
    Encapsulate the aforementioned functions into a single function for ease of invocation.
    input: file_name
    '''
    data = read_file(file_name)
    address = search_instructions(data)
    output_results(address)

if __name__ == '__main__':
    Arm('../Arm.txt')