(define program (read))

(define (atom? x)
	(and (not (pair? x)) (not (null? x))))

(define (eval s)
	(cond
		((atom? s) s)
		((eq? (car s) '+) (+ (eval (car (cdr s))) (eval (car (cdr (cdr s))))))
		((eq? (car s) '-) (- (eval (car (cdr s))) (eval (car (cdr (cdr s))))))
		((eq? (car s) '*) (* (eval (car (cdr s))) (eval (car (cdr (cdr s))))))
		((eq? (car s) '/) (/ (eval (car (cdr s))) (eval (car (cdr (cdr s))))))
		((eq? (car s) 'atom?) (atom? (car (cdr s))))
		((eq? (car s) 'cons) (cons (car (cdr s)) (car (cdr (cdr s)))))
		)
	)

(display (eval program))
(newline)
