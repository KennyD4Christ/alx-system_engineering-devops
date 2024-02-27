#!/usr/bin/env ruby

def match_school(string)
  # Using the scan method to find matches and joining them with an empty string
  puts string.scan(/School/).join
end

match_school(ARGV[0])
