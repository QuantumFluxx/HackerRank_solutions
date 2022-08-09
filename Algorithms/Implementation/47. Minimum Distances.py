class Solution:
    def __init__(self):
        self.size = int(input())
        self.array1 = get_int_list(input())

    def calculate(self):
        val_dict = {}
        for i,val in enumerate(self.array1):
            if val in val_dict:
                val_dict[val].append(i)
            else:
                val_dict[val]=[i]
        min_val = None
        for indices in val_dict.values():
            if len(indices) > 1:
                for i in range(0,len(indices)-1):
                    if min_val is None or (indices[i+1]-indices[i]) < min_val:
                        min_val = indices[i+1]-indices[i]
        if min_val is None:
            return -1
        else:
            return min_val


def main():
    my_object = Solution()
    print(my_object.calculate())


def get_int_list(in_str):
    return [int(i) for i in in_str.strip().split()]


if __name__ == "__main__":
    main()