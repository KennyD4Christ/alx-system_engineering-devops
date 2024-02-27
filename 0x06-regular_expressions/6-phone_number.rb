#!/usr/bin/env ruby
# Match the pattern of a 10-digit phone number
puts ARGV[0].scan(/\A\d{10}\z/).join
