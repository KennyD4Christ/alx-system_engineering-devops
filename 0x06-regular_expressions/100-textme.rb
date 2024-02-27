#!/usr/bin/env ruby

# Read each line from the input file
File.open(ARGV[0], "r").each do |line|
  # Match the sender, receiver, and flags using regex
  match_data = line.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
            
  # Output the matched sender, receiver, and flags
  puts "#{match_data[1]},#{match_data[2]},#{match_data[3]}"
end
