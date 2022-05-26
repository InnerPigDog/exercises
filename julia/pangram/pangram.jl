"""
    ispangram(input)

Return `true` if `input` contains every alphabetic character (case insensitive).

"""
function ispangram(input)
    for letter in "abcdefghijklmnopqrstuvwxyz"
        if !(letter  in lowercase(input))
            return false
        end
    end
    return true
    
    # Much more elegant solution:
    # return 'a':'z' ⊆ lowercase(input)
end


