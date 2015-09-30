quicksort :: (Ord a) => [a] -> [a]

quicksort [] = []

quicksort(x:xs) =
  let smallSorted = quicksort [a | a <- xs, a <= x ]
      bigSorted   = quicksort [a | a <- xs, a > x ]
  in smallSorted ++ [x] ++ bigSorted
