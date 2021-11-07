from morseCodeConvert import Convert
convert=Convert()
end=False

while not end:
    response=convert.userInputProcess()
    if response=='n':
        end=True

