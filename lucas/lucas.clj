(ns lucas)

(defn lucas [n]
  (loop [i 0
         a 2N
         b 1N]
    (println "i: " i ", a: " a ", b: " b)
    (if (= i n)
      a
      (recur (inc i) b (+ a b)))))

(println (lucas 100))
