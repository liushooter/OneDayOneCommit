require 'open3'
require "open4"

##########Open3##########

Open3.popen3("echo '邹倩雯' ") do |io, stdout, stderr, thread|
  io.write "love"
  io.close
  puts io.class
  puts stdout.read
  puts stderr.read
  puts thread.class
end

stdin, stdout, stderr = Open3.popen3("date")
puts stdout.read
puts stderr.read

##########Open4##########

pid, stdin, stdout, stderr = Open4::popen4 "cal"

puts pid
puts stdout.read
puts stderr.read

# http://tech.natemurray.com/2007/03/ruby-shell-commands.html
