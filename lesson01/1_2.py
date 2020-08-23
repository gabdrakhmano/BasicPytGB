userinput = int(input('Enter time interval in seconds - '))
hours = userinput // 3600
minutes = (userinput % 3600) // 60
seconds = (userinput % 3600) % 60
print('Converted to hh:mm:ss - 'f'{hours:02d}:{minutes:02d}:{seconds:02d}')
