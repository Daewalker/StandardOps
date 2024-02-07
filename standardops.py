def user_input():
    problem = input("What component is having issues (type 'exit' to exit): ")
    return problem

def operating_procedure(problem): #Defines S.O.P. based on the user input 
    part_list = {
    'gcm': 'Escalate to CNE-Gategway team | Phone 884140 (Primary) or 884141 (Secondary)',
    '': '', # Allows for procedure growth
    }
    
    # Begin the loop
    if problem.lower() == 'exit':
        return False    # Break loop
        
    if problem.lower() in part_list:
        sop = part_list[problem.lower()]
        print(f"\nStandard SOP for {problem}: is {sop}\n")
    else: 
        print(f"\nSorry, no S.O.P. found for this {problem}. Check with a Senior Tech.\n")
        
    return True # Continues the loop
    
def display_banner():
    banner = """
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    *          Standard Ops Tool         *
    *         Created for the NMC        *
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    """
    print(banner)
    
def main():
    display_banner()
    
    while True:
        problem = user_input()
        if not operating_procedure(problem):
            break # Kill program
            
if __name__ == "__main__":
    main()