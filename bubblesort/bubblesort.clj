(ns bubblesort)

(defn bubble-pass [coll]
  (reduce (fn [acc x]
            (if (> (last acc) x)
              (conj (pop acc) x (last acc))
              (conj acc x)))
          [(first coll)]
          (rest coll)))

(defn bubble-sort [coll]
  (let [passed (bubble-pass coll)]
    (if (= passed coll)
      coll
      (recur passed))))

(println (bubble-sort [5 3 1 4 2]))  ; [1 2 3 4 5]
