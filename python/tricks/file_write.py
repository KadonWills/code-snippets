#-------------------------------------------------
# support for writing output to a file
#-------------------------------------------------
def writeln(f, *args):
    for arg in args:
        f.write(str(arg))
    f.write("\n")
