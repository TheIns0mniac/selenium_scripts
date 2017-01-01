#Displays the multiplication table of the number specified by the user.

#Lets the user enter a number of their choice.
puts "Enter a number whose multiplication table you would like to have displayed: "
number = gets.chomp.to_i #"to.i" converts the string to an integer.
puts """
- 1 X #{number} = #{number * 1}
- 2 X #{number} = #{number * 2}
- 3 X #{number} = #{number * 3}
- 4 X #{number} = #{number * 4}
- 4 X #{number} = #{number * 5}
- 4 X #{number} = #{number * 6}
- 4 X #{number} = #{number * 7}
- 4 X #{number} = #{number * 8}
- 4 X #{number} = #{number * 9}
- 4 X #{number} = #{number * 10}
"""