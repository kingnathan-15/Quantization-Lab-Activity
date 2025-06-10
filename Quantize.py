def Quantize(maxRange, minRange, sampleRate, bitRate, analogVoltage):
    maxRange = float(maxRange)
    minRange = float(minRange)
    sampleRate = float(sampleRate)
    bitRate = float(bitRate)
    analogVoltage = float(analogVoltage)

    quantizationLevels = 2 ** bitRate
    quantizationStep = (maxRange - minRange) / quantizationLevels
    if quantizationStep != 0:
        index = round((analogVoltage - minRange) / quantizationStep)
    else:
        index = 0

    if index < 0:
        index = 0
    elif index >= quantizationLevels:
        index = quantizationLevels - 1
    
    quantizedValue = minRange + index * quantizationStep
    return quantizedValue