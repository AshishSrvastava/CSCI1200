import os
def main():
    """Removes the files that are createed by HW6 ipynb
    """
    file_path = os.path.join(os.path.dirname( __file__ ))
    os.chdir(file_path)
    os.remove("chosen_improved.txt")
    os.remove("chosen_students.txt")
    os.remove("extra_chosen_improved.txt")
    os.remove("outliers.txt")
    os.remove("student_scores.csv")

if __name__ == "__main__":
    main()