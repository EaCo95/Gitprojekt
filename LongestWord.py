# Skapa en metod som du döper till HittaLangstaOrdet. Metoden skall ta som inparameter en array med strängar. 
# Metoden skall loopa igenom arrayen och returnera det längsta ordet.

Lista = ["får", "låda","katt", "fågel"]

def HittaLangstaOrdet(List):
    

    HittaLangstaOrdet = ""
    for string in List:
        if len(string) > len(HittaLangstaOrdet):
            HittaLangstaOrdet = string
    return HittaLangstaOrdet
        
print(HittaLangstaOrdet(Lista))




# l = ["This","is","a","list","of","some","short","and","some","longer","strings"]

# def getLongestString(list_of_strings):
#     longest_string = ""
#     for string in list_of_strings:
#         if len(string) > len(longest_string):
#             longest_string = string
#     return longest_string

# print(getLongestString(l))

# #Output:
# strings
