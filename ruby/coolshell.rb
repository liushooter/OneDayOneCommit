# [abcdefghijklmnopqrstuvwxyz] <=> [pvwdgazxubqfsnrhocitlkeymj]

# Wxgcg txgcg ui p ixgff, txgcg ui p epm. I gyhgwt mrl lig txg ixgff wrsspnd tr irfkg txui hcrvfgs, nre, hfgpig tcm liunz txg crt13 ra "ixgff" tr gntgc ngyt

# def rot13(value)
#   return value.tr 'A-Za-z', 'N-ZA-Mn-za-m'
# end


left =  "abcdefghijklmnopqrstuvwxyz"
right = "pvwdgazxubqfsnrhocitlkeymj"

text =  "Wxgcg txgcg ui p ixgff, txgcg ui p epm. I gyhgwt mrl lig txg ixgff wrsspnd tr irfkg txui hcrvfgs, nre, hfgpig tcm liunz txg crt13 ra 'ixgff' tr gntgc ngyt fgkgf."

hash = {}

arr = right.split('')

arr.each_with_index do |val, i|
  hash.merge!(val => left[i])
end

puts hash

result = ""

text.split('').each do |t|
  result <<  (hash["#{t}"].nil? ? t : hash["#{t}"])
end

puts result
