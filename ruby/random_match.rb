def match(members, group)
  result = members.shuffle
  members_size = members.size
  group_size = group.size

  avg = members_size/group_size

  hash = {}

  group_size.times do |i|
    first = result.sample(avg)
    hash[group[i]] = first
    result = result - first
  end

  result.size.times do |i|
    first = result.sample(1)
    hash[group[i]] << first[0]
    result = result - first
  end


  puts hash
end

arr = [1,2,3,4,5,6,7,8]
group = ['shooter', 'zqw',  'others']
match(arr, group)

puts "-" * 30

arr2 = ('a' .. 'z').to_a
group2 = ['zens', 'hera', 'poseidon', 'venus',  'hermes']
match(arr2, group2)
