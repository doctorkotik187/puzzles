(ns distance)

(defn euclid [a b]
  (let [[x1 y1] a
        [x2 y2] b
        dx (- x1 x2)
        dy (- y1 y2)]
    (Math/sqrt (+ (* dx dx) (* dy dy)))))

(println (euclid [1 1] [2 2]))
