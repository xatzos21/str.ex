# String basics 3

#> **Secret condition** :point_up: : The secret must be at least **8** **characters**.

### The cipher algorithm is :
# * Concatenate the love secret with the love name    
# * Reverse the string
# * Concatenate the revered string with the  year of birth 
# >  ***NOTE:*** We need to cipher the secret itself , 
# not to create a new  ciphered string.

# ### Input
# ```
# *secret:* this_is_my_secret  
# *name:* Max  
# *year:* 1982  
# ```

# ### Output
# ```
# xaMterces_ym_si_siht1982
# ```

secret = "blablabla"
name = "AEK"
year = "1982"

secret2 = secret + name
mysecret = secret2[::-1]


print(mysecret+ year)