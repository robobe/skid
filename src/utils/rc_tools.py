
class lpf():
    def __init__(self, base=0, factor=0.8):
        self.__factor = factor
        self.__history = base

    def update(self, value):
        self.__history += (value * self.__factor)
        self.__history /= 2
        return self.__history
    
class map_utils():
    def __init__(self, in_lower, in_upper, out_lower, out_upper):
        self.__in_l = in_lower
        self.__in_h = in_upper
        self.__out_l = out_lower
        self.__out_h = out_upper

    def map_range(self, value):
        return norm((self.__in_l,self.__in_h),
        (self.__out_l, self.__out_h),
        value)

def norm(in_range: tuple, out_range: tuple, value):
    inLower, inUpper = in_range
    outLower, outUpper = out_range
    inSpan = inUpper - inLower
    outSpan = outUpper - outLower
    scaled = float(value-inLower)/ float(inSpan)
    result = outLower + (scaled * outSpan)
    return result

if __name__ == "__main__":
    r = norm((0,640), (-1,1), 320)
    print(r)

    m = map_utils(-1, 1, 1000, 2000)
    print(m.map_range(0))
