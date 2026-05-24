(ns pi)

(defn inside-circle? [p]
  (let [[x y] p]
    (<= (+ (* x x)
           (* y y))
        1)))

(defn monte-carlo [n]
  (let [points (repeatedly n #(vector (- (rand 2) 1)
                                      (- (rand 2) 1)))
        inside (filter #(inside-circle? %) points)]
    (* 4.0 (/ (count inside) n))))

(println (monte-carlo 1000000))
