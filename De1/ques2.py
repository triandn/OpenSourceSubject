def get_occurrence_of_all_characters(inp_str):
  
    #frequency dictionary
    freq = {}   
    for ele in inp_str: 
        if ele in freq: 
            freq[ele] += 1
        else: 
            freq[ele] = 1 

    print ("Ket qua :\n "+ str(freq)) 

get_occurrence_of_all_characters('w3resource')