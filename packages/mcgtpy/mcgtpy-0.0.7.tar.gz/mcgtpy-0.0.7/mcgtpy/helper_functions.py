def columns_janitor(old_col_names):
    """
    input:    list
    output:   list
    """
    new_col_names_list = []
    for col_name in old_col_names:
        # strip whitespace
        col_name = col_name.strip()
        # make lowercase
        col_name = col_name.lower()
        # replace " " with "_"
        col_name = col_name.replace(" ", "_")
        # replace "." with "_"
        col_name = col_name.replace(".", "_")
        # remove weird characters
        new_col_name = "".join(
            item for item in str(col_name) if item.isalnum() or item == "_"
        )
        # make sure there are 0 instances of 2 _'s next to each other
        while "__" in new_col_name:
            new_col_name = new_col_name.replace("__", "_")
        # make sure the column name does not lead or end with _
        while new_col_name[0] == "_":
            new_col_name = new_col_name[1 : len(new_col_name)]
        while new_col_name[len(new_col_name) - 1] == "_":
            new_col_name = new_col_name[0 : len(new_col_name) - 1]
        # append item to list of new columns
        new_col_names_list.append(new_col_name)

    # at end of loop, return the new columns 
    return new_col_names_list