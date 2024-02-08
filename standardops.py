def user_input():
    problem = input("What component is having issues (type 'exit' to exit): ")
    return problem

def operating_procedure(problem): #Defines S.O.P. based on the user input 
    part_list = {
    'gcm': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'rfgw': 'Escalate to DETOPS team | Phone 286322 (Primary) or 286281 (Secondary).',
    'idm': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'idc': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'igm': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'idc': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'ipgw': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'tds': 'Escalate to SDG-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'igw': 'Escalate to SDG-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'omm': 'Escalate to SDG-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'cro': 'Escalate to SDG-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'sgw': 'Escalate to SDG-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
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