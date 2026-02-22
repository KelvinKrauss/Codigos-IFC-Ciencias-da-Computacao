local matrix = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
}

local function transpose(m)
  local t = {}
  for i = 1, #m[1] do
    t[i] = {}
    for j = 1, #m do
      t[i][j] = m[j][i]
    end
  end
  return t
end

local t_matrix = transpose(matrix)

for i = 1, #t_matrix do
  for j = 1, #t_matrix[1] do
    io.write(t_matrix[i][j] .. " ")
  end
  print()
end
