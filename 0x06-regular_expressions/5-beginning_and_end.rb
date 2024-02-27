#!/usr/bin/env ruby
# Match the pattern that starts with 'h', has any single character in between, and ends with 'n'
puts ARGV[0].scan(/^h.n$/).join
