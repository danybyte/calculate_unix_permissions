def calculate_unix_permissions():
    while True:
        file_type = input("Enter file type (d for directory, - for regular file, l for symbolic link): ").strip()
        if file_type in ('d', '-', 'l'):
            break
        print("Invalid input. Please enter d, -, or l.")
    def get_yes_no(prompt):
        while True:
            answer = input(prompt).strip().lower()
            if answer in ('y', 'n'):
                return answer
            print("Invalid input. Please enter y or n.")
    
    # Owner permissions
    owner_read = get_yes_no("Owner has read permission? (y/n): ")
    owner_write = get_yes_no("Owner has write permission? (y/n): ")
    owner_execute = get_yes_no("Owner has execute permission? (y/n): ")
    
    # Group permissions
    group_read = get_yes_no("Group has read permission? (y/n): ")
    group_write = get_yes_no("Group has write permission? (y/n): ")
    group_execute = get_yes_no("Group has execute permission? (y/n): ")
    
    # Other permissions
    other_read = get_yes_no("Others have read permission? (y/n): ")
    other_write = get_yes_no("Others have write permission? (y/n): ")
    other_execute = get_yes_no("Others have execute permission? (y/n): ")
    
    permissions_code = ""
    
    # File type character
    if file_type == 'd':
        permissions_code += 'd'
    elif file_type == 'l':
        permissions_code += 'l'
    else:
        permissions_code += '-'
    
    # Owner permissions
    permissions_code += 'r' if owner_read == 'y' else '-'
    permissions_code += 'w' if owner_write == 'y' else '-'
    permissions_code += 'x' if owner_execute == 'y' else '-'
    
    # Group permissions
    permissions_code += 'r' if group_read == 'y' else '-'
    permissions_code += 'w' if group_write == 'y' else '-'
    permissions_code += 'x' if group_execute == 'y' else '-'
    
    # Other permissions
    permissions_code += 'r' if other_read == 'y' else '-'
    permissions_code += 'w' if other_write == 'y' else '-'
    permissions_code += 'x' if other_execute == 'y' else '-'
    
    # Calculate
    owner_num = (4 if owner_read == 'y' else 0) + (2 if owner_write == 'y' else 0) + (1 if owner_execute == 'y' else 0)
    group_num = (4 if group_read == 'y' else 0) + (2 if group_write == 'y' else 0) + (1 if group_execute == 'y' else 0)
    other_num = (4 if other_read == 'y' else 0) + (2 if other_write == 'y' else 0) + (1 if other_execute == 'y' else 0)
    
    numeric_code = f"{owner_num}{group_num}{other_num}"
    
    print(f"The generated Unix permission code is: {permissions_code}")
    print(f"The numeric permission code is: {numeric_code}")

calculate_unix_permissions()
