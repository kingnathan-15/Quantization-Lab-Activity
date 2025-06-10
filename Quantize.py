maxRange =  input("Input a maximum range: ")
minRange =  input("Input a minimum range: ")
sampleRate =  input("Input a sample rate: ")
bitRate =  input("Input a bit rate: ")
analogVoltage =  input("Input an analog voltage: ")

def Quantize(maxRange, minRange, sampleRate, bitRate, analogVoltage):
    maxRange = float(maxRange)
    minRange = float(minRange)
    sampleRate = float(sampleRate)
    bitRate = float(bitRate)
    analogVoltage = float(analogVoltage)

    quantizationLevels = 2 ** bitRate
    quantizationStep = (maxRange - minRange) / quantizationLevels
    index = round((analogVoltage - minRange) / quantizationStep)

    if index < 0:
        index = 0
    elif index >= quantizationLevels:
        index = quantizationLevels - 1
    
    quantizedValue = minRange + index * quantizationStep
    return quantizedValue

quantizedValue = Quantize(maxRange, minRange, sampleRate, bitRate, analogVoltage)
print(f"Quantized Value: {quantizedValue}")