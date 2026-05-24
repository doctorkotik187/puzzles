(ns fibonacci)

(defn fibonacci [n]
  (loop [i 0
         a 0
         b 1]
    (println "i: " i ", a: " a ", b: " b)
    (if (= i n)
      a
      (recur (inc i) b (+ a b)))))

(println (fibonacci 21))
