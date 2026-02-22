local function is_prime(num)
  if num < 2 then return false end
  for i = 2, math.sqrt(num) do
    if num % i == 0 then return false end
  end
  return true
end

for i = 1, 20 do
  if is_prime(i) then
    print(i .. " é primo")
  end
end
