"""
    count_nucleotides(strand)

The count of each nucleotide within `strand` as a dictionary.

Invalid strands raise a `DomainError`.

"""
function count_nucleotides(strand)
    nucl_count = Dict('A' => 0, 'G' => 0, 'T' => 0, 'C' => 0)
    for nucl in strand
        if haskey(nucl_count, nucl)
            nucl_count[nucl] += 1
        else
            throw(DomainError(nucl, "is not a nucleotide"))
        end
    end
    return nucl_count
end
