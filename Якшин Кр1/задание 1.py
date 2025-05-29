def first_last(letter, st):
    first_index = st.find(letter)
    if first_index == -1:
        return (None, None)
    
    last_index = st.rfind(letter)
    return (first_index, last_index)

print(first_last('a', 'banana'))  
print(first_last('z', 'banana'))  
print(first_last('n', 'banana'))  
