(ns collatz)

(defn collatz [n]
  (loop [n n
         counter 1]
    (println (str "step " counter ": " n))
    (cond
      (< n 1) (println "Please provide a positive integer N.")
      (= n 1) :done
      (even? n) (recur (/ n 2) (inc counter))

      :else (recur (+ (* n 3) 1) (inc counter)))))

(collatz 27)
