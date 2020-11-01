
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
    in_lower, in_upper = in_range
    out_lower, out_upper = out_range
    ratio = value / in_upper - in_lower
    result = out_lower + ratio * (out_upper-out_lower)
    return result

if __name__ == "__main__":
    r = norm((0,640), (-1,1), 640)
    print(r)

    m = map_utils(0, 640, -1, 1)
    print(m.map_range(320))
