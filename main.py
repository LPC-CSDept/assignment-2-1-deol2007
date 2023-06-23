def main():
    """
    ##################################################
    Complete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    
    num_male = int(input("Enter number of males:"))
    num_female =int(input("Enter number of females:"))

    total_people = num_male + num_female

    m_perc = num_male/total_people * 100
    f_perc = num_female/total_people * 100

    print(f"Total Number of People:{total_people}")
    print(f"Percent of Males:{m_perc:.2f}")
    print(f"Percent of Female:{f_perc:.2f}")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
