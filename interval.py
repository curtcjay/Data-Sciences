#define a class to change a string to a interval
class interval:
    def __init__(self, string = ''):
        
        self.string = string.replace(' ', '')
        self.lower_sym = self.string[0]
        self.upper_sym = self.string[-1]
        separate = self.string.index(',')
        self.lower_num = int(self.string[1:separate])
        self.upper_num = int(self.string[separate+1:-1])
        
        if self.lower_sym == '[':
            self.lower_sym_exclusive = 0
        elif self.lower_sym == '(':
            self.lower_sym_exclusive = 1
        if self.upper_sym == ']':
            self.upper_sym_exclusive = 0
        elif self.upper_sym == ')':
            self.upper_sym_exclusive = 1
        
        if self.lower_num + self.lower_sym_exclusive + self.upper_sym_exclusive > self.upper_num:
            raise Exception('Invalid interval')
                    
    def __repr__(self):
        return self.string

#function to merge two intervals
def mergeIntervals(int1, int2):
    
    if int1.upper_num - int1.upper_sym_exclusive < int2.lower_num + int2.lower_sym_exclusive - 1 or int2.upper_num - int2.upper_sym_exclusive < int1.lower_num + int1.lower_sym_exclusive - 1:
        raise Exception('No overlapping intervals')
        
    else:
        
        merged = ''
        
        if int1.upper_num - 0.5*int1.upper_sym_exclusive >= int2.upper_num - 0.5*int2.upper_sym_exclusive:
            upper_num = int1.upper_num
            upper_sym = int1.upper_sym
        else:
            upper_num = int2.upper_num
            upper_sym = int2.upper_sym
            
        if int1.lower_num + 0.5*int1.lower_sym_exclusive <= int2.lower_num + 0.5*int2.lower_sym_exclusive:
            lower_num = int1.lower_num
            lower_sym = int1.lower_sym
        else:
            lower_num = int2.lower_num
            lower_sym = int2.lower_sym
            
        merged = merged + lower_sym + str(lower_num) + ',' + str(upper_num) + upper_sym
        
        int_merged = interval(merged)
        
    return int_merged   

#function to merge all overlapping intervals
def mergeOverlapping(intlist):
    
    def getkey(itv):
        return itv.lower_num + 0.5*itv.lower_sym_exclusive
    p = sorted(intlist, key=getkey)
    
    merged_init = p[0]
    merged_all = []
    
    for i in range(1, len(p)):
        try:
            merged_init = mergeIntervals(merged_init, p[i])
            
        except Exception:
            merged_all.append(merged_init)
            merged_init = p[i]
    
    merged_all.append(merged_init)
    
    return merged_all

#function to insert a new interval to a existing interval list
def insert(intlist, newint):
    intlist.append(newint)
    return mergeOverlapping(intlist)

#final program
def main():
    initial = raw_input('List of intervals?')
    init_list = initial.split(', ')
    intlist = []
    try:
        for i in init_list:
            intlist.append(interval(i))
    except:
        print 'Invalid interval'
    while True:
        addint = raw_input('Interval?')
        if addint == 'quit':
            break
        else:
            try:
                newint = interval(addint)
            except:
                print 'Invalid interval'
                continue
            intlist = insert(intlist, newint)
            print intlist

if __name__ == '__main__':
    main()