gets.to_i.times{
    x = gets.split.map(&:to_i)
    print 2 * x[2] - x[0], ' ', 2 * x[3] - x[1], "\n"
}