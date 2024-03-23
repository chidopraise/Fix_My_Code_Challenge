###
#
#  Sort integer arguments (ascending) 
#
###

result = []
ARGV.each do |arg|
    # skip if not integer
    next if arg !~ /^-?[0-9]+$/

    # convert to integer
    i_arg = arg.to_i
    
    # insert result at the right position
    result.insert(result.bsearch_index { |x| x >= i_arg }.to_i || result.size, i_arg)
end

puts result
