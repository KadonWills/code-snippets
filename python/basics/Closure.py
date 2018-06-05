# Create a closure with mutable attribute: index
def test_closure(max):
    index = {1:-1}
    def enclosed():
        if index[1] <= max:
           index[1] += 1
           return index[1]
        else:
           return -1
    return enclosed

def main():
    # use closure based function my_scan()
    my_scan = test_closure(5);
    for i in range(0,5):
        print(i,'->',my_scan())


# compiler entry point
if __name__ == "__main__":
    main()