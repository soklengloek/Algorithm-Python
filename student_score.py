def main():
    print ("Student Score Calculator")
    print ("------------------------")
    java = int(input("Enter Java score: "))
    python = int(input("Enter Python score: "))
    php = int(input("Enter PHP score: "))
    english = int(input("Enter English score: "))
    return java, python, php, english
def process(java, python, php, english):
    total_score = java + python + php + english
    average_score = total_score / 4
    print ("Total Score:", total_score)
    print ("Average Score:", average_score)
    #Process
    if average_score >= 90:
        print ("Grade: A")
    elif average_score >= 80:
        print ("Grade: B")
    elif average_score >= 70:
        print ("Grade: C")
    elif average_score >= 60:
        print ("Grade: D")
    elif average_score >= 50:
        print ("Grade: E")
    else:
        print ("Grade: F")
java, python, php, english = main()
process(java, python, php, english)
