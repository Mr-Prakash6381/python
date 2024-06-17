class Invalidmark(Exception):
    pass

try:
    mark=int(input("Enter the mark-?"))
    if(mark<1 or mark>100):
        raise Invalidmark

except Invalidmark:
    print("Invalidmark !!!, The mark should be between 1 to 100")
